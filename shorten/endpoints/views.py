from django.http import Http404
from django.urls import reverse
from django.views.generic.base import RedirectView, TemplateView
from rest_framework.generics import CreateAPIView
from endpoints.serializers import UrlSerializer
from endpoints.utils import get_full_url


class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ShortenUrlView(CreateAPIView):
    serializer_class = UrlSerializer


class RedirectUrlView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        path = self.kwargs['slug']
        try:
            return get_full_url(path)
        except Http404:
            return reverse('home')
