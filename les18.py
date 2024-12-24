number = input("Telefon raqamingizni kiriting: ")
formats = f"+998 ({number[:2]})-{number[2:5]}-{number[5:7]}-{number[7:]}"
print("Formatlangan raqam:", formats)