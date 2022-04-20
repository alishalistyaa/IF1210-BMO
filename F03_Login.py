# Senin, 18 April 2022
# Catatan: 

# Mengimport Fungsi dari direktori lain
from A_CSVParser import CSV_Parser
from A_Functions import *
from F02_Register import *


def login():
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    user = CSV_Parser('fileuser.csv')
    a = length_manual(user)
    for i in range(a):
        for j in range(6):
            if username == user[i][1]:
                x = i
    
    if is_username_available(username):
        if password== user[x][3]:
            nama = user[x][2]
            print("Halo {}! Selamat datang di “Binomo”.".format(nama))

        else:
            print("Password atau username salah atau tidak ditemukan.")
    else:
        print("Password atau username salah atau tidak ditemukan.")

cek = False
aksi = input("")
while cek == False:
    if aksi == 'login':
        login()
        cek = True
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”")