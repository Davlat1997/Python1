narx = float(input("Mahsulot narxini kiriting: "))
foiz = float(input("Chegirma foizini kiriting: "))

chegirma = narx * (foiz / 100)
lastnarx = narx - chegirma

print(f"Sizga {chegirma:.2f} so'm: << chegirma qildik.  ")
print(f"Foizni hisobladik sizning chegirmadan chiqgan narxiz: {lastnarx:.2f} so'm")