import os
import logging

from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.httpexceptions import HTTPFound
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.view import view_config

from wsgiref.simple_server import make_server

import sqlite3

import requests
from lxml import html

import re

from urllib.parse import urlsplit

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

# a tag grabber
def grab_urls(site):
    page_text = requests.get(site).text
    parsed = html.fromstring(page_text[38:])
    urls = parsed.cssselect('a')
    urllist = [dict(text=e.text, url=e.get('href')) for e in urls]
    return urllist
    
# views
@view_config(route_name='list', renderer='list.mako')
def list_view(request):
    rs = request.db.execute("select id, name from tasks where closed = 0")
    tasks = [dict(id=row[0], name=row[1]) for row in rs.fetchall()]
    return {'tasks': tasks}

@view_config(route_name='new', renderer='new.mako')
def new_view(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            request.db.execute('insert into tasks (name, closed) values (?, ?)',
                               [request.POST['name'], 0])
            request.db.commit()
            request.session.flash('New task was successfully added!')
            return HTTPFound(location=request.route_url('list'))
        else:
            request.session.flash('Please enter a name for the task!')
    return {}

@view_config(route_name='close')
def close_view(request):
    task_id = int(request.matchdict['id'])
    request.db.execute("update tasks set closed = ? where id = ?", (1, task_id))
    request.db.commit()
    request.session.flash('Task was successfully closed!')
    return HTTPFound(location=request.route_url('list'))

@view_config(context='pyramid.exceptions.NotFound', renderer='notfound.mako')
def notfound_view(self):
    return {}

@view_config(route_name='aggregate', renderer='aggregate.mako')
def aggregate_view(request):
    rs = request.db.execute("select id, text, url from urls")
    urls = [dict(id=row[0], text=row[1], url=row[2]) for row in rs.fetchall()]
    return {'urls': urls}

@view_config(route_name='newsite', renderer='newsite.mako')
def new_site_view(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            s = urlsplit(request.POST['name'])
            root_url = "http://" + s.netloc + s.path.rstrip(re.findall('/.*$', s.path)[0])
            full_url = "http://" + s.netloc + s.path
            urllist = grab_urls(full_url)
            if urllist:
                for item in urllist:
                    if item['url'] == None:
                        continue
                    if item['url'][0] == '/' or '#':
                        item['url'] = root_url + item['url']
                    if item['text'] == None:
                        item['text'] = item['url']
                    request.db.execute('insert into urls (url, text) values (?, ?)',
                                       [item['url'], item['text']])
                    request.db.commit()
            request.session.flash('New URLs were successfully added!')
            return HTTPFound(location=request.route_url('aggregate'))
        else:
            request.session.flash('Please enter a URL to scrape!')
    return {}


# subscribers
@subscriber(NewRequest)
def new_request_subscriber(event):
    request = event.request
    settings = request.registry.settings
    request.db = sqlite3.connect(settings['db'])
    request.add_finished_callback(close_db_connection)

def close_db_connection(request):
    request.db.close()
    
@subscriber(ApplicationCreated)
def application_created_subscriber(event):
    log.warn('Initializing database...')
    f = open(os.path.join(here, 'schema.sql'), 'r')
    stmt = f.read()
    settings = event.app.registry.settings
    db = sqlite3.connect(settings['db'])
    db.executescript(stmt)
    db.commit()
    f.close()

if __name__ == '__main__':
    # configuration settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['mako.directories'] = os.path.join(here, 'templates')
    settings['db'] = os.path.join(here, 'tasks.db')
    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    # configuration setup
    config = Configurator(settings=settings, session_factory=session_factory)
    # routes setup
    config.add_route('list', '/')
    config.add_route('new', '/new')
    config.add_route('close', '/close/{id}')
    config.add_route('aggregate', '/aggregate')
    config.add_route('newsite', '/newsite')
    # static view setup
    config.add_static_view('static', os.path.join(here, 'static'))
    # scan for @view_config and @subscriber decorators
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

