# Program - F09
# Program Melihat Gameku
# Akses - User

from A_Functions import *
from A_Pemanis import *

def melihat_gameku(user_id, data_riwayat, data_game):
    # KAMUS LOKAL
    # data_riwayat, data_game : matrix hasil parsing
    # properti_game : array
    # data_gameku : matrix hasil

    # Inisialisasi matrix dan array kosong
    loading()
    data_gameku = []
    properti_game = []

    # ALGORITMA UTAMA
    for i in range(length_manual(data_riwayat)):
        # Mencari user_id di data riwayat
        if data_riwayat[i][3]== user_id:
            game_id_dipunya = data_riwayat[i][0] # Maka didapatkan ID Game

            # Mencari ID Game tersebut di data game
            for j in range(length_manual(data_game)):
                if data_game[j][0] == game_id_dipunya:

                    # Jika ditemukan ID Game, append properti dari game tersebut:
                    # Game ID, Nama, Harga, User_id, Tahun_beli
                    for k in range(length_manual(data_game[j])):
                        properti_game = append_manual(properti_game, data_game[j][k])
                    # Mengappend properti tersebut ke list kosong
                    data_gameku = append_manual(data_gameku, properti_game)
                    # Riset array kosong sehingga dapat dicari lagi dengan ID Game berbeda
                    properti_game = []

            # Print hasil:
            # Jika belum pernah membeli game
    if data_gameku==[]:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        # Jika ada game
        # Cari length terpanjang dari tiap komponen biar rapi
        # karena game id dan tahun pasti sama panjangnya, maka diskip
        # karena harga panjangnya di akhir, maka diskip juga

        # Mencari length terpanjang dari nama_game
        max_nama = max_length(data_gameku,1)
        if max_nama < (length_manual('NAMA')):
            max_nama = 4
                
        # Mencari length terpanjang dari kategori
        max_kategori = max_length(data_gameku,2) 
        if max_kategori < (length_manual('KATEGORI')):
            max_kategori = 8 

        max_nomor = (length_manual(data_game) % 10) + 1

        print('\n------------------------------------------------------------')        
        print(f"   ID   | NAMA{' '*(max_nama-4)} | KATEGORI{' '*(max_kategori-8)} | TAHUN RILIS  | HARGA ")
        print('------------------------------------------------------------')
        for i in range(length_manual(data_gameku)):
            spasi_nama = ' '*(max_nama-length_manual(data_gameku[i][1]))
            spasi_kategori = ' '*(max_kategori-length_manual(data_gameku[i][2]))
            spasi_nomor = ' '*(max_nomor-length_manual(str(i+1)))
            print(f"{spasi_nomor}{i+1}. {data_gameku[i][0]} | {data_gameku[i][1]}{spasi_nama} | {data_gameku[i][2]}{spasi_kategori} | {data_gameku[i][3]}{' '* 7} | {data_gameku[i][4]}")
        print('------------------------------------------------------------')
    return(data_gameku)

# ---- CONTOH PENGGUNAAN ----
# melihat_gameku(user_id, data.riwayat, data.game)
