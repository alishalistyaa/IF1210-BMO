# Sabtu, 9 April 2022
# Catatan: 

# Mengimport Fungsi dari direktori lain
from A_CSVParser import *
from A_Functions import *

# Membuat fungsi buy_game
def buy_game(id_user):
    id_game = str(input("Masukkan ID Game: "))

    data_game = CSV_Parser("database/game.csv")
    data_riwayat = CSV_Parser("database/riwayat.csv")
    data_user = CSV_Parser("database/user.csv")
    valid = False

    # Stok Game tersebut sedang habis!
    for i in range(1,length_manual(data_game)):
        if data_game[i][0] == id_game:
            nama_game = data_game[i][1]
            if data_game[i][5] < 0:
                print("Stok Game tersebut sedang habis!")
                valid = False
            else: valid = True

    # Anda sudah memiliki Game tersebut!
    for i in range(1,length_manual(data_riwayat)):
        if data_riwayat[i][3] == id_user and data_game[i][0] == id_game:
            print("Anda sudah memiliki Game tersebut!")
            valid = False
        else: valid = True

    # Saldo anda tidak cukup untuk membeli game tersebut!
    for i in range(1,length_manual(data_game)):
        if data_game[i][0] == id_game:
            harga_game = data_game[i][4]
            break
    for i in range(1, length_manual(data_user)):
        if data_user[i][1] == id_user:
            saldo_user = data_user[i][5]
            break

    if harga_game > saldo_user:
        print("Saldo anda tidak cukup untuk membeli game tersebut!")
        valid = False
    else: valid = True

    # Game "Nama Game" berhasil dibeli!
    if valid:
        print(f"Game {nama_game} berhasil dibeli!")
        saldo_user = saldo_user - harga_game
    else: pass

    return 
