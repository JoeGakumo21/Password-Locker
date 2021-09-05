class User:
    '''
    class that generate new instance of users
    '''
    user_list=[] #empty userdetails list

    
    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties for our object
        '''
        self.username=username
        self.password=password

    # def  full_details_user(self):
    #     obj=Credentians()
    #     data= obj.Credentians()
    def save_user(self):
        '''
        save userdetails method into users password lock
        '''
        User.user_list.append(self)
        