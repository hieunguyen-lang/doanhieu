from .cart import Cart
from.mail import Mail_Verify
# để cho cart có thể hoạt động ở mọi page
def cart(request):
    # trả về dữ liệu của Cart
    return {'cart': Cart(request)}
def mail_verify(request):
    # trả về dữ liệu của Cart
    return{'mail_verify': Mail_Verify(request)}