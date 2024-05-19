from pickletools import read_uint1
from pydoc import pager
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from .models import *
#session cart
from .cart import Cart
#session mail_verify
from .mail import Mail_Verify
import random
from datetime import timedelta, datetime
import pytz
from django.db.models import Q
# api
from rest_framework.response import Response
from rest_framework.views import APIView
import math
from .serializer import *
# send mail
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def convert_to_gmt7(utc_datetime):
    # Xác định timezone cho UTC và GMT+7
    utc_tz = pytz.timezone('UTC')
    gmt7_tz = pytz.timezone('Asia/Ho_Chi_Minh')  # GMT+7
    # Chuyển đổi thời gian từ UTC sang GMT+7
    gmt7_datetime = utc_datetime.replace(tzinfo=utc_tz).astimezone(gmt7_tz)
    return gmt7_datetime
def home(request):
    
    if request.method == "POST":
        filtervalue = request.POST.get('addressfilter', None)
        pricesort = request.POST.get('pricesort', None)
        checkin = request.POST.get('check_in_iso', None)
        checkout = request.POST.get('check_out_iso', None)
        if checkin:
            checkin_format = checkin
        
        else:
            checkin_format = None

        if checkout:
            
            checkout_format = checkout
            
        else:
            checkout = None
        if not checkin_format or not checkout_format:
            # Nếu một trong hai trường không được nhập, hiển thị thông báo và không thực hiện gì cả
            roomfilter = Phong.objects.all()
            context = {'roomfilter': roomfilter}
            return render(request,'trangchu/home.html', context)
        else:
     
            roomfilter = Phong.objects.all()
            if filtervalue =="Tất cả khu vực":
                roomfilter = Phong.objects.all()
            elif filtervalue:
                roomfilter = Phong.objects.filter(Diachi__icontains=filtervalue)
            if pricesort == 'Gia4tieng':
                roomfilter = roomfilter.order_by('Gia4tieng')
            if pricesort == '-Gia4tieng':
                roomfilter = roomfilter.order_by('-Gia4tieng')
                
            if checkin and checkout:
               
                conflicting_orders = Order_item.objects.filter(
                    Q(checkin__lte=checkin_format, checkout__gte=checkin_format) |
                    Q(checkin__lte=checkout_format, checkout__gte=checkout_format) |
                    Q(checkin__gte=checkin_format, checkout__lte=checkout_format)
                ).values_list('phong__id', flat=True)

                # Loại bỏ các phòng đã được đặt khỏi danh sách tất cả các phòng
                roomfilter = roomfilter.exclude(id__in=conflicting_orders)
             
            context = {'roomfilter': roomfilter, 'filtervalue':filtervalue, 'checkin': checkin,'checkout': checkout}        
            return render(request,'trangchu/home.html', context)
    else:
        roomfilter = Phong.objects.order_by('id')
        context = {'roomfilter' :roomfilter}
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
    sum = cart.sum_gia()
    
    context = {'cart_items': cart_items,'sum':sum}
    return render(request,'trangchu/cart.html', context)
def checkout(request, phong_id):
    
    mail_verify = Mail_Verify(request)
    # tạo code random
   
    # lấy giỏ hàng trong session
    cart =Cart(request)
    # lấy giỏ hàng theo phong_id
    cart_items =cart.get_objects_by_id(phong_id)
    # trả về select giá phòng theo ca đã chọn
    context = {'item_by_id': cart_items,'sum':sum}
    return render(request, 'trangchu/checkout.html', context)
def verify(request, id):
    mail_verify = Mail_Verify(request)
    if request.method == "POST":
        customer_name = request.POST.get('customername')
        customer_mail = request.POST.get('customermail')
        customer_phone = request.POST.get('customerphone')
         #lấy email khách hàng
        Code = mail_verify.create_code()
        mail_verify.save_code(Code=Code,CustomerName=customer_name, CustomerMail=customer_mail, CustomerPhone=customer_phone )
        # Lấy data lưu trong session
        StoredData = mail_verify.get_saved_code()
        #Lấy code
        code = StoredData.get('Code')
        # gửi code về mail khách hàng mail
        email_from = settings.DEFAULT_FROM_EMAIL
        message = f'Lalendi Studio\nMã xác thực: {code}'
        send_mail('Lalendi', message, email_from, [customer_mail])
        context ={'phong_id':id}
        return render(request, 'trangchu/verify.html',context )
    else:
        messages.success(request, "Từ trồi truy cập")
        return redirect('home')  
