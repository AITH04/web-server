from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Web
from .forms import WebForm
import json
# Create your views here.
# def index(request):
    # if 'email' in request.GET and request.GET['email'] != '' and 'gender' in request.GET and request.GET['gender'] != '' \
    #         and 'subject' in request.GET and request.GET['subject'] != '' \
    #         and 'interested_things' in request.GET and request.GET['interested_things'] != '':
    #     return HttpResponse('Welcome!~' + request.GET['email'] + '想送禮物給' + request.GET['subject'] + '他喜歡' +
    #                         request.GET['interested_things'] )
    # else:
    #     return render(request, "index.html")
def index(request):
    return render(request, "index.html")

def showtemplate(request):
    web_list = Web.objects.all() # 把所有 Vendor 的資料取出來
    context = {'web_list': web_list} # 建立 Dict對應到Vendor的資料，
    return render(request, "welcome.html", context)

def web_create_view(request):
    form = WebForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        form = WebForm()
    context = {
        'form' : form
    }
    return render(request, "welcome.html", context)
# def singleWeb(request,id):
#     web_list = Web.objects.get(id=id) # 把所有 Vendor 的資料取出來
#     context = {'web_list': web_list} # 建立 Dict對應到Vendor的資料，
#     return render(request, 'welcome.html', context)

def message(request):
    Web.objects.all()
    return render(request, "message.html")

def product(request):
    return render(request, "product.html")




