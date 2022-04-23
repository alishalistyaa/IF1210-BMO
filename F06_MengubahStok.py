# Program - F06 Mengubah Stok
# Program Memerlukan File game.csv yang berisi data Game
# Akses - Admin

# Mengimport Fungsi dari direktori lain
from A_CSVParser import *
from A_Functions import *

def ubah_stok(data_game):
    # KAMUS LOKAL
    # data_game                : matrix
    # panjang_data             : int
    # id_game, nama_game       : string
    # tambah_stok, stok_baru   : int


    # ALGORITMA
    # Input masukan
    id_game = str(input("Masukkan ID game: "))

    # Membaca panjang data 
    panjang_data = length_manual(data_game)

    for i in range(panjang_data):
        if data_game[i][0] == id_game:
            # Mengekstrak data
            nama_game = data_game[i][1]
            stok_game = int(data_game[i][5])
            # Input data stok
            tambah_stok = int(input("Masukkan jumlah: "))
            
            # Data baru
            stok_baru = stok_game + tambah_stok

            if stok_baru < 0:   # Jika stoknya kurang
                print(f"Stok game {nama_game} gagal dikurangi karena stok kurang. Stok sekarang: {stok_game} (<{tambah_stok*(-1)})")
                break
            else:               # Jika stok tidak kurang
                # Perbarui data game
                data_game[i][5] = stok_baru
                # Output
                if tambah_stok > 0:
                    print(f"Stok game {nama_game} berhasil ditambahkan. Stok sekarang: {stok_baru}")
                elif tambah_stok < 0:
                    print(f"Stok game {nama_game} berhasil dikurangi. Stok sekarang: {stok_baru}")
                elif tambah_stok == 0:
                    print(f"Tidak ada perubahan dalam stok")
            break

        elif i == (panjang_data-1):
            print("Tidak ada game dengan ID tersebut!")
    
    return(data_game)

# ------- CONTOH PENGGUNAAN -------
# print(ubah_stok('database'))