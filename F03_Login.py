# Program - F03 Login
# Program Memerlukan File user.csv yang berisi Data User
# Akses - User dan Admin

# Mengimport Fungsi dari Direktori Lain
from A_CSVParser import CSV_Parser
from A_Functions import *
import A_Data as data
from F02_Register import *
from B01_Cipher import *


def login(data_user):
    # KAMUS LOKAL
    # data_user : array
    # username, password : str
    # a: int

    # ALGORITMA UTAMA
    # Inisialisasi input
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    # Looping untuk username
    a = length_manual(data_user)
    for i in range(a):
        for j in range(6):
            if username == data_user[i][1]:
                x = i
    # Mengecek apakah username cocok dengan password
    if is_username_available(username, data_user):
        if password == dekripsi(data_user[x][3], data.PASSWORD_KEY):
            nama = data_user[x][2]
            id_user = data_user[x][0]
            print("Halo {}! Selamat datang di “Binomo”.".format(nama))

        else:
            id_user = 9999
            print("Password atau username salah atau tidak ditemukan.")
            return(id_user)

    else:
        id_user = 9999
        print("Password atau username salah atau tidak ditemukan.")
        return(id_user)
    
    # jika username cocok, mengembalikan user_id
    return(id_user)
    
# ------- CONTOH PENGGUNAAN -------
# login(data.user)