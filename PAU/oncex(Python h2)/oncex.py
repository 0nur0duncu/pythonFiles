"""Kodunuzu bu dosyaya yazın. Girdi alırken input metodunun içini boş bırakın
input('')
şeklinde ve ekrana istenen çıktı dışında başka bir şey yazdırmayın."""
xbaslayan = []
xbaslamayan = []

kelime = input('')
while kelime != "" :
    if kelime.startswith("x"):
        xbaslayan.append(kelime)
    else:
        xbaslamayan.append(kelime)
    kelime = input('')
    
xbaslamayan.sort()
xbaslayan.sort()

for eleman in xbaslayan+xbaslamayan : #combine the strings (but start with xbaslayan) and print the elements
    print(eleman)
    