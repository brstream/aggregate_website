from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from layouts import Layouts

def __init__(self, request):
    self.request = request

@view_config(route_name='list', renderer='list.mako')
def list_view(request):
    rs = request.db.execute("select id, text from events")
    events = [dict(id=row[0], text=row[1]) for row in rs.fetchall()]
    return {'events': events}
 
@view_config(context='pyramid.exceptions.NotFound',
             renderer='notfound.mako')
def notfound_view(self):
    return {}
