from hashids import Hashids
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import Http404
from endpoints.models import ShortenedUrls


def encode_url_id(url_id):
    h = Hashids(min_length=8, salt=settings.URL_SALT)
    return h.encode(url_id)


def decode_url_string(url_string):
    h = Hashids(min_length=8, salt=settings.URL_SALT)
    result = h.decode(url_string)
    if result:
        return result[0]


def get_full_url(shortened_url):
    decoded_url_id = decode_url_string(shortened_url)
    if not decoded_url_id:
        raise Http404()
    shortened_url = get_object_or_404(ShortenedUrls, id=decoded_url_id)
    return shortened_url.url


def get_shortened_url(request, url_id):
    slug = encode_url_id(url_id)
    return '{scheme}://{host}/{slug}'.format(
        scheme=request.META['wsgi.url_scheme'],
        host=request.get_host(), slug=slug
    )
