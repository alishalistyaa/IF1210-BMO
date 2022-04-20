# 18 April 2022
# Catatan:

# Mengimport library
import os
from A_DataFunctions import *

array = [['G001', 'Abahsja', 'Ass', '2000', '15', '1'], ['G002', 'B', 'Bs', '2000', '1', '5'], ['G003', 'Csn', 'Cssss', '2000', '2', '10'], ['G004', 'Dsjjs', 'Dss', '2011', '3000', '20'],['G004', 'Dsjjs', 'Dss', '2011', '3000', '20'],['G004', 'Dsjjs', 'Dss', '2011', '3000', '20']]

def array_to_csv(array, header):
    # KAMUS LOKAL
    # array : matriks
    # data, header : str

    # ALGORITMA
    # Inisialisasi data pertama = header
    data = header
    # melakukan .join manual
    for i in range(length_manual(array)):
        for j in range(length_manual(array)):
            data += array[i][j]
            # jika sudah di akhir baris tidak udah ada ;
            if j != (length_manual(array)-1): 
                data += ';'
        # jika sudah di akhir baris, make a new line
        data += "\n"
    return(data)

def pilih_folder(nama_folder):

    # checking folder
    path = os.getcwd() + '/' + folder_name

    # Jika folder sudah ada
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return

pilih_folder()

def save(array_game, array_kepemilikan, array_riwayat, array_user):
    folder_name = str(input("Masukkan nama folder penyimpanan: ")) 
    
    print("Saving...")
    print(f"Data telah disimpan pada folder {folder_name}!")


print(array_to_csv(array,'id;nama;kategori;tahunrilis;harga;stok\n'))