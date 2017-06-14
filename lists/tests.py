from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>G-CRM</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')


    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text':'A New list item'})
        self.assertIn('A New list item',response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
