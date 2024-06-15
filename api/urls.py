# URLS
from django.urls import path
from django.shortcuts import redirect

# STATIC
from django.conf import settings
from django.conf.urls.static import static

# PAGES
from pages.views import Home


urlpatterns = [
  path('home/', Home.as_view(), name='home-view'),
]

urlpatterns += [path('', lambda request: redirect('home-view'))]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
