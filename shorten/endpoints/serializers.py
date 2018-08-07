from rest_framework import serializers
from endpoints.models import ShortenedUrls
from endpoints.utils import get_shortened_url


class UrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortenedUrls
        fields = ('url',)
        extra_kwargs = {'url': {'write_only': True}}

    def create(self, validated_data):
        url_object, created = self.Meta.model.objects.get_or_create(
            url=validated_data['url']
        )
        return url_object

    def to_representation(self, url_object):
        response = super(UrlSerializer, self).to_representation(url_object)
        response['shortened_url'] = get_shortened_url(
            self.context.get('request'), url_object.id
        )
        return response
