# Senin, 18 April 2022
# Catatan: 

# Mengimport Fungsi dari direktori lain
from A_CSVParser import CSV_Parser
from A_Functions import *
from F02_Register import *


def login(data_user):
    # KAMUS LOKAL
    # data_user : array
    # username, password : str
    # a: int

    # ALGORITMA UTAMA
    # Inisialisasi input
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    # Parsing CSV

    # Looping untuk username
    a = length_manual(data_user)
    for i in range(a):
        for j in range(6):
            if username == data_user[i][1]:
                x = i
    # Mengecek apakah username cocok dengan password
    if is_username_available(username, data_user):
        if password== data_user[x][3]:
            nama = data_user[x][2]
            id_user = data_user[x][0]
            print("Halo {}! Selamat datang di “Binomo”.".format(nama))

        else:
            return(print("Password atau username salah atau tidak ditemukan."))
    else:
        return(print("Password atau username salah atau tidak ditemukan."))
    
    # jika username cocok, mengembalikan user_id
    return(id_user)
    
# ------- CONTOH PENGGUNAAN -------
# login(data.user)