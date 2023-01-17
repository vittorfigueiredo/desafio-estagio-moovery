from rest_framework import serializers

from .models import Links


class LinksSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Links
    fields = (
      'id',
      'url_original',
      'url_curta',
      'data_hora_de_cadastro',
    )