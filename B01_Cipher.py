# Selasa, 19 April 2022
# Catatan: 

# Mengimport library
from A_Functions import append_manual, length_manual
import A_Data as data

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
        posisi_ascii = ord(password_asli[i])
        # Untuk huruf kapital, huruf kecil, dan angka
        if posisi_ascii >= 65 and posisi_ascii <=90:
            huruf = (posisi_ascii-65 + ord(key[i]))% 26 
            huruf += ord('A')
        elif posisi_ascii >= 97 and posisi_ascii <=122:
            huruf = (posisi_ascii-97 + ord(key[i])) % 26
            huruf += ord('a')    
        elif posisi_ascii >= 48 and posisi_ascii <=57:
            huruf = (posisi_ascii-48 + ord(key[i])) % 10
            huruf += ord('0')   

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
        posisi_ascii = ord(password_baru[i])

       # Untuk huruf kapital, huruf kecil, dan angka
        if posisi_ascii >= 65 and posisi_ascii <=90:
            huruf = (posisi_ascii - ord(key[i])-65) % 26
            huruf += ord('A')
        elif posisi_ascii >= 97 and posisi_ascii <=122:
            huruf = (posisi_ascii - ord(key[i])-97) % 26
            huruf += ord('a')    
        elif posisi_ascii >= 48 and posisi_ascii <=57:
            huruf = (posisi_ascii - ord(key[i])-48) % 10
            huruf += ord('0') 

        temp = append_manual(temp, chr(huruf))
    # Mengubah temporary (list) menjadi string
    for i in (temp):
        password_asli += i
    return(password_asli) 

# ------- CONTOH PENGGUNAAN ----------
#print(enkripsi("alisha220303",data.PASSWORD_KEY))
#print(dekripsi("567",data.PASSWORD_KEY))