# AMALIYOT
# #1 
# print("Otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan")
# otam={"ism":"Abduvohid", "familiya":"Axmadaliyev", "t_yil":"1958", "y_manzil":"do`rmon"}
# print(f'Otam {otam["ism"].title()} {otam["familiya"].title()} {otam["t_yil"]} yilda tug`ilgan. {otam["y_manzil"].capitalize()} da yashaydi')

# #2
# print(" Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh")
# taom={"Nuriddin":"osh", "Azizbek":"mastava", "Asilbek":"shashlik", "Muhammadyusuf":"makaron", "Nodirbek":"grechka"}
# print(f'Nuriddinning sevimli taomi {taom["Nuriddin"]}, \nAzizbekning sevimli taomi {taom["Azizbek"]}, \nAsilbekning sevimli taomi {taom["Asilbek"]}')

# #3 
# print("Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.")
# python_lugat={"float":"haqiqiy sonlar", "integer":"butun sonlar", "string":"matnli ma'lumotlar", "if":"\"agar\"  deb tarjima qilinadi. pythonda tarmoqlanish uchun ishlatiladi", "else":"\"aks holda\" deb tarjima qilinadi. Pythonda tarmoqlanish uchun ishlatiladi","list":"ro`yhatli ma'lumot turi hisoblanadi"}

# #4 
# print("Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, \"Bunda so'z mavjud emas\" degan xabarni chiqaring.")
# soz=python_lugat.get(input("Pythonga oid atama yozing:  "), "Bu atama lug`atda yo`q")
# print(soz)

# #5 
# print("Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.")
# soz1=input("Pythonga oid atama yozing:  ")
# if soz1 in python_lugat:
#     print(python_lugat[soz1])
# else:
#     print("Bu atama lug`atda yo`q")