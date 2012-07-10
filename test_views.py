import unittest

from pyramid.testing import DummyRequest
from pyramid.testing import setUp
from pyramid.testing import tearDown

class PlumVillageViewsUnitTests(unittest.TestCase):
    def setUp(self):
        request = DummyRequest()
        self.config = setUp(request=request)

    def tearDown(self):
        tearDown()

    def _makeOne(self, request):
        from views import PlumVillageViews

        inst = PlumVillageViews(request)
        return inst

    def test_index_view(self):
        request = DummyRequest()
        inst = self._makeOne(request)
        result = inst.index_view()
        self.assertEqual(result['page_title'], 'Home')
