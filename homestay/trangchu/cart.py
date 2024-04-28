from .models import *
class Cart():
    def __init__(self, request):
        self.session = request.session
        #lay session hien tai
        cart = self.session.get('session_key')
        #neu user la moi, thi tao session moi
        if 'session_key' not in request.session:
            cart= self.session['session_key']={}
        #make
        self.cart = cart
    def add(self, phong, selected_option, selectedtext):
        phong_id = str(phong.id)
        selected_option= int(selected_option)
        selectedtext = selectedtext
        if phong_id in self.cart:
            pass
        else:
            self.cart[phong_id] = {
                'Ten': phong.Ten,
                'Gia' : selected_option, 
                'Ca': selectedtext,                                            
                                  }
            # Lưu selected_option vào session
            
        self.session.modified = True
        #return cart length
    def __len__(self):
        return len(self.cart)
    def get_cart_items(self):
        
        phong_ids = self.cart.keys()
        phongs=Phong.objects.filter(id__in = phong_ids)

        return phongs
    def get_giaphong(self):
        selected_ops =self.cart
        return selected_ops
    def get_selecttext(self):
        selected_text =self.cart
        return selected_text
    def update_select(self, phong_id, selected_option, selectedtext):
        phong_id = str(phong_id)
        selectedoption = str(selected_option)
        selectedtext = selectedtext
        ourcart = self.cart
        ourcart[phong_id] = {
            'Ten': ourcart[phong_id]['Ten'],    
            'Gia' : selectedoption, 
            'Ca': selectedtext, 
        }
        
        self.session.modified = True
    


