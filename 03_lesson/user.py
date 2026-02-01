class User:
    def __init__(self, first_name, last_name):
        self.myname=first_name
        self.mylast_name=last_name
    def print_first_name(self):
        print("Имя",self.myname )
    def print_last_name(self):
        print("Фамилия", self.mylast_name)
    def print_full_name(self):
        print("Имя и фамилия",self.myname,self.mylast_name)
