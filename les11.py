
matn = "Python"

# bu yerda P harfini inobatga olmay z ga qarayabti va false chiqyabti "Mavjud emas natija buladi "
natija = 'P' in matn and 'z' in matn 
# agar z ni urniga y qushsak natija true buladi "Harf mavjud chiqadi"

print("Matnda 'P' va 'z' harflari mavjud emas." * (not natija))

print(natija)

print("Matnda 'P' va 'y' harflari mavjud." * natija)