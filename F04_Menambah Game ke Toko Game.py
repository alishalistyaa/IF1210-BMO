# Senin, 18 April 2022
# Catatan: 

# Mengimport Fungsi dari direktori lain
from codecs import namereplace_errors
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
def tambah_game():
    cek = False
    while cek == False:
        name= input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun = int(input('Masukkan tahun rilis: '))
        harga = int(input('Masukkan harga: '))
        stok_awal = int(input('Masukkan stok awal: '))
        if name ==''or kategori == ''or str(tahun) =='' or str(harga) =='' or str(stok_awal) == '':
            print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO')
            cek = False
        else:
            
            print('Selamat! Berhasil menambahkan game {}'.format(name))
            cek = True

aksi = input('')
if aksi == 'tambah_game':
    tambah_game()
        