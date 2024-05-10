from pickletools import read_uint1
from pydoc import pager
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .cart import Cart
from django.db.models import Q
# api
from rest_framework.response import Response
from rest_framework.views import APIView
import math
from .serializer import *

# Create your views here.
def home(request):
    
    if request.method == "POST":
        filtervalue = request.POST.get('addressfilter', None)
        pricesort = request.POST.get('pricesort', None)
        roomfilter = Phong.objects.all()
        if filtervalue:
            roomfilter = Phong.objects.filter(Diachi__icontains=filtervalue)
        if pricesort == 'Gia4tieng':
            roomfilter = roomfilter.order_by('Gia4tieng')
        elif pricesort == '-Gia4tieng':
            roomfilter = roomfilter.order_by('-Gia4tieng')
        context = {'roomfilter': roomfilter, 'filtervalue':filtervalue}        
        return render(request,'trangchu/home.html', context)
    else:
        phongs = Phong.objects.order_by('id')
        context = {'phongs' :phongs}
        return render(request,'trangchu/home.html', context)
#api 
def search(request):
    return render(request, "trangchu/search.html", {})
class roomapiview(APIView):

     def get(self,request):
        s = request.GET.get('s')
        
        sort = request.GET.get('sort')
        rooms = Phong.objects.all()

        if s:
            rooms = Phong.objects.filter(Q(Diachi__icontains=s) | Q(id__icontains=s)) 
        
        if sort =='asc':
            rooms = Phong.objects.order_by('Gia4tieng')
        elif sort == 'desc':
            rooms = Phong.objects.order_by('-Gia4tieng')
        

        total = rooms.count()
        serializer = RoomSerializer(rooms, many=True)
        return Response( {
            'data':serializer.data,
            'Tổng': total
        })

class roomid(APIView):
    def get(self, request):
        id = request.GET.get('id')
        if id:
            rooms = Phong.objects.filter(id=id) 

        serializer  =RoomidSerializer(rooms, many=True)
        return Response(serializer.data)
        
def cart(request):
    cart =Cart(request)
    cart_items =cart.get_cart_items()
    selected_option = cart.get_giaphong()
    selected_text = cart.get_selecttext()
    sum = cart.sum_gia()
    # trả về select giá phòng theo ca đã chọn
    context = {'cart_items': cart_items, 'selected_option': selected_option, 'selected_text': selected_text, 'sum':sum}
    return render(request,'trangchu/cart.html', context)
def checkout(request):
    return render(request,'trangchu/checkout.html' )
def cart_add(request):
    #lay cart
    cart = Cart(request)
    #test POST
    if request.POST.get('action') == 'post':
        phong_id = int(request.POST.get('phong_id'))
        #get selected value ở data của js
        selected_option= request.POST.get('selected_option')
        #get selected text
        selectedtext = request.POST.get('selectedtext')
        #tim  san pham theo id
        phong = get_object_or_404(Phong,id=phong_id)
        
        #save vao session
        cart.add(phong=phong,selected_option=selected_option, selectedtext=selectedtext)
        
        # return response
       # response = JsonResponse({'Tên phòng ': phong.Ten })
        #get cart quantity
        cart_quantity= cart.__len__()
        response = JsonResponse({'qty': cart_quantity, 'select': selected_option, 'selecttext': selectedtext})
        
        return response 
def cart_select_update(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        phong_id = int(request.POST.get('phong_id'))
        #get selected value ở data của js
        selected_option= request.POST.get('selected_option')
        #get selected text
        selectedtext = request.POST.get('selected_text')
        #tim  san pham theo id
        cart.update_select(phong_id=phong_id, selected_option=selected_option,selectedtext=selectedtext )
        response = JsonResponse({'select': selected_option, 'selecttext': selectedtext  })
        return response
        #return render(request,'trangchu/cart.html')
def cart_delete(request):
    cart=Cart(request)
    #lay phòng id
    if request.POST.get('action') == 'post':
        phong_id = int(request.POST.get('phong_id'))
        cart.cart_delete(phongid=phong_id)
        response =JsonResponse({'id': phong_id})
        return response
def xemphong(request,id):
    phong = get_object_or_404(Phong, id=id)
    context = {'phong':phong}
    return render(request,'trangchu/xemchitietphong.html', context)
def blog(request):
    return render(request, 'trangchu/blog.html')
