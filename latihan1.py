txt = 'Hello World'
hitung = len(txt)
terakhir = txt[-1]
index = txt[2:5]
hapus = txt.replace(' ', '')
besar = txt.upper()
kecil = txt.lower()
ganti = txt.replace('H', 'J')

print("Text \t\t\t\t\t: "+txt)
print("Jumlah karakter \t\t\t:",hitung)
print("Karakter terakhir \t\t\t: "+terakhir)
print("Karakter index ke-2 sampai index ke-4 \t: "+index)
print("Spasi dihilangkan \t\t\t: "+hapus)
print("Huruf besar \t\t\t\t: "+besar)
print("Huruf kecil \t\t\t\t: "+kecil)
print("Ganti karakter H dengan karakter j \t: "+ganti)
