# Program - F10 Mencari Game Berdasarkan ID Game dan Tahun Rilis
# Program Memerlukan ID User yang Terintegrasikan Dengan File Kepemilikan
# Akses - User

# Mengimport Fungsi dari Direktori Lain
from A_Functions import *
from A_Pemanis import *


# Definisi Fungsi id_user untuk memvalidasi username
def id_user(data_user, panjang_user,username):
    for i in range(panjang_user):
        if data_user[i][1] == username:
            id_user = data_user[i][0]
    return id_user

# Definisi Fungsi id_genre dengan Parameter variabel id game input
def id_genre(id_game_input, data_game, panjang_game):
    for j in range(panjang_game):
        if data_game[j][0] == id_game_input: 
            genre_game = data_game[j][2] 
    return genre_game

# Definisi Fungsi id_tahun dengan Paramater variabel id game input
def id_tahun(id_game_input,data_game,panjang_game):
    for j in range(panjang_game):
        if data_game[j][0] == id_game_input: 
            tahun_game = data_game[j][3] 
    return tahun_game

# Definisi Fungsi cek_id_game_dan_tahun_rilis()
def cek_id_game_dan_tahun_rilis(data_game,data_riwayat,data_kepemilikan,data_user, username):
    # Inisialisasi
    panjang_user = length_manual(data_user)
    panjang_game = length_manual(data_game)
    panjang_riwayat = length_manual(data_riwayat)
    panjang_kepemilikan = length_manual(data_kepemilikan)

    # Input id game dan tahun game
    id_game_input = str(input('Masukkan ID Game: '))
    tahun_game_input = str(input('Masukkan Tahun Rilis Game: '))
    loading()
    
    # Mengeluarkan Output Berupa Kalimat
    print('Daftar game pada inventory yang memenuhi kriteria:')
    
    # Variabel nomor untuk Menampilkan Pada Output
    nomor = 1
    
    # PROGRAM UTAMA
    validasi = False
    for k in range(panjang_kepemilikan):
        id_us = id_user(data_user, panjang_user,username)
        if id_us == data_kepemilikan[k][1]:
            validasi_user = True
            if validasi_user == True:
                # Jika input tahun rilis kosong dan input id game benar
                if (tahun_game_input == ''):
                    if id_game_input == data_kepemilikan[k][0]:
                        id_game = data_kepemilikan[k][0]
                        nama_game = data_game[k][1]
                        harga_game = data_game[k][4]
                        genre_game = id_genre(id_game_input, data_game, panjang_game)
                        tahun_game = id_tahun(id_game_input,data_game,panjang_game)

                        print(nomor, f'. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_game}')
                        nomor += 1
                        validasi = True
                
                # Jika input tahun rilis benar dan input id game kosong        
                if (id_game_input == ''):
                    if tahun_game_input == data_game[k][3]:
                        id_game = data_game[k][0]
                        nama_game = data_game[k][1]
                        harga_game = data_game[k][4]
                        genre_game = data_game[k][2]

                        if id_game == data_kepemilikan[k][0]: 
                            tahun_game = data_game[k][3]
                            print(nomor, f'. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_game}')
                            nomor += 1
                            validasi = True
                
                # Jika input tahun rilis benar dan input id game benar
                if id_game_input != '' and tahun_game_input != '':
                    id_game = data_kepemilikan[k][0]
                    tahun_game = data_game[k][3]
                    if id_game_input == id_game and tahun_game_input == tahun_game:
                        nama_game = data_riwayat[k][1]
                        harga_game = data_riwayat[k][2]
                        genre_game = data_game[k][2]
                        print(nomor, f'. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_game}')
                        nomor += 1
                        validasi = True
                        break

                # Jika input tahun rilis kosong dan input id game kosong
                if id_game_input == '' and tahun_game_input == '':
                    id_game = data_game[k][0]
                    nama_game = data_game[k][1]
                    harga_game = data_game[k][4]
                    if id_game == data_kepemilikan[k][0]:
                        genre_game = data_game[k][2]
                        tahun_game = data_game[k][3]
                        print(nomor, f'. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_game}')
                        nomor += 1
                        validasi = True

    # Jika validasi bernilai False maka Tidak ada Game yang Memenuhi Kriteria
    if validasi == False:
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')    

# Memanggil Fungsi cek_id_game_dan_tahun_rilis()
# cek_id_game_dan_tahun_rilis(data.game, data.riwayat)