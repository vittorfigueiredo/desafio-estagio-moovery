from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('links/', views.LinksView.as_view(), name='links'),
    path('shortner/', views.ShortnerApiView.as_view(), name='shortner'),
    path('<path:url_curta>/', views.RedirectView.as_view(), name='redirect'),
]
