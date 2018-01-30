from django.conf.urls import url
from .views import home_page, about_page, contact_page, login_page, logout_page, register_page, submit_page, user_news_page, source_news_page

urlpatterns = [
    url( r"^$", home_page, name = "home_page" ),
    url( r"^about/$", about_page, name = "about_page" ),
    url( r"^contact/$", contact_page, name = "contact_page" ),
    url( r"^filter-name/(?P<name>.+)/$", user_news_page, name = "user_news_page" ),
    url( r"^filter-source/(?P<source>.+)/$", source_news_page, name = "source_news_page" ),
    url( r"^login/$", login_page, name = "login_page" ),
    url( r"^logout/$", logout_page, name = "logout_page" ),
    url( r"^register/$", register_page, name = "register_page" ),
    url( r"^submit/$", submit_page, name = "submit_page" ),
]
