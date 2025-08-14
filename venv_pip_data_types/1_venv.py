#-----------------------------python sintaksi-----------------------------------------------------------
#vertual muhit
#harbir koding jarayni bosjhlahidan oldin venv yaraltlishi kerak
#2 hil versaydagi kutib honalarni 1 a qobiqa ushlab trish uchun
#vertual muhit yatatishni 2 hil usului bor bular
#cmd orqali kod yozish
#inteer prator orqali kod yozish
#python -m venv venv / py -m venv venv - shu 2 hil uslubda venv yartish mukun
#venv\Scripts\activate - venvni aktivatsay yarrtibersih
#pip --version -kutubhonani ersaysii aniqlash
#pip install --upgrade pip kutubhonalarni versalarni yangislsah
#pip uninstall kutubhonani ochsirsh
#pip list yuklnaga kutubhonlshni chiqarish
#pip show yani bir kutubhoni malumotini hiqaradi
#pip install -r requirements.txt - requasdagi ham kodlarni yuklanb oladi
#pip freeze > requirements.txt -request yaratadi
eski_matn = "Men olma yeyman."
yangi_matn = eski_matn.replace("olma", "anor")
print(yangi_matn)
# Matndagi biror so'zni boshqasiga almashtiradi
bo_sh_joyli_matn = "   Salom, dunyo!   "
toza_matn = bo_sh_joyli_matn.strip()
print(toza_matn)
# Matnning boshidagi va oxiridagi bo'sh joylarni olib tashlaydi
gap = "Bugun havo juda yaxshi"
so_zlar = gap.split(" ")
print(so_zlar)
# Matnni berilgan ajratuvchi bo'yicha qismlarga bo'lib, ro'yxat (list) qaytaradi
matn = "Python dasturlash tili."
boshlanadi = matn.startswith("Python")
print(boshlanadi)
# Matn berilgan so'z bilan boshlanadimi yoki yo'q, tekshiradi (True/False qaytaradi)
fayl_nomi = "hujjat.pdf"
tugaydi = fayl_nomi.endswith(".pdf")
print(tugaydi)
# Matn berilgan so'z bilan tugaydimi yoki yo'q, tekshiradi (True/False qaytaradi)
matn_qidirish = "Bu misolda biror so'z qidiramiz."
indeks = matn_qidirish.find("so'z")
print(indeks)
# Matn ichidan berilgan so'zni qidiradi va topilgan birinchi joyining indeksini qaytaradi.
# Agar topilmasa, -1 qaytaradi.