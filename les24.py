email = input("Email manzilingizni kiriting: ")
index = email.find("@")

domen = email[index + 1:]


print("Email domeni:", domen)