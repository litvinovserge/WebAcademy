name = input("Введите имя: ")

ramka = "*" * 20
len_p = int(((20 - 2 -len(name))/2))


prob = " " * len_p

print (ramka)
print ("*" + prob + name + prob + "*")
print (ramka)
