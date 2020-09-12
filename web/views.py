from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import *
from .forms import WebForm
import json
import requests
from random import randint

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

# def web_create_view(request):
#     form = WebForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         print(form.cleaned_data)
#         form = WebForm()
#     context = {
#         'form' : form
#     }
#     return render(request, "welcome.html", context)



# def createOrder(request):
# 	form = OrderForm()
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = OrderForm(request.POST)
# 		if form.is_valid():
# 			form_list = [{
# 				'receivername': Web.receivername,
# 				'email': Web.email,
# 				'gender': Web.gender,
# 				'receiverage': Web.receiveage,
# 				'relationship': Web.relationship
# 			}]
# 			form_list.save()
# 			return redirect('/')
#
# 	context = {'form':form}
# 	return render(request, 'welcome.html', context)

def post1(request):
	if request.method == "POST":#如果是以POST的方式才處理
		receivername = request.POST['receivername']    #取得表單輸入資料
		email = request.POST['email']
		gender = request.POST['gender']
		receiveage = request.POST['receiveage']
		relationship = request.POST['relationship']
		unit = Web.objects.create(receivername=receivername, email=email, gender=gender, receiveage=receiveage, relationship=relationship)
		unit.save() #寫入資料庫
		# response = requests.get("", json={'receivername':receivername, 'email':email, 'gender':gender, 'receiveage':receiveage, 'relationship':relationship})
		return render(request, 'message.html', )
	else:
		message = '請輸入資料(資料不作驗證)'
	return render(request, "welcome.html", locals())

def favorite(request):
	categorylist = ["音樂", '運動', '影劇', '旅遊', '購物', '閱讀', '電動', '美食']
	key = categorylist[randint(0,len(categorylist))] # 從前個網頁傳來的值
	if key == "音樂":
		para = {'category': key,
				'subcategory': ['古典音樂', '流行音樂', '電音', '嘻哈饒舌', '搖滾樂', '其他'],
				'open_question':['最喜歡的專輯:', '最喜歡的歌手:', '曾參加過的演唱會:']
				}
	elif key == "運動":
		para = {'category': key,
				'subcategory': ['田徑', '球類', '有氧', '無氧', '靜態休閒', '其他'],
				'open_question':['最喜歡的運動:', '最喜歡的運動明星:', '喜歡的運動品牌:']
				}
	elif key == "影劇":
		para = {'category': key,
				'subcategory': ['好萊塢大片', '日劇', '韓劇', '連續劇', '古裝劇', '其他'],
				'open_question':['最喜歡的影劇:', '最喜歡的好萊塢明星:', '喜歡的影劇風格:']
				}
	elif key == "旅遊":
		para = {'category': key,
				'subcategory': ['國內旅遊', '國外旅遊', '當天來回', '東南亞探險', '哈日韓族'],
				'open_question':['最喜歡的地方（國家/地名）:']
				}
	elif key == "購物":
		para = {'category': key,
				'subcategory': ['流行服飾', '家用實物', '精品名牌', '電子器具', '護膚保養', '其他'],
				'open_question':['逛街最常逛的東西:']
				}
	elif key == "閱讀":
		para = {'category': key,
				'subcategory': ['旅遊叢書', '文學小說', '商業理財', '語言學習', '心理勵志', '其他'],
				'open_question':['最喜歡的書籍？', '最喜歡的作者？']
				}
	elif key == "電動":
		para = {'category': key,
				'subcategory': ['手機遊戲', '線上遊戲', '掌上型機台(switch/nds等)', '其他'],
				'open_question':['最喜歡的遊戲類型？']
				}
	elif key == "美食":
		para = {'category': key,
				'subcategory': ['台式', '中式', '西式', '日式', '韓式', '其他'],
				'open_question': ['最喜歡的餐廳？', '最喜歡的食物？']
				}
	else:
		para = {'category': 'invalid category',
				'subcategory': ['Angela', 'Benton', 'Chin', 'Honda', 'Jason', 'Wendy'],
				'open_question': ['invalid category']
				}
	return render(request, "favorite.html",para)

def message(request):
    return render(request, "message.html")

def product(request):
	return render(request, "product.html")




