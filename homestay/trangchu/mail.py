import random
import string
class Mail_Verify():
    # Khời tạo session để lưu code
    def __init__(self, request):
        self.session = request.session
        mail_verify = self.session.get('verify_key')
        if 'verify_key' not in request.session:
            mail_verify= self.session['verify_key']={}
        self.mail_verify = mail_verify
    #Tạo random code
    def create_code(self ):
        digits = string.digits
        return ''.join(random.choice(digits) for i in range(6))
    #lưu code vào session
    def save_code(self, Code, CustomerName, CustomerMail, CustomerPhone):
        self.mail_verify['verify_key'] = {
            'Code' : Code,
            'CustomerName': CustomerName,
            'CustomerMail': CustomerMail,
            'CustomerPhone': CustomerPhone,
        }   
        # lưu thay đổi vào session
        self.session.modified = True
    #lấy giá trị trong session
    def get_saved_code(self):
        return self.mail_verify.get('verify_key', {})

    def delete_session(self):
        del self.mail_verify