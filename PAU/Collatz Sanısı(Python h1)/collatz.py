# Collatz sanısı
# Kodunuzu bu dosya içine yazınız
"""
Kodunuzun düzgün çalışması için
input metodunun içindeki metni boş bırakın
input('')
şeklinde...
"""
sayi = int(input(''))
i=0
while sayi != 1:
    if sayi%2 == 0 :
        sayi /= 2
    else:
        sayi = 3*sayi +1
    i += 1
        
print(i)