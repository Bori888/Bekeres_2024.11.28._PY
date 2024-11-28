kor = int(input("Mennyi idős vagy(6<): "))
while not kor > 6:
    kor = int(input("Hiba! Mennyi idős vagy: "))

nev = input("Mi a neved: ")
while not len(nev) >= 3:
    nev = input("Hiba! Mi a neved: ")

print(f"A te neved: {nev} és 4{kor} éves vagy.")

print("2. fajta megoldas\n----------------------")

jo=False
while not (jo):
    kor = int(input("Hiba! Mennyi idős vagy: "))
    nev = input("Hiba! Mi a neved: ")
    jo = (kor > 6) and (len(nev) >= 3)

#a rossz korokat ossze adja ez majd ki kell javitani hogy csak az utolsot irja ki
print(f"A te neved: {nev} és 4{kor} éves vagy.")


