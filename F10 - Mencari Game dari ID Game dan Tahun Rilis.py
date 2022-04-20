# Program - F10 Mencari Game Berdasarkan ID Game dan Tahun Rilis
# Program Memerlukan ID User yang Terintegrasikan Dengan File Kepemilikan
# Akses - User

# Mengimport Fungsi dari Direktori Lain
from A_Functions import *
from A_CSVParser import *

# Definisi Fungsi id_genre dengan Parameter variabel id game input
def id_genre(id_game_input):
    data_game = CSV_Parser('game.csv')
    panjang_game = length_manual(data_game)
    for j in range(panjang_game):
        if data_game[j][0] == id_game_input: 
            genre_game = data_game[j][2] 
    return genre_game

# Definisi Fungsi id_tahun dengan Paramater variabel id game input
def id_tahun(id_game_input):
    data_game = CSV_Parser('game.csv')
    panjang_game = length_manual(data_game)
    for j in range(panjang_game):
        if data_game[j][0] == id_game_input: 
            tahun_game = data_game[j][3] 
    return tahun_game

# Definisi Fungsi cek_id_game_dan_tahun_rilis()
def cek_id_game_dan_tahun_rilis():

    # Input id game dan tahun game
    id_game_input = str(input('Masukkan ID Game: '))
    tahun_game_input = str(input('Masukkan Tahun Rilis Game: '))

    # CSV RIWAYAT
    data_riwayat = CSV_Parser('riwayat.csv')
    panjang_riwayat = length_manual(data_riwayat)

    # CSV GAME
    data_game = CSV_Parser('game.csv')
    panjang_game = length_manual(data_game)

    # Mengeluarkan Output Berupa Kalimat
    print('Daftar game pada inventory yang memenuhi kriteria:')

    # Variabel nomor untuk Menampilkan Pada Output
    nomor = 1

    # Variabel validasi untuk Memvalidasikan Input
    validasi = False

    # PROGRAM UTAMA
    # Jika input tahun rilis kosong dan input id game benar
    if (tahun_game_input == ''):
        for j in range(panjang_riwayat):
            if id_game_input == data_riwayat[j][0]:
                id_game = data_riwayat[j][0]
                nama_game = data_riwayat[j][1]
                harga_game = data_riwayat[j][2]
                genre_game = id_genre(id_game_input)
                tahun_game = id_tahun(id_game_input)

                print(nomor, f'. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_game}')
                nomor += 1
                validasi = True

    # Jika input tahun rilis benar dan input id game kosong
    if (id_game_input == ''):
        for j in range(panjang_game):
            if tahun_game_input == data_game[j][3]:
                for i in range(panjang_riwayat):
                    id_game = data_game[j][0]
                    nama_game = data_game[j][1]
                    harga_game = data_game[j][4]
                    genre_game = data_game[j][2]

                    if id_game == data_riwayat[i][0]: 
                        tahun_game = data_game[j][3]
                        print(nomor, f'. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_game}')
                        nomor += 1
                        validasi = True
                        
    # Jika input tahun rilis benar dan input id game benar
    if id_game_input != '' and tahun_game_input != '':
        for i in range(panjang_riwayat):
            id_game = data_riwayat[i][0]
            for j in range(panjang_game):
                tahun_game = data_game[j][3]
                if id_game_input == id_game and tahun_game_input == tahun_game:
                    nama_game = data_riwayat[i][1]
                    harga_game = data_riwayat[i][2]
                    genre_game = data_game[j][2]
                    print(nomor, f'. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_game}')
                    nomor += 1
                    validasi = True
                    break

    # Jika input tahun rilis kosong dan input id game kosong
    if id_game_input == '' and tahun_game_input == '':
        for i in range(panjang_riwayat):
            id_game = data_riwayat[i][0]
            nama_game = data_riwayat[i][1]
            harga_game = data_riwayat[i][2]
            for j in range(panjang_game):
                if id_game == data_game[j][0]:
                    genre_game = data_game[j][2]
                    tahun_game = data_game[j][3]
                    print(nomor, f'. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_game}')
                    nomor += 1
                    validasi = True

    # Jika validasi bernilai False maka Tidak ada Game yang Memenuhi Kriteria
    if validasi == False:
        print('Tidak ada game pada inventory-mu yang memenuhi kriteria')

# Memanggil Fungsi cek_id_game_dan_tahun_rilis()
cek_id_game_dan_tahun_rilis()