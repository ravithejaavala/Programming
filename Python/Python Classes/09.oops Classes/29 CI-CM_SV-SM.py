# 22-03-025
'''

IV -- IM  --- self  -- Individual

CV -- CM -- cls  -- shareable & modifiable

Class Variable and Class Method:
-------------------------------
A variable that is shared by all the instance of a class. The class variables are defined
within a class but outside any of the class methods.
the class variables are not used as frequently as instance variable

**  the class variables are declared when a class is being constructed and they are not
defined inside of any method of a class..so the scope of the class variables are entire
class (we can able to access inside instance method and class method)

Note:
----
the implict(first parameter) of the class method is *cls*
while class method we need to call decorator (@classmethod)

'''

class Emp(object):

    office_location = 'blr' # class variable
    def _init_(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal
    def get_emp_details(self): # instance method
        print(self.name, self.age, self.sal)

    @classmethod
    def get_emp_off(cls): # classmethod
        print(cls.office_location)

ravi = Emp('ravi',29, 345643)
ravi.get_emp_details() # calling the instance method with the help of an object
ravi.get_emp_off()

hyma = Emp('hyma',24, 456789)
hyma.get_emp_details() # calling the instance method with the help of an object
hyma.get_emp_off()

# way of calling the attributes
print(ravi.office_location)
print(ravi.name)

print(Emp.office_location)
# print(Emp.name)

'''
IV IM
CV CM
SV SM


CV IM   --- 
IV CM   --- let me know as an example it it works

'''

# CV -- IM

class Student:

    schol_name = 'xyz' # class variable

    def _init_(self, name, roll, age):
        self.name = name
        self.roll = roll
        self.age = age

    def get_student(self):
        print(self.name, self.roll, self.age, self.schol_name)

bhanu = Student('bhanu',2345678, 23)
bhanu.get_student()


'''
static variables and static method:
---------------------------
All objects share class or static variables. An instance or non-static variables are
different for different objects(every object has a copy).

static variables are defined inside the class definition, but outside of any method
definitions. They are typically initialized with a value, just like an instance variable,
but they can be accessed and modified through the class itself, rather than through the
instance...


Advtanges:
-----
Memory efficiency: static variables are allocated memory once when the object for the 
class is created for the first time...

clss scope : The static variables are created outside methods but inside of the class



Note:
----
the static variables are defined inside the class definition
we need to use the @static method, while writing static method which is mandatory...

'''