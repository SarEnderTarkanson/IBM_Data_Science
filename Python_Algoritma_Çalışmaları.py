isim = input('İsminizi ve Soyisminizi giriniz: ')

sesli = 'aeıioöuüAEIİOÖUÜ'

sayaç = 0
sayaç_sessiz = 0

for i in isim:
    if i in sesli:
        sayaç += 1
    elif i not in sesli:
        sayaç_sessiz += 1
print(f'Sesli Harf Sayısı: {sayaç}')
print(f'Sessiz Harf Sayısı: {sayaç_sessiz}')