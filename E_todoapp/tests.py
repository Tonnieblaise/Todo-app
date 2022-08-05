from django.test import TestCase

# Create your tests here.
class Tests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200 )

    def test_update_page_status_code(self):
        response = self.client.get('update')
        self.assertEqual(response.status_code,404 )