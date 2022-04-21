# 18 April 2022
# Catatan:

# Mengimport library
from F16_Save import *

def exit(data_game, data_kepemilikan, data_riwayat, data_user):
    validasi = False

    while validasi == False:
        apakah_simpan = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
        if apakah_simpan == 'Y' or apakah_simpan =='y':
            return(save(data_game, data_kepemilikan, data_riwayat, data_user))
        elif apakah_simpan =='N' or apakah_simpan =='n':
            return(print("Keluar file tanpa menyimpan..."))
        else: validasi = False

# ------ CONTOH PENGGUNAAN -------
# exit(arraygame, arraykepemilikan, arrayriwayat, arrayuser)