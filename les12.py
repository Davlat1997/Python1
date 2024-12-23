matn1 = input("1-matnni kiriting: ")
matn2 = input("2-matnni kiriting: ")


print("Ikkala matn bir xil obyektmi?")
natija2 = matn1 is not matn2
natija = matn1 is matn2
print("Bir xil!" * natija) 
print(natija) 
print("Bir xil emas!" * natija2)  