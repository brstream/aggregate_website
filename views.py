from pyramid.view import view_config

from layouts import Layouts

class PlumVillageViews(Layouts):

    def __init__(self, request):
        self.request = request

    @view_config(renderer="templates/index.pt")
    def index_view(self):
        return {"page_title": "Home"}
