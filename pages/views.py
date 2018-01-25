from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import NewsInfo
from .forms import ContactForm

# Create your views here.
def home_page(request):
    news_list = NewsInfo.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(news_list, 2)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    return render(request, 'pages/home.html', {'news':news})

def about_page(request):
    context = {}
    return render(request, 'pages/about.html', context)

def contact_page(request):
    form = ContactForm()
    context = {'form':form}
    return render(request, 'pages/contact.html', context)

def login_page(request):
    return render(request, '', context)
