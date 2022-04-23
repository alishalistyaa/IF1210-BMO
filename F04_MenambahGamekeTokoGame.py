# Program - F04 Menambah Game ke Toko Game
# Program Memerlukan File data.csv yang berisi data game
# Akses - Admin

# Mengimport Fungsi dari Direktori Lain
from A_CSVParser import *
from A_Functions import *

def check_valid_(username: str):
    """
    Fungsi yang mengecek apakah username yang dimasukkan adalah valid
    """

    # KAMUS LOKAL
    # char: str
    # username: int

    # ALGORITMA
    for char in username:
        # Jika ada karakter yang bukan huruf, angka, _ atau -, maka username tidak valid
        user = ord(char)
        if not (97 <= user <= 122 or 65 <= user <= 90 or 48 <= user <= 57 or char == "_" or char == "-"):
            return False
    return True


def tambah_game(data_game):
    # Inisialisasi data csv game
    cek = False
    while cek == False:
        nama = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun = int(input('Masukkan tahun rilis: '))
        harga = int(input('Masukkan harga: '))
        stok_awal = int(input('Masukkan stok awal: '))
        if nama ==''or kategori == ''or str(tahun) =='' or str(harga) =='' or str(stok_awal) == '':
            print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO')
            cek = False
        else:
            print('Selamat! Berhasil menambahkan game {}'.format(nama))
            cek = True

            # Generate ID GAME
            jumlah_game = length_manual(data_game)
            # Inisialisasi
            id_game = 'G'

            if jumlah_game < 100:
                id_game += '0'
            else : pass
            id_game += str(jumlah_game)
        
            # Didapat baris data baru
            game_baru =[id_game,nama,kategori,tahun,harga,stok_awal]
            # Memasukkan data ke array csv
            data_game = append_manual(data_game, game_baru)

    return(data_game)


# ------- CONTOH PENGGUNAAN -------
# (tambah_game(data.game))


# aksi = input('')
# if aksi == 'tambah_game':
#     tambah_game()
        