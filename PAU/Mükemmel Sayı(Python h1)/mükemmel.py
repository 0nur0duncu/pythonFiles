# Mükemmel sayı
# Kodunuzu bu dosya içine yazınız
"""
Kodunuzun düzgün çalışması için
input metodunun içindeki metni boş bırakın
input('')
şeklinde...
"""
sayi = int(input(''))
toplam =0
for i in range(1,sayi//2+1):
    if sayi % i ==0:
        toplam += i
        
if toplam == sayi:
    print("mükemmel")
else:
    print("mükemmel değil")