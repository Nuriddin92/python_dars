
# #1
# son=int(input("Biror juft son kiriting:   "))
# if son%2==0:
#     print('Rahmat')
# else:
#     print("Bu juft son emas")

# #2
# yosh=int(input("Yoshingizni kiriting:\n>>>"))
# if yosh<=4 or yosh>=60:
#     print("Sizga chipta bepul!")
# elif yosh<=18:
#     print("Sizga chipta narxi 10000 so`m!")
# else:
#     print("Sizga chipta narxi 20000 so`m!")

# #3
# print("Istalgan ikkita sonni kiriting!")
# a=int(input("Birinchi sonni kiriting:\n>>>"))
# b=int(input("Ikkinchi sonni kiriting:\n>>>"))
# if a>b:
#     print("Birinchi son katta")
# elif a==b:
#     print("Ikkala son teng")
# else:
#     print("Ikkinchi son katta")

# #4
# mahsulotlar=['limon','mandarin','olma','anor','uzum','tarvuz','non','banan','qovun','nok','apelsin','kivi']
# print("Do`konimizga xush kelibsiz!")
# savat=[]
# for i in range(5):
#     savat.append(input('Mahsulot nomini yozing:\n>>>'))
# # print(savat)
# for m in savat:
#     if m.lower() in mahsulotlar:
#         print(f"{m.title()}   Mahsulot do`konimizda bor")
#     else:
#         print(f"{m.title()}   Mahsulot do`konimizda yo`q")
            
# #5
# mahsulotlar1=['limon','mandarin','olma','anor','uzum','tarvuz','non','banan','qovun','nok','apelsin','kivi']
# print("Do`konimizga xush kelibsiz!")
# bor_mahsulotlar=[]
# yoq_mahsulotlar=[]
# print("5 ta mahsulot nomini kiriting")
# for f in range(5):
#     mahsul=(input('Mahsulot nomini yozing:\n>>>'))
#     if mahsul.lower() in mahsulotlar1:
#         bor_mahsulotlar.append(mahsul)
#     else:
#         yoq_mahsulotlar.append(mahsul)

# if len(bor_mahsulotlar)==0:
#     print("Afsuski ushbu mahsulotlarning hech biri do`konimizda yo`q!")
# elif len(bor_mahsulotlar)!=0 and len(yoq_mahsulotlar)!=0:
#     print(f"Quyidagi mahsulotlar do`konimzda yo`q:\n{yoq_mahsulotlar}")
# else:
#     print("Siz so`ragan barcha mahsulotlar do`konimizda bor!")

# #6
# foydalanuvchilar=['nuriddin','azizbek','asilbek','nodirbek','muhammadyusuf','izzatulloh','fayzulloh','hojiakbar','abdulloh','asadulloh','nurmuhammad']
# bor=True
# while bor==True:
#     user=input("Yangi login tanlang:\n>>>")
#     if user.lower() in foydalanuvchilar:
#         print("kechirasiz ushbu login band!")
#         bor=True
#     else:
#         print(f"Xush kelibsiz {user.title()}!")
#         bor=False

#6
son1=int(input("Butun son kiriting:\n>>>"))
for m in range(2,11):
    if son1%m==0:
        print(f"{son1} soni {m} ga qoldiqsiz bo`linadi!")
         













