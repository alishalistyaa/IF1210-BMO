# Program - F16 Save
# Program Memerlukan File data.csv, riwayat.csv, user.csv, kepemilikan.csv 
# yang berisi data User, Game, Riwayat dan Kepemilikan
# Akses - Admin dan User

# Mengimport library
import os
from A_Functions import *

def array_to_csv(array):
    # KAMUS LOKAL
    # array : matriks
    # data, header : str

    # ALGORITMA
    # Inisialisasi data pertama = kosong
    data = ''
    # melakukan .join manual
    for i in range(length_manual(array)):
        for j in range(length_manual(array[i])):
            data += str(array[i][j])
            # jika sudah di akhir baris tidak udah ada ;
            if j != (length_manual(array)-1): 
                data += ';'
        # jika sudah di akhir baris, make a new line
        data += "\n"
    return(data)

def pilih_folder(nama_folder):
    # checking folder
    path = os.getcwd() + '/' + nama_folder

    # Jika folder sudah ada
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return

def write_file(data_array,nama_folder, nama_file):
    f = open(nama_folder+'/'+nama_file, "w")
    f.write(array_to_csv(data_array))
    f.close()

def save(data_game, data_kepemilikan, data_riwayat, data_user):
    nama_folder = str(input("Masukkan nama folder penyimpanan: "))
    pilih_folder(nama_folder)

    # Inisialisasi write folder 
    write_file(data_game,nama_folder,'game.csv')
    write_file(data_kepemilikan,nama_folder,'kepemilikan.csv')
    write_file(data_riwayat,nama_folder,'riwayat.csv')
    write_file(data_user,nama_folder,'user.csv')

    print("Saving...")
    print(f"Data telah disimpan pada folder {nama_folder}!")

