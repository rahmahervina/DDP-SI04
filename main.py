import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f"Luas Persegi {sisi} * {sisi} = {luas}")
    print(f"Keliling Persegi adalah {keliling}")

def l_persegipanjang(panjang, lebar):
    luas = panjang*lebar
    keliling = 2*panjang+lebar
    print(f"Luas PersegiPanjang {panjang} * {lebar} = {luas}")
    print(f"Keliling PersegiPanjang adalah {2} * {panjang} + {lebar} = {keliling}")

def l_segitiga(alas, tinggi):
    luas = 0.5*alas*tinggi
    print(f"Luas Segitiga {0.5} * {alas} * {tinggi} = {luas}")

def l_lingkaran(r1, r2):
    luas = 3.14 * r1 * r2 
    print(f"Luas lingkaran ini adalah phi * {r1} * {r2} = {luas}")

def l_jajargenjang(alas, tinggi):
    luas = alas * tinggi
    print(f"Luas Jajargenjang adalah {alas} * {tinggi} = {luas}")

def v_kubus(sisi):
    volume = sisi*sisi*sisi
    print(f"Volume Kubus adalah {sisi} * {sisi} * {sisi} = {volume}")

def v_balok(panjang, lebar, tinggi):
    volume = panjang*lebar*tinggi
    print(f"Volume Balok adalah {panjang} * {lebar} * {tinggi} = {volume}")

def v_limas(luasalas, tinggi):
    volume = 1/3*luasalas*tinggi
    print(f"Volume Limas adalah {1/3} * {luasalas} * {tinggi} = {volume}")

def v_prisma(luasalas, tinggi):
    volume = luasalas * tinggi
    print(f"Volume Prisma adalah {luasalas} * {tinggi} = {volume}")

def v_bola(r1, r2, r3):
    volume = 4/3*r1*r2*r3
    print(f"Volume Bola adalah {4/3} * {r1} * {r2} * {r3} = {volume}")