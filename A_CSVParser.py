# Sabtu, 9 April 2022
# Catatan:

# Import fungsi dari directory lain
from A_Functions import *

def CSV_Parser(nama_file_csv):
    # KAMUS LOKAL
    # nama_file_csv : CSV       (yang akan di baca)
    # matriks_baru  : Matrix    (hasil membaca csv)

    # Inisialisasi matriks baru
    matriks_baru = []
    # Mengolah CSV
    with open(nama_file_csv, 'r') as file:
        for line in file:
            matriks_baru = append_manual(matriks_baru, split_manual(line.replace('\n',''),';'))
    
    return(matriks_baru)
            
# ------ CONTOH PENGGUNAAN --------
# CSV_Parser('datatest.csv')