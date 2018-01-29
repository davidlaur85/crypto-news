from django.conf.urls import url
from .views import home_page, about_page, contact_page, login_page, register_page, submit_page

urlpatterns = [
    url( r"^$", home_page, name = "home_page" ),
    url( r"^about/$", about_page, name = "about_page" ),
    url( r"^contact/$", contact_page, name = "contact_page" ),
    url( r"^login/$", login_page, name = "login_page" ),
    url( r"^register/$", register_page, name = "register_page" ),
    url( r"^submit/$", submit_page, name = "submit_page" ),
]
