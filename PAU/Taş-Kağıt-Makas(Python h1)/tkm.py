# Taş-kağıt-makas
# Kodunuzu bu dosya içine yazınız
"""
Kodunuzun düzgün çalışması için
input metodunun içindeki metni boş bırakın
input('')
şeklinde...
"""
o1 = input('')
o2 = input('')

if o1 == o2:
    print("berabere")
elif o1== "taş" and o2 == "makas" or o1== "kağıt" and o2 == "taş" or o1== "makas" and o2 == "kağıt":
    print ("birinci oyuncu kazandı")
else:
    print ("ikinci oyuncu kazandı")