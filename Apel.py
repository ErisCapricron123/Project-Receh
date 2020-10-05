print('selamat datang silahkan berbelanja')
harga = 5000
jumlah = int(input("Anda mau beli berapa apel? "))
uang = int(input("Berapa uang anda? "))
total = jumlah*harga
apel='🍎'*jumlah

argumen = input("apakah anda yakin membeli" + ' '+ str(jumlah) +'apel?' + "(yes/no) ")

if argumen == 'yes' :
    if uang > total :
        print(apel)
        kembalian = uang - total
        print('sisa uang anda' + ' ' + str(kembalian))
    elif uang == total :
        print(apel)
        print('uang anda habis')
    else:
        print('uang anda kurang')

elif argumen == 'no' :
    print('silahkan datang kembali')
