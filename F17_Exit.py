# Program - F17 Exit
# Program Memerlukan File data.csv, riwayat.csv, user.csv, kepemilikan.csv 
# yang berisi data User, Game, Riwayat dan Kepemilikan
# Akses - User dan Admin

# Mengimport library
from F16_Save import *
from A_Pemanis import *

def exit(data_game, data_kepemilikan, data_riwayat, data_user):
    validasi = False

    while validasi == False:
        apakah_simpan = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
        if apakah_simpan == 'Y' or apakah_simpan =='y':
            nama_folder = save(data_game, data_kepemilikan, data_riwayat, data_user)
            animatedbmo_end(folder_end)
            return(print(f"Data telah disimpan pada folder {nama_folder}!"))
        elif apakah_simpan =='N' or apakah_simpan =='n':
            animatedbmo_end(folder_end)
            return(print("Keluar program tanpa menyimpan!"))
        else: validasi = False

# ------ CONTOH PENGGUNAAN -------
# exit(arraygame, arraykepemilikan, arrayriwayat, arrayuser)