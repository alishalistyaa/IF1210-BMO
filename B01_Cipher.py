# Selasa, 19 April 2022
# Catatan: 

# Mengimport library
from A_Functions import append_manual, length_manual

# Generating key
def generate_key(string, key):
    # KAMUS LOKAL
    # string, key: str

    key = list(key)
    key_string =''
    # Jika key yang diinput sudah sama
    if length_manual(string) == length_manual(key):
        return(key)
    else:
        for i in range(length_manual(string) - length_manual(key)):
            key = append_manual(key, key[i% length_manual(key)])
    # Looping mengubah key (list) menjadi str
    for i in key:
        key_string += i
    return(key_string)

def enkripsi(password_asli, masukan_key):
    # KAMUS LOKAL
    # password_asli, masukan_key : str (input)

    # key : str
    # temp : array
    # password_baru : str

    # ALGORITMA
    # Inisialisasi 
    key = generate_key(password_asli, masukan_key)
    temp = []
    password_baru =''
    # Looping untuk mengencrypt dan disimpan di temporary
    for i in range(length_manual(password_asli)):
        huruf = (ord(password_asli[i]) + ord(key[i])) % 26
        huruf += ord('A')
        temp = append_manual(temp, chr(huruf))
    # Mengubah temporary (list) menjadi string
    for i in (temp):
        password_baru += i
    return(password_baru)

def dekripsi(password_baru,masukan_key):
    # KAMUS LOKAL
    # password_baru, masukan_key : str (input)

    # key : str
    # temp : array
    # password_baru : str

    # ALGORITMA
    key = generate_key(password_baru, masukan_key)
    temp = []
    password_asli = ''
    # Looping untuk dekripsi dan disimpan di temporary
    for i in range(length_manual(password_baru)):
        huruf = (ord(password_baru[i]) - ord(key[i])+ 26) % 26
        huruf += ord('A')
        temp = append_manual(temp, chr(huruf))

    # Mengubah temporary (list) menjadi string
    for i in (temp):
        password_asli += i
    return(password_asli) 

# ------- CONTOH PENGGUNAAN ----------
# print(enkripsi("AbCdE","SJD"))
# print(dekripsi("AMKVZA","ALISHA"))