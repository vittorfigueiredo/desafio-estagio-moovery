import random
import string

from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Links
from .serializer import LinksSerializer


def random_generator(size=10, chars=string.ascii_letters + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

def home(request):
  links = Links.objects.all()
  return render(request, 'home.html', context= {
    'links': links,
  })

class LinksView(APIView):
    def get(self, format=None):
        links = Links.objects.all()
        serializer = LinksSerializer(links, many=True)

        return Response({'links': serializer.data})
  
class ShortnerApiView(APIView):
  def post(self, request, format=None):
        data = {
            'url_original': request.POST.get('link_original', ''),
            'url_curta': 'http://moove.ry/' + random_generator(),
            'created_by': self.request.user.id
        }

        serializer = LinksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class RedirectView(APIView):
    def get(self, request, url_curta, format=None):
        url_curta = self.kwargs.get('url_curta')

        try:
            filtered_link = Links.objects.filter(
                url_curta = url_curta).first()
            url_curta = filtered_link.url_original
        except Links.DoesNotExist:
            context = {
                'detail': f'A URL {url_curta} não foi encontrada ou ainda não foi encurtada.'
            }
            return Response(context)

        return HttpResponseRedirect(redirect_to=url_curta)
    
  