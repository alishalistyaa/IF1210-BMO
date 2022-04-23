# Selasa, 12 April 2022
# Catatan: Revisi kedua. Mengubah .replace menjadi iterasi menghilangkan \n

# Import fungsi dari directory lain
from A_Functions import *

def CSV_Parser(nama_file_csv):
    # KAMUS LOKAL
    # nama_file_csv : CSV       (yang akan di baca)
    # matriks_baru  : Matrix    (hasil membaca csv)

    # Inisialisasi matriks baru
    matriks_baru = []
    matriks_temp = []
    # Mengolah CSV
    with open(nama_file_csv, 'r', encoding='utf-8-sig') as file:
        # Membaca file dan menyimpannya di matriks sementara
        for line in file:
            matriks_temp = append_manual(matriks_temp, split_manual(line,';'))

        # Menghilangkan '\n' pada akhir setiap baris [ fungsi manual untuk .replace() ] 
        for i in range(length_manual(matriks_temp)):
            matriks_baru = append_manual(matriks_baru, remove_manual(matriks_temp[i], length_manual(matriks_temp[i])-1))

    return(matriks_baru)
            
# ------ CONTOH PENGGUNAAN --------
# print(CSV_Parser('database/kepemilikan.csv'))