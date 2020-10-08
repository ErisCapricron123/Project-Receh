print('Selamat Datang Selamat Berbelanja')
print('         Toko Pak Malik         ')
print('=================================')
buah ={'apel':12, 'pisang':18, 'ceri':32, 'anggur': 25 }

gambar = ['🍎', '🍌', '🍒', '🍇']
y = 0
for item in buah:
    kapital = item.capitalize()
    print('Harga '+kapital+' Rp'+str(buah[item]))

uang = int(input('Berapa jumlah uang yang ingin anda masukan?: '))
print('=================================')

for item in buah :
    kapital = item.capitalize()
    y = y + 1
    print('Harga ' + kapital + ' Rp' + str(buah[item]))
    pertanyaan = input('Apakah anda ingin membeli ' + kapital + '? (y/n) ')

    if pertanyaan == 'y' :
        gambar = {1:'🍎', 2:'🍌',3: '🍒', 4:'🍇'}
        jumlah = int(input('Anda ingin membeli berapa?: '))
        if uang < buah[item]*jumlah:
            print('Uang Anda Kurang')
            break
        print(kapital +' : '+gambar[y]*jumlah)
        harga = buah[item]*jumlah
        uang -= harga
        print('Sisa Uang Anda: ' + str(uang))
        print('=================================')
    else:
        print('eror')
