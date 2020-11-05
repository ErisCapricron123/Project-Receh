def dukun(angka):
    if angka % 2 == 0:
        print("Bilangan", angka ,"adalah genap")
    elif angka % 2 == 1:
        print('Bilangan', angka , "adalah ganjil")

angka = int(input("Masukan angka: "))
dukun(angka)
