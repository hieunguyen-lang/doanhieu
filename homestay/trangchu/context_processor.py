from .cart import Cart
# để cho cart có thể hoạt động ở mọi page
def cart(request):
    # trả về dữ liệu của Cart
    return {'cart': Cart(request)}