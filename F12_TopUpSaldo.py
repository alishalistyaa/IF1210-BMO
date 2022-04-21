# Program - F12 Top Up Saldo
# Program Memerlukan Aksi Save untuk Menyimpan ke Database
# Akses - Admin

# Mengimport Fungsi dari Direktori Lain
from A_Functions import *
from A_CSVParser import *

# Definsi Fungsi topup_saldo untuk Topup Saldo
def topup_saldo(data_user):
    # Menghitung panjang variabel data_user
    panjang_data_user = length_manual(data_user)
    
    # Menginput username
    username_input = str(input('Masukan username: '))
    # Menginput saldo yang ingin di topup
    saldo_topup = str(input('Masukan saldo: '))

    # Boolean untuk validasi username
    validasi = False

    # Looping untuk mendapatkan kevalidan dan hasil topup
    for i in range(1, panjang_data_user):
        if data_user[i][1] == username_input:
            # Jika topup saldo Diatas dan Sama Dengan Nol
            if int(saldo_topup) >= 0:
                saldo_asli = int(data_user[i][5])
                saldo_sekarang = str(int(saldo_topup) + saldo_asli)
                print(f'Top up berhasil. Saldo {data_user[i][2]} bertambah menjadi {saldo_sekarang}.')
                break
            # Jika topup saldo dibawah Nol
            if int(saldo_topup) < 0:
                # Jika Total di Database Masih diatas atau sama dengan Nol
                if (int(saldo_topup) + int(data_user[i][5])) >= 0:
                    saldo_sekarang = (int(data_user[i][5]) + int(saldo_topup))
                    print(f'Top up berhasil. Saldo {data_user[i][2]} bertambah menjadi {saldo_sekarang}.')
                    break
                # Jika Total di Database dibawah Nol
                if (int(saldo_topup) + int(data_user[i][5])) < 0:
                    saldo_sekarang = int(data_user[i][5])
                    print('Masukan tidak valid')
                    break
            validasi = True

    # Jika Validasi Bernilai Tidak True yaitu Username Input tidak ada yang sesuai
    if validasi != True :
        if data_user[i][1] != username_input :
            if saldo_topup != '' or saldo_topup == '':
                return(print(f'Username {username_input} tidak ditemukan'))

    # Mengoutput data_user
        if data_user[i][1] == username_input :
            (data_user[i][5]) = str(saldo_sekarang)
            
    return(data_user)

# Mengeluarkan Output Fungsi topup_saldo
#print(topup_saldo('database'))
