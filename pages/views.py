from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

from .models import NewsInfo
from .forms import ContactForm, LoginForm, RegisterForm, SubmitForm

# Create your views here.
def home_page(request):
    news_list = NewsInfo.objects.all()
    page = request.GET.get( "page", 1 )
    paginator = Paginator( news_list, 2 )
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page( 1 )
    except EmptyPage:
        news = paginator.page( paginator.num_pages )
    return render( request, "pages/home.html", { "news":news } )


def about_page(request):
    context = {}
    return render( request, "pages/about.html", context )


def contact_page(request):
    title = "Contact us"
    description = "If you have any questions please don't hesitate to contact us."
    form = ContactForm()
    button = "Submit"
    context = {
        "title": title,
        "description": description,
        "form": form,
        "button": button
    }
    return render( request, "pages/form.html", context )


def login_page(request):
    next_page = request.GET.get("next")
    title = "Login"
    description = "Login to your account"
    form = LoginForm(request.POST or None)
    button = "Login"
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username=username, password=password)
        login(request, user)
        if next_page:
            return redirect(next_page)
        return redirect("/")
    context = {
        "title": title,
        "description": description,
        "form": form,
        "button": button
    }
    return render( request, "pages/form.html", context )


def register_page(request):
    title = "Register"
    description = "Don't have an account yet? You can create an account in less than 1 minute."
    form = RegisterForm()
    button = "Register"
    context = {
        "title": title,
        "description": description,
        "form": form,
        "button": button
    }
    return render( request, "pages/form.html", context )


def logout_page(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/login/")
def submit_page(request):
    if request.method == "POST":
        form = SubmitForm(request.POST or None)
        if form.is_valid():
            news = NewsInfo()
            news.title = form.cleaned_data["title"]
            news.title_url = form.cleaned_data["url"]
            news.user = request.user
            website_name = str(news.title_url)
            to_remove = ["http://", "https://", "www."]
            for word in to_remove:
                if word in website_name:
                    website_name = website_name.replace(word, "")
            website_name = website_name.split("/")
            news.website_name = website_name[0]
            news.save()
            print(website_name[0])
            return redirect("/")

    else:
        title = "Submit news"
        description = "Do you have some interesting news from the world of cryptocurrency? Don't hesitate to share it with your community."
        form = SubmitForm()
        button = "Submit"
        context = {
            "title": title,
            "description": description,
            "form": form,
            "button": button
        }
        return render( request, "pages/form.html", context )
