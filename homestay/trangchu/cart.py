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
    def add(self, phong, checkin, checkout, price, lenday, sumprice, checkindisplay,checkoutdisplay):
        phong_id = str(phong.id)
        
        if phong_id in self.cart:
            Cart.cart_delete(self, phong_id)
            if phong_id not in self.cart:
                self.cart[phong_id] = {
                'phong_id': phong.id,
                'Ten': phong.Ten,
                'checkin': checkin,
                'checkout': checkout,
                'checkindisplay': checkindisplay, 
                'checkoutdisplay': checkoutdisplay, 
                'price': price,
                'lenday': lenday,
                'sumprice': sumprice,                                       
                                  }
        else:
            self.cart[phong_id] = {
                'phong_id': phong.id,
                'Ten': phong.Ten,
                'checkin': checkin,
                'checkout': checkout,
                'checkindisplay': checkindisplay, 
                'checkoutdisplay': checkoutdisplay,  
                'price': price,
                'lenday': lenday,
                'sumprice': sumprice,                                       
                                  }
          
        self.session.modified = True
        #return cart length
    def get_objects_by_id(self, id):
        id_str = str(id)
        item_by_id = []

        if id_str in self.cart:
            item_data = self.cart[id_str]
            phong_id = item_data.get('phong_id')
            phong = Phong.objects.get(id=phong_id)
            checkin = item_data.get('checkin')
            checkout = item_data.get('checkout')
            checkindisplay =item_data.get('checkindisplay')
            checkoutdisplay =item_data.get('checkoutdisplay')
            price = item_data.get('price')
            lenday = item_data.get('lenday')
            sumprice = item_data.get('sumprice')

            cart_item = {
                'phong_id': phong_id,
                'phong': {
                    'id': phong.id,
                    'Ten': phong.Ten,
                    'Gia4tieng': phong.Gia4tieng,
                    'HinhanhURL': phong.HinhanhURL,
                },
                'checkin': checkin,
                'checkout': checkout,
                'checkindisplay': checkindisplay, 
                'checkoutdisplay': checkoutdisplay,
                'price': price,
                'lenday': lenday,
                'sumprice': sumprice,
            }
            item_by_id.append(cart_item)

        return item_by_id
        
    def __len__(self):
        return len(self.cart)
    def get_cart_items(self):
        
        cart_items = []
        for phong_id, item_data in self.cart.items():
            phong = Phong.objects.get(id=phong_id)
            phong_id = item_data.get('phong_id')
            checkin = item_data.get('checkin')
            checkout = item_data.get('checkout')
            checkindisplay = item_data.get('checkindisplay')
            checkoutdisplay = item_data.get('checkoutdisplay')
            price = item_data.get('price')
            lenday = item_data.get('lenday')
            sumprice =  item_data.get('sumprice')
            cart_item = {
                'phong_id': phong_id,
                'phong': phong,
                'checkin': checkin,
                'checkout': checkout,
                'checkindisplay': checkindisplay,
                'checkoutdisplay': checkoutdisplay,
                'price': price,
                'lenday': lenday,
                'sumprice': sumprice,
                
            }
            cart_items.append(cart_item)
        return cart_items

    def update_select(self, phong_id, checkin, checkout):
        phong_id = str(phong_id)
         
        selectedtext = selectedtext
        ourcart = self.cart
        ourcart[phong_id] = {
            'Ten': ourcart[phong_id]['Ten'],    
          
        }
        
        self.session.modified = True
    def sum_gia(self):
        sum=0
        for item in self.cart.values():
            sum += int(item['sumprice'])
        return sum 
    def cart_delete(self, phongid):  
        phong_id = str(phongid) 
        if phong_id in self.cart:
            del self.cart[phong_id]
            self.session.modified = True


     
        




