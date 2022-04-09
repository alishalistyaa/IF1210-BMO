# Sabtu, 9 April 2022
# Catatan:
# Karena ada beberapa fungsi yang tidak diperbolehkan,
# Maka dibuat fungsi-fungsi ini untuk membantu

# Membuat fungsi len() secara manual
def length_manual(list):
    # KAMUS LOKAL
    # list : list
    # length : int

    # ALGORITMA
    # Inisialisasi panjang list = 0
    length = 0                  
    # Looping sebanyak list
    for i in (list):
        length += 1

    return length

# ------ CONTOH PENGGUNAAN --------
# -> length_manual('aaaa')
# -> 4

# Membuat fungsi append() secara manual
def append_manual(list_awal, item_baru):
    # KAMUS LOKAL
    # list_awal : list
    # item_baru : str, int, float, list
    # length_list_awal, indeks_terakhir : int
    # list_baru : list

    # ALGORITMA
    # Mengetahui panjang list awal
    length_list_awal = length_manual(list_awal)

    # Inisialiasi list kosong
    # Panjangnya length_list_awal + 1 karena mau di append
    list_baru = [0 for i in range(length_list_awal + 1)]
    # Input list awal
    for i in range(length_list_awal):
        list_baru[i] = list_awal[i]
    # Menambahkan item baru
    indeks_terakhir = length_list_awal
    list_baru[indeks_terakhir] = item_baru
    
    return list_baru

# ------ CONTOH PENGGUNAAN --------
# -> append_manual(['a', 'b', 'c'], ['1', '2', '3'])
# -> ['a', 'b', 'c', ['1', '2', '3']]

# Membuat fungsi split() secara manual
def split_manual(list_awal, pemisah):
    # KAMUS LOKAL
    # List_awal : list

    # ALGORITMA
    # Inisialisasi list baru kosong dan item kosong
    list_baru = []
    item = ''
    # Mengolah item tersebut
    for i in list_awal:
        if i == pemisah:
            list_baru = append_manual(list_baru,item)   # Jika bertemu dengan pemisah, maka menambahkan item ke list baru
            item = ''                                   # Setelah ditambahkan, reset item agar bisa memulai item lain
        else:
            item += i                                   # Jika belum bertemu pemisah, menambahkan string ke item

    # Menambahkan item terakhir
    list_baru = append_manual(list_baru,item)

    return(list_baru)

# ------ CONTOH PENGGUNAAN --------
# (split_manual('abcd;efgh;ijkl', ';'))
# 'abcd;efgh;ijkl' sebagai list_awal dan ' ; ' sebagai pemisah
# -> ['abcd', 'efgh', 'ijkl']