def billinginfo(request, id):
    if request.method == "POST":
        code_customer_input = request.POST.get('code_input')
        mail_verify = Mail_Verify(request)
        StoredData = mail_verify.get_saved_code()
        customer_name = StoredData.get('CustomerName')
        customer_mail = StoredData.get('CustomerMail')
        customer_phone = StoredData.get('CustomerPhone')
        code_stored = StoredData.get('Code')
        print("Code from customer:", code_customer_input)
        print("Stored data:", code_stored)
        # In ra nội dung của session để kiểm tra
        if  code_stored == code_customer_input:
            # xoá session
            mail_verify.delete_session()
            cart =Cart(request)
            cart_items =cart.get_objects_by_id(id)
            # lấy thông tin khách hàng
           
            # lưu vào cơ sở dữ liệu
            # Tạo các đối tượng thời gian với thông tin múi giờ
            #email      
            for item in cart_items:
                phong_id= item['phong_id']
                checkin = item['checkin']
                checkout = item['checkout']
                sumprice = item['sumprice']
                
            room_available = Order_item.objects.filter(
                    phong_id=phong_id
                ).filter(
                    Q(checkin__lt=checkout) & Q(checkout__gt=checkin)
                ).exists()
           
            if not room_available:
                customer_info.objects.create(name=customer_name, email=customer_mail, number=customer_phone) #bảng thông tin người dùng
                order = Order.objects.create(full_name=customer_name, email=customer_mail, number=customer_phone)
                order.save()
                Order_id = order.pk
                create_order_item = Order_item.objects.create(order_id=Order_id, phong_id=phong_id, checkin=checkin, checkout=checkout, price=sumprice)
                create_order_item.save()
                # trả về select giá phòng theo ca đã chọn
                context = {'cart_items': cart_items,'sum':sum, 'name':customer_name, 'mail':customer_mail, 'phone': customer_phone}
                return render(request, 'trangchu/billing_info.html', context)
            else:
                messages.error(request, "Phòng không còn trống trong khoảng thời gian đã đặt")
                return redirect('cart')
        else:
            messages.error(request, "Mã xác thực không hợp lệ.")
            return redirect('verify', id=id)
    else:
        messages.success(request, "Từ trồi truy cập")
        return redirect('home')       
def cart_add(request):
    #lay cart
    cart = Cart(request)
    #test POST
    if request.POST.get('action') == 'post':
        phong_id = int(request.POST.get('phong_id'))
        #tim  san pham theo id
        phong = get_object_or_404(Phong,id=phong_id)
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        checkindisplay = request.POST.get('checkindisplay')
        checkoutdisplay = request.POST.get('checkoutdisplay')
        price = request.POST.get('price')
        lenday = request.POST.get('lenday')
        sumprice = request.POST.get('sumprice')
        #save vao session
        cart.add(phong=phong, checkin=checkin, checkout=checkout, price=price, lenday=lenday, sumprice=sumprice, checkindisplay=checkindisplay,checkoutdisplay=checkoutdisplay)
        
        # return response
        #response = JsonResponse({'Tên phòng ': phong.Ten })
        #get cart quantity
        cart_quantity= cart.__len__()
        response = JsonResponse({'qty': cart_quantity,'checkin': checkin})
        messages.success(request,("Đã thêm vào giỏ hàng"))   
        return response
def cart_select_update(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        phong_id = int(request.POST.get('phong_id'))
        #get selected value ở data của js
        checkin = str(request.POST.get('check_in'))
        checkout = str(request.POST.get('check_out'))
        #tim  san pham theo id
        cart.update_select(phong_id=phong_id, checkin=checkin,checkout=checkout )
        response = JsonResponse({'checkin': checkin, 'checkout': checkout  })
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
def get_dates_between(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    return dates

def xemphong(request,id):
    dates=[]
    phong = get_object_or_404(Phong, id=id)
    order_item_by_phong= Order_item.objects.filter(phong=phong)
    for item in order_item_by_phong:
        checkin_gmt7 = item.checkin
        checkout_gmt7 = item.checkout
        checkin = convert_to_gmt7(checkin_gmt7)
        checkout = convert_to_gmt7(checkout_gmt7)
        dates_between = get_dates_between(checkin, checkout)
        dates.extend(dates_between)
    dates_str = [date.strftime('%d-%m-%Y') for date in dates]
    
    context = {'phong':phong,'dates':dates_str,}
    return render(request,'trangchu/xemchitietphong.html', context)
def blog(request):
    return render(request, 'trangchu/blog.html')
def PreviewUpdate(request):
    if request.POST.get('action') == 'post':
        len = int(request.POST.get('lengthInDays'))
        gia = int(request.POST.get('price'))
        checkin =  request.POST.get('checkin')
        checkout =  request.POST.get('checkout')
        
        sum = len*gia
        response = JsonResponse({'sum': sum, 'len':len, 'checkin': checkin, 'checkout': checkout,})
        return response
def Home_Update_Search(request):
    if request.POST.get('action') == 'post':

        checkin =  request.POST.get('checkin')
        checkout =  request.POST.get('checkout')

        response = JsonResponse({'checkin': checkin, 'checkout': checkout,})
        return response

