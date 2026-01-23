from django.test import TestCase
from django.urls import reverse

class SimpleProjectTests(TestCase):
    
    def test_homepage_status_code(self):
        """Verify that the homepage loads successfully."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Verify the correct template is used for the index page."""
        # This assumes you have a URL named 'index' or 'home'
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/index.html')

    def test_homepage_contains_correct_html(self):
        """Verify the homepage contains the expected welcome text."""
        response = self.client.get('/')
        self.assertContains(response, '<h1>Welcome</h1>')