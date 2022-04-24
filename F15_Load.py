# Program - F15 Load
# Program mengembalikan data parser
# Akses - Sistem

# Mengimport module yang diperlukan
import argparse
import os
import A_Data as data
from A_CSVParser import *

def cari_folder(nama_folder,path):
    # {Fungsi ini mencari folder pada direktori}
    if nama_folder == '':
        print(f'Tidak ada nama folder yang diberikan!')
        return(False)
    else:
        # CONTROL
        # print(path)
        if os.path.exists(path):
            return(True)
        else: 
            print(f'\nFolder "{nama_folder}" tidak ditemukan.')
            return(False)

def load():
    # Fungsi ini mengembalikan 
    # setup parser
    parser = argparse.ArgumentParser()
    parser.add_argument('nama_folder', help="Configuration Folder Name BNMO") #positional argument
    args = parser.parse_args()

    # CONTROL
    # print(vars(args))

    # Inisialisasi folder
    path = os.getcwd() + '/' + args.nama_folder
    valid = False
    valid = cari_folder(args.nama_folder,path)
    
    if valid:
        data.user = CSV_Parser(path+'/user.csv')
        data.game = CSV_Parser(path+'/game.csv')
        data.kepemilikan = CSV_Parser(path+'/kepemilikan.csv')
        data.riwayat = CSV_Parser(path+'/riwayat.csv')

        return True
    else:
        return False
    
# PENGGUNAAN
# load()