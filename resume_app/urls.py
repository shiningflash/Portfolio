from django.urls import path
from . import views

from django.conf import settings, urls
from django.conf.urls.static import static

from django.conf.urls import url
from django.views.static import serve 

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)