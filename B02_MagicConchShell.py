# Senin, 11 April 2022
# Catatan: 

# Mengimport library
import time
from A_Functions import *

# Membuat random number
def randomnumber(minimum, maximum):
    # KAMUS LOKAL
    # now       : str
    # rnd       : real
    # randomnum : int

    # ALGORITMA
    now = str(time.perf_counter())
    rnd = float(now[::-1][:3:])/10
    randomnum  = round(minimum+ rnd*(maximum-minimum))
    return randomnum

# Membuat kerang ajaib
def kerangajaib():
    # KAMUS LOKAL
    # randomnum : int

    # ALGORITMA
    # Bertanya
    pertanyaan = str(input("Mau tanya apa? "))
    # Memanggil fungsi Random Number
    randomnum = randomnumber(1,length_manual(pertanyaan))

    # Menjawab berdasarkan random number
    if randomnum%11 == 0:
        print("Tentunya.")
    elif randomnum%7 == 0:
        print("Ya.")
    elif randomnum %5 == 0:
        print("Tidak.")
    elif randomnum %3 == 0:
        print("Bisa jadi.")
    elif randomnum %2 == 0:
        print("Mungkin.")
    else: print("Tidak mungkin.")

# ---- CONTOH PENGGUNAAN -----
# kerangajaib()