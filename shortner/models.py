from django.db import models


class Links(models.Model):
  url_original = models.URLField()
  url_curta = models.CharField(max_length=60, unique=True)
  data_hora_de_cadastro = models.DateTimeField(auto_now_add=True)
  
  def __srt__(self) -> str:
    return self.link_encurtado