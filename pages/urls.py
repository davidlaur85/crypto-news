from django.conf.urls import url
from .views import home_page, about_page, contact_page

urlpatterns = [
    url(r'^$', home_page, name='home_page'),
    url(r'^about/$', about_page, name='about_page'),
    url(r'^contact/$', contact_page, name='contact_page'),
]
