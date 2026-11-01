import math

Duvar_Alan = float(input("Duvar alanını giriniz (m²): "))
Kutu_Maliyeti = float(input("Kutu maliyetini giriniz (TL): "))
# 1 Kutu Boya 12.5 m² alanı boyar 

Gereken_Kutu= Duvar_Alan / 12.5 
Tam_Kutu = math.ceil(Gereken_Kutu)
Maliyet = Tam_Kutu * Kutu_Maliyeti

print(f"Gereken kutu sayısı: {Tam_Kutu}")
print(f"Toplam maliyet: {Maliyet:.2f} TL")