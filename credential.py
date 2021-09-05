class Credentians:
    '''
    this class generate new instances of credentials to class user
    '''
    def __init__(self, account,fullname,phonenumber,email ):
        '''
        method that help populate the user  created
        '''
        self.account=account
        self.fullname=fullname
        self.phonenumber=phonenumber
        self.email=email