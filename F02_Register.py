# Program - F02 Register
# Program Memerlukan File user.csv yang berisi data User
# Akses - Admin

# Mengimport Fungsi dari Direktori Lain
from A_CSVParser import CSV_Parser
from A_Functions import *
from B01_Cipher import *
import A_Data as data

# Program UserUtils
# Berisi fungsi/prosedur untuk mempermudah pengolahan data user


def check_valid_username(username: str):
    """
    Fungsi yang mengecek apakah username yang dimasukkan adalah valid
    """

    # KAMUS LOKAL
    # char: str
    # user: int

    # ALGORITMA
    for char in username:
        # Jika ada karakter yang bukan huruf, angka, _ atau -, maka username tidak valid
        user = ord(char)
        if not (97 <= user <= 122 or 65 <= user <= 90 or 48 <= user <= 57 or char == "_" or char == "-"):
            return False
    return True

def is_username_available(username: str, data_user):
    """ Fungsi yang mengembalikan true apabila username yang dimasukkan tidak ada, false jika sudah ada """

    # KAMUS LOKAL
    # users: Data
    # user: BarisData
    a = length_manual(data_user)
    for i in range(a):
        for j in range(6):
            if username == data_user[i][1]:
                return True
    return False
    # ALGORITMA
    
            
def register(data_user):
    global data
    nama = input("Masukan nama: ")
    
    cek = False
    while cek == False:
        username = input("Masukan username: ")
        if not (is_username_available(username, data_user)) and check_valid_username(username) :
            password_asli = input("Masukan password: ")

            # Mengenkripsi password
            password_enkripsi = enkripsi(str(password_asli), data.PASSWORD_KEY)
            print('Username {} telah berhasil register ke dalam "BMO"'.format(username))
            cek = True
        elif (is_username_available(username,'database')):
            print('Usermane {} sudah terpakai, silahkan menggunakan username lain')
            cek == False
        else:
            print('Format Username Salah.')
            cek == False

    # Membuat baris untuk diappend ke dalam user.csv

    # Inisialisasi id, role, dan saldo
    id_user = str((length_manual(data_user)))
    role = 'User'
    saldo = str(0)

    # Baris data user
    data = [id_user, username, nama, password_enkripsi, role, saldo]
    # Memasukkan data ke array csv
    data_user = append_manual(data_user, data)

    return(data_user)

# ------- CONTOH PENGGUNAAN -------