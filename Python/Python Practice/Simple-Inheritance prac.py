"""
class EC2Manager:
    def __init__(self, instance_id):
        self.instance_id = instance_id

    def start_instance(self):
        print(f"Starting EC2 instance: {self.instance_id}")

    def stop_instance(self):
        print(f"Stopping EC2 instance: {self.instance_id}")

class AutoScalingManager(EC2Manager):
    def __init__(self, instance_id, min_instances, max_instances):
        super().__init__(instance_id)
        self.min_instances = min_instances
        self.max_instances = max_instances

    def scale_up(self):
        print(f"Scaling up instances... Max allowed: {self.max_instances}")

    def scale_down(self):
        print(f"Scaling down instances... Min allowed: {self.min_instances}")

# Usage
ec2 = AutoScalingManager("i-1234567890abcdef", min_instances=2, max_instances=10)
ec2.start_instance()
ec2.scale_up()
ec2.scale_down()
ec2.stop_instance()


import boto3

class EC2Manager:
    def __init__(self, instance_id, region="us-east-1"):
        self.instance_id = instance_id
        self.ec2_client = boto3.client("ec2", region_name=region)

    def start_instance(self):
        response = self.ec2_client.start_instances(InstanceIds=[self.instance_id])
        print(f"Starting EC2 instance: {self.instance_id}")
        return response

    def stop_instance(self):
        response = self.ec2_client.stop_instances(InstanceIds=[self.instance_id])
        print(f"Stopping EC2 instance: {self.instance_id}")
        return response

class AutoScalingManager(EC2Manager):
    def __init__(self, instance_id, min_instances, max_instances, region="us-east-1"):
        super().__init__(instance_id, region)
        self.min_instances = min_instances
        self.max_instances = max_instances

    def scale_up(self):
        print(f"Scaling up EC2 instances... Max allowed: {self.max_instances}")
        # In a real-world scenario, we'd launch new instances using `run_instances`

    def scale_down(self):
        print(f"Scaling down EC2 instances... Min allowed: {self.min_instances}")
        # Here, we'd terminate instances based on load

# Usage Example
instance_id = "i-1234567890abcdef"  # Replace with your actual EC2 instance ID
region = "us-east-1"  # Modify based on your AWS region

ec2 = AutoScalingManager(instance_id, min_instances=2, max_instances=5, region=region)

# Start and stop instance using Boto3
ec2.start_instance()
ec2.scale_up()
ec2.scale_down()
ec2.stop_instance()


class Employee:
    
    def __init__(self,emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee Id : ", self.emp_id)
        print("Employee Name : ", self.name)
        print("Employee Salary : ", self.salary)

class Developer(Employee):
    
    def __init__(self, emp_id, name, salary, program_lang):
        super().__init__(emp_id, name, salary)   # or Employee.__init__(self, emp_id, name, salary)
        self.program_lang = program_lang
    
    def show_dev_info(self):
        print("Employee Id : ", self.emp_id)
        print("Employee Name : ", self.name)
        print("Employee Salary : ", self.salary)
        print("Employee Programming Language : ", self.program_lang)

emp1 = Developer(1001, "Ravi Kumar", 60000, "Python")

emp1.show_dev_info()

class Bankaccount():

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, bal):
        self.balance = self.balance + bal
        print("Depositing ₹",bal,"...")
        print("New Balance: ₹",self.balance)

    def withdraw(self,bal):
        self.balance = self.balance - bal
        print("Withdrawing ₹",bal,"...")
        print("New Balance: ₹",self.balance)

    def display_balance(self):
        print("Available Balance = ",self.balance)

class Savingsaccount(Bankaccount):

    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)

    def add_interest(self, interest):
        new_bal = self.balance + (self.balance*interest)/100
        print("Adding Interest (",interest,")")
        print("New Balance after interest: ₹",new_bal)

ravi= Savingsaccount(1001, "Ravi", 1000)

ravi.deposit(200)

ravi.withdraw(200)

ravi.display_balance()

ravi.add_interest(5) 

class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print("Book Title: ", self.title)
        print("Author:", self.author)
        print("ISB:", self.isbn)
class Ebook(Book):

    def __init__(self, title, author, isbn,file_size, format):
        super().__init__(title, author, isbn)
        self.file_size = file_size
        self.format = format
    def display_ebook_info(self):
        self.display_info()
        print("File Size:", self.file_size)
        print("Format:", self.format)

ebook1 = Ebook("The Alchemist", "Paulo Coelho", "978-0061122415", 2.5, "PDF")
ebook1.display_ebook_info()


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print("Vehicle Information:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type, seating_capacity):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.seating_capacity = seating_capacity

    def display_car_info(self):
        self.display_info()
        print("Fuel Type:", self.fuel_type)
        print("Seating Capacity:", self.seating_capacity)
class Rentalcar(Car):
    def __init__(self, brand, model, year, fuel_type, seating_capacity, rental_price_per_day, is_available):
        super().__init__(brand, model, year, fuel_type, seating_capacity)
        self.rental_price_per_day = rental_price_per_day
        self.is_available = is_available

    def display_rental_info(self):
        self.display_car_info()
        print("Rental Price per Day: ₹", self.rental_price_per_day)
        print("Available:", "Yes" if self.is_available else "No")

    def rent_car(self,days):
        if self.is_available:
            print("Renting for", days,"days...")
            print("Total Price: ₹", self.rental_price_per_day*days,sep="")
        else:
            print("Not Available")

car1 = Rentalcar("Toyota", "Corolla", 2022, "Petrol", 5, 2000, True)
car1.display_rental_info()
car1.rent_car(3)
"""
