   
from A_CSVParser import CSV_Parser
from A_Functions import *

# Program UserUtils
# Berisi fungsi/prosedur untuk mempermudah pengolahan data user

PASSWORD_STANDARD = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|':,./<>?`~\\ "
PASSWORD_KEY = "5@OR3A.wT<7&/zcIk(}J+)o_=%eChdKH m6[]jYQ4n?qPUy0M8a$uX~Fs9{bSGx:`f#-!1glWZ>*VLp\\E,rB'i^NDv|2t"
PASSWORD_LENGTH = length_manual(PASSWORD_STANDARD)


def is_admin(role):
    """ Fungsi yang mengembalikan true apabila role user adalah admin, false jika bukan """

    # ALGORITMA
    if role == "Admin":
        return True
    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    return False


def is_user(role):
    """ Fungsi yang mengembalikan true apabila role user adalah user, false jika bukan """

    # ALGORITMA
    if role == "User":
        return True
    print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    return False


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
    nama = input("Masukan nama: ")
    
    cek = False
    while cek == False:
        username = input("Masukan username: ")
        if not (is_username_available(username, 'database')) and check_valid_username(username) :
            password = input("Masukan password: ")
            print('Username {} telah berhasil register ke dalam "Binomo"'.format(username))
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
    data = [id_user, username, nama, password, role, saldo]
    # Memasukkan data ke array csv
    data_user = append_manual(data_user, data)

    return(data_user)

# ------- CONTOH PENGGUNAAN -------
# register('data.user')
