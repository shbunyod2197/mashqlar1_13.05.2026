# 1
class Student:
    school_name = "Najot Ta'lim"
    country = "Uzbekistan"

    def __init__(self, fullname, age, course, grade):
        self.fullname = fullname
        self.age = age
        self.course = course
        self.grade = grade

    def show_info(self):
        print("Full name:", self.fullname)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Grade:", self.grade)

    def show_grade(self, new_grade):
        print(f"{self.fullname} bahosi o'zgardi: {self.grade} -> {new_grade}")
        self.grade = new_grade


s1 = Student("Azamat", 21, "Backend", "B")
s2 = Student("Ali", 19, "Frontend", "C")
s3 = Student("Vali", 22, "Design", "A")



s1.show_info()
s2.show_info()
s3.show_info()


s1.show_info()
s2.show_info()



# 2
class Car:
    wheels = 4
    country = "Germany"

    def __init__(self, brand, color, price, speed):
        self.brand = brand
        self.color = color
        self.price = price
        self.speed = speed

    def show_car(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Price:", self.price)
        print("Speed:", self.speed)

    def change_color(self, new_color):
        print(f"{self.brand} rangi o'zgardi: {self.color} -> {new_color}")
        self.color = new_color

    def increase_speed(self, km):
        self.speed += km
        print(f"{self.brand} tezligi oshdi: {self.speed}")


c1 = Car("BMW", "black", 50000, 200)
c2 = Car("Mercedes", "white", 80000, 220)

c1.show_car()
c2.show_car()

c1.change_color("red")
c1.increase_speed(50)
c2.change_color("blue")

c1.show_car()
c2.show_car()


# 3
class Phone:
    factory = "China"
    charger_type = "Type-C"

    def __init__(self, brand, model, memory, price):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.price = price

    def show_phone(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Memory:", self.memory)
        print("Price:", self.price)

    def change_price(self, new_price):
        print(f"{self.brand} narxi o'zgardi: {self.price} -> {new_price}")
        self.price = new_price

    def upgrade_memory(self, new_memory):
        print(f"{self.brand} xotirasi o'zgardi: {self.memory} -> {new_memory}")
        self.memory = new_memory


p1 = Phone("Samsung", "S24", 128, 1200)
p2 = Phone("iPhone", "15", 256, 1500)
p3 = Phone("Xiaomi", "13", 128, 800)

p1.show_phone()
p2.show_phone()
p3.show_phone()

# 4
class Employee:
    company_name = "Google"
    work_time = "09:00 - 18:00"

    def __init__(self, fullname, salary, position, age):
        self.fullname = fullname
        self.salary = salary
        self.position = position
        self.age = age

    def show_employee(self):
        print("Full name:", self.fullname)
        print("Salary:", self.salary)
        print("Position:", self.position)
        print("Age:", self.age)

    def increase_salary(self, amount):
        self.salary += amount
        print(f"{self.fullname} maoshi oshdi: {self.salary}")

    def change_position(self, new_position):
        print(f"{self.fullname} lavozimi o'zgardi: {self.position} -> {new_position}")
        self.position = new_position


e1 = Employee("Azamat", 5000, "Junior", 22)

e1.show_employee()

e1.increase_salary(1000)
e1.change_position("Middle")

e1.show_employee()

# 5
class Animal:
    kingdom = "Animals"
    planet = "Earth"

    def __init__(self, name, color, weight, age):
        self.name = name
        self.color = color
        self.weight = weight
        self.age = age

    def show_animal(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Weight:", self.weight)
        print("Age:", self.age)

    def change_weight(self, new_weight):
        print(f"{self.name} vazni o'zgardi: {self.weight} -> {new_weight}")
        self.weight = new_weight


a1 = Animal("Sher", "sariq", 200, 5)
a2 = Animal("Fil", "kulrang", 5000, 20)
a3 = Animal("Tulki", "qizil", 10, 3)

a1.show_animal()
a2.show_animal()
a3.show_animal()

a1.change_weight(210)
a2.change_weight(5100)

a1.show_animal()
a2.show_animal()
a3.show_animal()


# 6
class Book:
    library_name = "Central Library"
    language = "English"

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def show_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)
        print("Price:", self.price)

    def change_price(self, new_price):
        print(f"{self.title} narxi o'zgardi: {self.price} -> {new_price}")
        self.price = new_price

    def add_pages(self, count):
        self.pages += count
        print(f"{self.title} sahifalari oshdi: {self.pages}")


b1 = Book("Python", "Guido", 300, 50)

b1.show_book()

b1.change_price(45)
b1.add_pages(50)

b1.show_book()


# 7
class BankCard:
    bank_name = "Anor Bank"
    currency = "UZS"

    def __init__(self, owner, balance, card_number, password):
        self.owner = owner
        self.balance = balance
        self.card_number = card_number
        self.password = password

    def show_card(self):
        print("Bank Name:", self.bank_name)
        print("Card Number:", self.card_number)
        print("Password:", self.password)
        print("balance:", self.balance)

    def add_balance(self ,amount):
        self.balance += amount

    def remove_balance(self ,amount):
        self.balance -= amount

a1 = BankCard("bunyod", 10000, 726432, "ajoyib11")
a1.show_card()
a1.add_balance(1100)
a1.remove_balance(100)
a1.show_card()

# 8
class Teacher:
    school = "School 12"
    country = "Uzbekistan"

    def __init__(self, fullname, subject, experience, salary):
        self.fullname = fullname
        self.subject = subject
        self.experience = experience
        self.salary = salary

    def show_teacher(self):
        print("Fullname:", self.fullname)
        print("Subject:", self.subject)
        print("Experience:", self.experience)
        print("Salary:", self.salary)

    def increase_salary(self, amount):
        self.salary += amount

    def change_subject(self, new_subject):
        self.subject = new_subject


a1 = Teacher("ali", "fizik", 2000, 500)
a1.show_teacher()
a1.increase_salary(1000)
a1.show_teacher()
a1.increase_salary(1000)
a1.show_teacher()

# 9
class LopTop:
    ram_type = "DDR5"
    os = "Windows 11"

    def __init__(self, brand, cpu, ram_size, storage):
        self.brand = brand
        self.cpu = cpu
        self.ram_size = ram_size
        self.storage = storage

    def show_loptop(self):
        print("Brand:", self.brand)
        print("CPU:", self.cpu)
        print("RAM Size:", self.ram_size)
        print("Storage:", self.storage)

    def upgrade_ram(self, n_ram):
        self.ram_size = n_ram

    def upgrade_storage(self, n_storage):
        self.ram_size = n_storage

a = LopTop("a", 44, 90, 1000)
a.show_loptop()
a.upgrade_ram(1000)
a.upgrade_storage(1000)
a.show_loptop()


# 10
class User:
    platform = "Telegram"
    country = "Uzbekistan"

    def __init__(self, username, phone, followers, bio):
        self.username = username
        self.phone = phone
        self.followers = followers
        self.bio = bio

    def show_user(self):
        print("Username:", self.username)
        print("Phone:", self.phone)
        print("Followers:", self.followers)
        print("Bio:", self.bio)

    def change_bio(self, n_bio):
        self.bio = n_bio

    def increase_followers(self, n_count):
        self.followers += n_count

a = User("bunyod", 9877777909, 6000, "jahdfjkhak")
a.show_user()
a.increase_followers(1000)
a.show_user()
a.change_bio("knksjhkk")
a.show_user()
