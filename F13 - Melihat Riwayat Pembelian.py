# Program - F13 Melihat Riwayat Pembelian
# Program Memerlukan File riwayat.csv yang berisi Riwayat Pembelian User
# Akses - User

# Mengimport Fungsi dari Direktori Lain
from A_Functions import *
from A_CSVParser import *

# Definisi Fungsi lihat_riwayat untuk Melihat Riwayat Pembelian
def lihat_riwayat():
    # Menginput user id user yang akan melihat riwayat pembelian
    user_id = str(input('Masukan user id: '))

    # Membaca riwayat.csv dan menyimpan dalam sebuah variabel
    data_riwayat = CSV_Parser('riwayat.csv')

    # Panjang data
    panjang_riwayat = length_manual(data_riwayat)

    # Variabel nomor untuk Menampilkan Pada Output
    nomor = 1
    # Variabel validasi untuk Memvalidasikan Input
    validasi = False

    # Looping Untuk Mendapatkan Data Riwayat User
    for i in range(panjang_riwayat):
        if user_id == data_riwayat[i][3]:
            id_game = data_riwayat[i][0]
            nama_game = data_riwayat[i][1]
            harga_game = data_riwayat[i][2]
            tahun_beli = data_riwayat[i][4]
            print(f'{nomor}. {id_game} | {nama_game} | {harga_game} | {tahun_beli}')
            nomor += 1
            # Validasi bernilai True Jika Terdapat Game yang Dibeli
            validasi = True
    
    # Validasi bernilai False Jika Tidak Terdapat Game yang Dibeli
    if validasi == False:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')

# Mengeluarkan Ouput Fungsi lihat_riwayat
lihat_riwayat()