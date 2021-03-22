print('konversi string')
print('daftar menu')
print('1. upper')
print('2. lower')
print('3. title')
print('4. replace')
a=int(input('menu mana yang dipilih:'))
if a == 1:
    b=str(input('kalimat yang ingin dijadikan huruf besar:'))
    print(b.upper())

elif a == 2:
    b=str(input('kalimat yang ingin dijadikan huruf kecil:'))
    print(b.lower())

elif a==3:
    b=str(input('kalimat yang ingin dijadikan judul:'))
    print(b.title())

elif a==4:
    b=str(input('kalimat apa yang ingin anda tulis:'))
    c=str(input('hurufbaru apa yang anda inginkan:'))
    d=str(input('huruf apa yang ingin anda ubah:'))
    print(b.replace(c,d))

else:
    print('invalid')
