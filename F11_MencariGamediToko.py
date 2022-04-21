# Program - F11 Mencari Game di Toko
# Program Tidak Memerlukan ID User Karena Hanya Mencari Game di Database Toko
# Akses - Admin dan User

# Mengimport Fungsi dari Direktori Lain
from A_Functions import *

# Mendefinisikan Fungsi search_game_at_store()
def search_game_at_store(data_game):

    # Menentukan Panjang Variabel panjang_game
    panjang_game = length_manual(data_game)

    # Variabel nomor untuk menampilkan nomor
    nomor = 1

    # Validasi 
    validasi = False

    # Input untuk Mencari Data yang Diinginkan (input meliputi id, nama, harga, genre, tahun rilis game yang ingin dicari)
    id_game = str(input('Masukkan ID Game: '))
    nama_game = str(input('Masukkan Nama Game: '))
    harga_game = str(input('Masukkan Harga Game: '))
    genre_game = str(input('Masukkan Kategori Game: '))
    tahun_rilis = str(input('Masukkan Tahun Rilis Game: '))
    
    # Mengeluarkan Ouput Kalimat Awal
    print('Daftar game pada toko yang memenuhi kriteria:')

    # Looping Sepanjang variabel panjang_game yang Merupakan Panjang Database Toko
    for i in range(panjang_game):

        # Jika Semua Input Tidak Kosong dan Benar Ada di Database Toko (output merupakan tulisan sesuai game yang ada)
        if id_game == data_game[i][0] and nama_game == data_game[i][1] and harga_game == data_game[i][4] and genre_game == data_game[i][2] and tahun_rilis == data_game[i][3]:
            print(f'{nomor}. {id_game} | {nama_game} | {harga_game} | {genre_game} | {tahun_rilis} | {data_game[i][5]}')
            # Validasi bernilai True yang Menandakan Game Ada di Database Toko
            validasi = True

        # Jika Input Terdapat Beberapa yang Kosong Tetapi Input id game Sesuai Database Toko
        if id_game == data_game[i][0]: 
            if nama_game == data_game[i][1] or nama_game == '':
                if harga_game == data_game[i][4] or harga_game == '':
                    if genre_game == data_game[i][2] or genre_game == '':
                        if tahun_rilis == data_game[i][3] or tahun_rilis == '':
                            print(f'{nomor}. {data_game[i][0]} | {data_game[i][1]} | {data_game[i][4]} | {data_game[i][2]} | {data_game[i][3]} | {data_game[i][5]}')
                            nomor += 1
                            # Validasi bernilai True yang Menandakan Game Ada di Database Toko
                            validasi = True

        # Jika Input Terdapat Beberapa yang Kosong Tetapi Input id game Kosong
        if id_game == '':
            if nama_game == data_game[i][1] or nama_game == '':
                if harga_game == data_game[i][4] or harga_game == '':
                    if genre_game == data_game[i][2] or genre_game == '':
                        if tahun_rilis == data_game[i][3] or tahun_rilis == '':
                            
                            # Jika Semua Input Kosong Tetapi Input id game Kosong
                            if id_game == '' and nama_game == '' and harga_game == '' and genre_game == '' and tahun_rilis == '':
                                print(f'{nomor}. {data_game[i+1][0]} | {data_game[i+1][1]} | {data_game[i+1][4]} | {data_game[i+1][2]} | {data_game[i+1][3]} | {data_game[i+1][5]}')
                                nomor += 1
                                if i == 6:
                                    # Validasi bernilai True yang Menandakan Game Ada di Database Toko
                                    validasi = True
                                    break

                            # Jika Input Terdapat Beberapa yang Kosong Tetapi Input id game Kosong
                            else:
                                print(f'{nomor}. {data_game[i][0]} | {data_game[i][1]} | {data_game[i][4]} | {data_game[i][2]} | {data_game[i][3]} | {data_game[i][5]}')
                                nomor += 1
                                validasi = True

# Jika Validasi bernilai False, Maka Tidak ada Input yang Memenuhi Kriteria
    if validasi == False:
        print('Tidak ada game pada toko yang memenuhi kriteria')

# Memanggil Fungsi search_game_at_store()
# search_game_at_store('database')