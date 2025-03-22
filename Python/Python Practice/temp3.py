"""
def can_partition(stones):
    total_sum = sum(stones)
    
    # If the total sum is odd, we can't split it into two equal parts
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2    # 5
    n = len(stones)

    # Create a DP array to track possible sums
    dp = [False] * (target + 1)      # 5+1 =6
    dp[0] = True

    # Iterate over each stone and update the DP array
    for stone in stones:
        for j in range(target, stone - 1, -1):
            dp[j] = dp[j] or dp[j - stone]

    return dp[target]

# Taking input from the user
n = int(input("Enter the number of stones: "))
stones = [int(input(f"Enter weight of stone {i + 1}: ")) for i in range(n)]

print(can_partition(stones))



class Vehicle:
    wheels = 4  # Class attribute

    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels  # Modifying class attribute

# Accessing class attribute
print(Vehicle.wheels)  # Output: 4

# Changing class attribute using cls
Vehicle.change_wheels(6)
print(Vehicle.wheels)  # Output: 6



class Employee:
    company = "TechCorp"

    def __init__(self,name):
        self.name = name
    @classmethod
    def set_company(cls, new_company):
        cls.company = new_company
    
    def is_adult(age):
        if age>=18:
            return True
        else:
            return False
class Manager(Employee):
    def __init__(self, name,department):
        self.department = department
        super().__init__(name)
    def print_details(self):
        print("Manager name = ", self.name," Manager Department = ", self.department)

m1=Manager("Alice", "HR")

Manager.print_details(m1)


print(m1.name)
print(m1.department)
print(m1.company)

Manager.set_company("InnoTech")

print(m1.company) 

print(Manager.is_adult(20))
print(Manager.is_adult(15))


class Vehicle:
    vehicle_type = "General"

    def __init__(self, brand):
        self.brand = brand
    
    @classmethod
    def set_vehicle_type(cls, new_type):
        cls.vehicle_type = new_type
    
    @staticmethod
    def is_motorized(engine_type):
        return engine_type == "petrol" or "diesel"

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)      
print(car1.model)     
print(car1.vehicle_type)

Car.set_vehicle_type("Four-Wheeler")
print(car1.vehicle_type)

print(Car.is_motorized("petrol")) 
print(Car.is_motorized("electric")) 



class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def new_company(cls, new_company):
        cls.company = new_company
    
    @staticmethod
    def check_salary(salary):
        return salary >= 50000
    
    def display_details(self):
        print("Name : ", self.name," Salary : ", self.salary)

    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display_details(self):
        super().display_details()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def knows_language(self, lang):
        return lang == self.programming_language
    

m1 = Manager("Alice", 70000, "HR")
d1 = Developer("Bob", 60000, "Python")

m1.display_details()
d1.display_details()

Employee.new_company("InnoTech")
print(m1.company)
print(d1.company)

print(Employee.check_salary(m1.salary))
print(Employee.check_salary(d1.salary))

print(d1.knows_language("Java"))
print(d1.knows_language("Python"))



class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def new_company(cls, new_company):
        cls.company = new_company
    
    @staticmethod
    def check_salary(salary):
        return salary >= 50000
    
    def display_details(self):
        print("Name : ", self.name," Salary : ", self.salary)

    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def display_details(self):
        super().display_details()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def knows_language(self, lang):
        return lang == self.programming_language
    

m1 = Manager("Alice", 70000, "HR")
d1 = Developer("Bob", 60000, "Python")

m1.display_details()
d1.display_details()


"""


class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def new_company(cls, new_company):
        cls.company = new_company
    
    def display_details(self):
        print("Name : ", self.name," Salary : ", self.salary," Company:",self.company)

# CV IM
# IV CM

m1 = Employee("Alice", 70000)

m1.display_details()
