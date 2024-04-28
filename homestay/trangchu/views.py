from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .cart import Cart

# Create your views here.
def home(request):
    phongs = Phong.objects.order_by('Ten')
    context = {'phongs' :phongs}
    return render(request,'trangchu/home.html', context)
def cart(request):
    cart =Cart(request)
    cart_items =cart.get_cart_items()
    selected_option = cart.get_giaphong()
    selected_text = cart.get_selecttext()
    # trả về select giá phòng theo ca đã chọn
    context = {'cart_items': cart_items, 'selected_option': selected_option, 'selected_text': selected_text}
    return render(request,'trangchu/cart.html', context)
def cart_add(request):
    #lay cart
    cart = Cart(request)
    #test POST
    if request.POST.get('action') == 'post':
        phong_id = int(request.POST.get('phong_id'))
        #get selected value ở data của js
        selected_option= int(request.POST.get('selected_option'))
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
        selected_option= str(request.POST.get('selected_option'))
        #get selected text
        selectedtext = request.POST.get('selectedtext')
        #tim  san pham theo id
        cart.update_select(phong_id=phong_id, selected_option=selected_option,selectedtext=selectedtext )
        response = JsonResponse({'select': selected_option, 'selecttext': selectedtext  })
        return response
        #return redirect('cart')
def xemphong(request,id):
    phong = get_object_or_404(Phong, id=id)
    context = {'phong':phong}
    return render(request,'trangchu/xemchitietphong.html', context)
def blog(request):
    return render(request, 'trangchu/blog.html')
