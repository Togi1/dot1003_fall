def agac():
    yukseklik =int(input("agac yuksekligi: "))
    kutu_boyutu=int(input("kutu boyutu: "))
    agac_genisligi=2*yukseklik-1
    if kutu_boyutu<agac_genisligi:
        print("hata: kutu boyutu agactan kucuk olamaz")
        return
    print("-"*kutu_boyutu)
    bosluk=(kutu_boyutu)*" "
    print(f"|{bosluk}|")
    for i in range(1,yukseklik+1):
        yildiz_sayisi=2*i-1
        bosluk_sayisi=yukseklik-i
        satir_icerigi=(" "*bosluk_sayisi)+("*"*yildiz_sayisi)
        sag_bosluk=kutu_boyutu-len(satir_icerigi)
        print(f"|{satir_icerigi}{' '*sag_bosluk}|")
    govde_bosluk=yukseklik-1
    govde_satiri=(" "*govde_bosluk)+"*"
    sag_govde_bosluk=kutu_boyutu-len(govde_satiri)
    print(f"|{govde_satiri}{' '*sag_govde_bosluk}|")
    print("-"*kutu_boyutu)
agac()
