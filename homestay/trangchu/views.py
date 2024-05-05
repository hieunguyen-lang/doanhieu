from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .cart import Cart
from django.db.models import Q, Min
# api
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *

# Create your views here.
def home(request):
    phongs = Phong.objects.order_by('id')
    context = {'phongs' :phongs}
    return render(request,'trangchu/home.html', context)
#api 
class roomapiview(APIView):

     def get(self,request):
        s = request.GET.get('s')
        soft = request.GET.get('soft')
        rooms = Phong.objects.all()
        if s:
            rooms = Phong.objects.filter(Q(Diachi__icontains=s) & Q(Netflix__icontains=s)) 
        
        if soft =='min':
            rooms = rooms.annotate(min_gia=Min('banggias__Gia4tieng'))
            rooms = Phong.objects.order_by('banggias.Gia4tieng')
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
        

class roomdetailapi(APIView):
    def get(self, request ):
        s= request.GET.get('s')
        roomdetail = Phong.objects.all()
        if s:
            roomdetail = Phong.objects.filter(id__icontains=s)
            serializer = RoomDetailSerializer(roomdetail, many=True)
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
