class student: 
    school = "AMV"
    def __init__(self, id ,name , phone):
        self.id = id
        self.name = name
        self.phone = phone
        
    @staticmethod
    def check_phone(phone):
        return len(phone) >= 10
    def say_hello(self):
        print(f'Xin chao {self.name}')
        
        
student1 = student(1,"Nam", 292920910)
student1.say_hello()
