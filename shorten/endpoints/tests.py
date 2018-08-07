from django_webtest import WebTest

from endpoints.models import ShortenedUrls
from endpoints.utils import encode_url_id


class ShortenUrlViewTests(WebTest):

    def test_get_home_view(self):
        response = self.app.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Marcus Patino Pan', response.text)

    def test_get_about_view(self):
        response = self.app.get('/about/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('About - Marcus Patino Pan', response.text)

    def test_get_shorten_url_view_not_allowed(self):
        response = self.app.get('/shorten_url/', status=405)
        self.assertEquals(response.status_code, 405)
        self.assertEquals(
            response.json, {'detail': 'Method "GET" not allowed.'}
        )

    def test_post_invalid_url_to_shorten_url_view(self):
        response = self.app.post_json(
            '/shorten_url/', params={'url': 'hello'}, status=400
        )
        self.assertEquals(response.json, {'url': ['Enter a valid URL.']})

    def test_post_without_http_url_to_shorten_url_view_is_invalid(self):
        response = self.app.post_json(
            '/shorten_url/', params={'url': 'www.google.com'}, status=400
        )
        self.assertEquals(response.json, {'url': ['Enter a valid URL.']})

    def test_post_valid_url_to_shorten_url_view(self):
        response = self.app.post_json(
            '/shorten_url/',
            params={'url': 'http://www.google.com'},
            status=201
        )
        self.assertEquals(
            response.json, {'shortened_url': 'http://testserver/l2YRm1Kn'}
        )

    def test_invalid_redirect_shortened_url_view(self):
        response = self.app.get('/imadethisup/', status=302)
        response = response.follow()
        self.assertEquals(response.url, b'')
        self.assertIn('Marcus Patino Pan', response.text)

    def test_redirect_url_view(self):
        about_url, _ = ShortenedUrls.objects.get_or_create(
            url='http://testserver/about/'
        )
        slug = encode_url_id(about_url.id)
        response = self.app.get('/{slug}/'.format(slug=slug))
        self.assertEquals(response.url, 'http://testserver/about/')
        response = response.follow()
        self.assertIn(b'About - Marcus Patino Pan', response)
