'''yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in yangi_cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.capitalize())
'''
"""
yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in yangi_cars:
    if car != 'gm':
        print(car.capitalize())
    else:
        print(car.upper())
"""
'''
username=input("Login:  ")
if username.lower()=="admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz,  {username.capitalize()}")
'''
"""
son_1=float(input("Birinchi sonni kiriting:  "))
son_2=int(input("Ikkinchi sonni kiriting:  "))
if  son_1==son_2:
    print('Sonlar "teng" ekan')
"""
'''
a=float(input("Istalgan son kiriting:  "))
print("Siz kiritgan musbat!") if a>0 else print("Siz kiritgan son manfiy!")
'''

b=float(input("Istalgan son kiriting:  "))
print(f"Siz kiritgan sonning ildizi:  {b**(1/2)} ga teng") if b>0 else print("Siz kiritgan son manfiy. Iltimos musbat son kiriting")


