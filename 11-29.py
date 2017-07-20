# class order:
#     brand = ''
#     amount = 0
#     orderdate = ''
#     deliverydate = ''
#
#     beer = order
#     beer.brand = 'Budlight'
#     beer.amount = 6
#
#
# class employee:
#     skills = ["hardworking", "smart"] #class attribute
#     title = 'clerk'
#     name = 'john'
#
#     print (employee.skills)
#     print (employee.title)
#
#     linda = employee
#     john = employee
#
#     linda.skills.append("presentable")
#     print(john.skills) #ur gonna see only presentable because in the last statement u updated
#
# #need instance attribute and will allow us to access class
#     #attributes we can update: list, dictionary--mutable attributes
#     #some attributes we cannot update: string or any variables, tuple--immutable attributes
# dir(employee)
#
# __init__() #will help us customize the class for each instance which we're using for.
#
# class Employee:
#     def__init__(self):
#         self.skills=[]
#         print (self.skills)
#     linda.


class employee1:  #defining the class
    staff = []

    def __init__(self, name):
        self.name = name
        self.skills=[]
        self.add_staff()

    def add_staff(self):
        self.staff.append(self.name)
        print ('{} is added to the list'.format(self.name))

    def add_skills (self, skill):
        self.skills.append(skill)

    def view_staff(self):
        print ("staff list")
        for i in self.staff:
            print(i)
    def view_skills(self):
        print ('skills of {}'.format(self.name))
        for skill in self.skills:
            print(skill)

            #lets say we have a script employee.py, import employee
       # e1 = employee.employee1 ('john)
         #e1.staff = [0] = 'George'
         #e1.addskill('smart')



