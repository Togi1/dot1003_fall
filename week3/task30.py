Numara_sayisi = 0
toplam=0
tek=0
cift=0
print("Dumb calculator v0.1 if you want to exit, enter 0.")


deger = True 

print("If you want to exit, enter 0.")
while deger:
    girilen_deger=int(input("Please enter a number:"))

    if girilen_deger != 0 :
        Numara_sayisi= Numara_sayisi + 1 
       
        toplam = toplam+girilen_deger
        if girilen_deger %2 == 0 :
            cift = cift+ 1
        else :
            tek = tek + 1 

    else:
        deger = False

print(f"Numara Sayisi: {Numara_sayisi}")
print(f"Toplam: {toplam}")
print(f"Tek: {tek} Cift: {cift}")
print(f"Ortalama: {toplam/Numara_sayisi}")
    
