def nama_bulan(id, nomor):
   if 1 <= nomor <= 12: 
        print(id[nomor])
   
   elif 0 or nomor >= 13 :
        print('EROR')

bulan = ['','Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktokber','November','Desember']
nomor = int(input('Masukan nomor bulan: '))
nama_bulan(bulan, nomor)
