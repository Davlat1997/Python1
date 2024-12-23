
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
print("\n")
natija = son1 == son2
print("Sonlar tengmi? ")
print(natija)
print("\n")
print("sonlar teng!" * (son1 == son2))
print("sonlar teng emas!" * (son1 != son2))