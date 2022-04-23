# Program - F05 Mengubah Game pada Toko
# Program Memerlukan File game.csv yang berisi data Game
# Akses - Admin

# Mengimport fungsi dari direktori lain
from A_CSVParser import *
from A_Functions import *


def ubah_data_game(data_game):
    # Input user
    id_game_input = str(input("Masukkan ID game: "))
    nama_game = str(input("Masukkan nama game: "))
    kategori_game = str(input("Masukkan kategori: "))
    tahun_rilis = str(input("Masukkan tahun rilis: "))
    harga_game = str(input("Masukkan harga:"))

    # Mencari ID Game
    panjang_game = length_manual(data_game)
    for i in range(panjang_game):
        if data_game[i][0] == id_game_input:
            index = i
            break
    
    data_baru = [id_game_input, nama_game, kategori_game, tahun_rilis, harga_game]
    for j in range(1, length_manual(data_baru)):
        if data_baru[j] == '':
            pass
        else: 
            data_game[index][j] = data_baru[j]
    return(data_game)

# ------- CONTOH PENGGUNAAN -------
# (ubah_data_game('database'))