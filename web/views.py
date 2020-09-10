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

    product_list = [	{
                            "goods_name": "360 Den 彈性褲襪 - 黑色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324230818.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2341.html?member=af000121893",
                            "goods_sale_price": "1600.00"
                        },
                        {
                            "goods_name": "420 Den 彈性褲襪 - 黑色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324230906.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2343.html?member=af000121893",
                            "goods_sale_price": "1920.00"
                        },
                        {

                            "goods_name": "140 Den 彈性褲襪 - 膚色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324230326.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2345.html?member=af000121893",
                            "goods_sale_price": "800.00"
                        },
                        {
                            "goods_name": "200 Den 彈性褲襪 - 膚色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現。\r\n◎可長時間使用，輕鬆達到按摩及運動效果。\r\n◎熱銷歐美市場，榮獲國際品質認證。",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324230637.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2347.html?member=af000121893",
                            "goods_sale_price": "1040.00"
                        },
                        {
                            "goods_name": "280 Den 彈性褲襪 - 膚色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324230729.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2349.html?member=af000121893",
                            "goods_sale_price": "1280.00"
                        },
                        {
                            "goods_name": "360 Den 彈性褲襪 - 膚色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324230753.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2351.html?member=af000121893",
                            "goods_sale_price": "1600.00"
                        },
                        {
                            "goods_name": "420 Den 彈性褲襪 - 膚色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324230931.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2353.html?member=af000121893",
                            "goods_sale_price": "1920.00"
                        },
                        {
                            "goods_name": "200 Den 彈性大腿襪 - 黑色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證\r\n",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324231124.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2359.html?member=af000121893",
                            "goods_sale_price": "1040.00"
                        },
                        {
                            "goods_name": "280 Den 彈性大腿襪 - 黑色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證\r\n",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324231222.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2361.html?member=af000121893",
                            "goods_sale_price": "1280.00"
                        },
                        {
                            "goods_name": "200 Den 彈性大腿襪 - 膚色(二雙入)",
                            "goods_slogan": "◎採用最新編織技術，質感立即顯現\r\n◎可長時間使用，輕鬆達到按摩及運動效果\r\n◎熱銷歐美市場，榮獲國際品質認證\r\n",
                            "goods_image": "http://img.oeya.com/website/upload/photos/201103/110324231104.jpg",
                            "goods_ad_site": "http://www.mymall.com.tw/pro-2363.html?member=af000121893",
                            "goods_sale_price": "1040.00"
                        }]

    return render(request, "product.html",{"productlist":product_list})




