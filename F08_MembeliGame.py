# Sabtu, 9 April 2022
# Catatan: 

# Mengimport Fungsi dari direktori lain
from A_CSVParser import *
from A_Functions import *
from F02_Register import *

# Membuat fungsi buy_game
def buy_game(id_user, data_game, data_riwayat, data_user, data_kepemilikan):
    # checking
    valid = False

    for i in range(length_manual(data_user)):
        if data_user[i][0] == id_user:
            role = data_user[i][4]
            break
    
    if is_admin(role):
        id_game_input = str(input("Masukkan ID Game: "))

        # Stok Game tersebut sedang habis!
        for i in range(1,length_manual(data_game)):
            if data_game[i][0] == id_game_input:
                nama_game = data_game[i][1]
                if int(data_game[i][5]) < 0:
                    print("Stok Game tersebut sedang habis!")
                    valid = False
                else: valid = True

        # Anda sudah memiliki Game tersebut!
        for i in range(1,length_manual(data_riwayat)):
            if data_riwayat[i][3] == id_user and data_game[i][0] == id_game_input:
                print("Anda sudah memiliki Game tersebut!")
                valid = False
            else: valid = True

        # Saldo anda tidak cukup untuk membeli game tersebut!
        for i in range(1,length_manual(data_game)):
            if data_game[i][0] == id_game_input:
                harga_game = int(data_game[i][4])
                break
        for i in range(1, length_manual(data_user)):
            if data_user[i][0] == id_user:
                saldo_user = int(data_user[i][5])
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


    # mengubah stok pada data_game
    panjang_game = length_manual(data_game)
    for i in range(panjang_game):
        if data_game[i][0] == id_game_input:
            data_game[i][5] = int(data_game[i][5]) - 1

    # menambah riwayat pada data riwayat
    item_riwayat = [id_game_input, nama_game, harga_game, id_user, '2022']
    data_riwayat = append_manual(data_riwayat,item_riwayat)

    # menambah kepemilikan pada data kepemilikan
    item_kepemilikan = [id_game_input, id_user]
    data_kepemilikan = append_manual(data_kepemilikan, item_kepemilikan)
    print(data_game)
    
    return (data_game,data_riwayat,data_kepemilikan)


# ------- CONTOH PENGGUNAAN -------
# buy_game(id_user, data.game, data.riwayat, data.user, data.kepemilikan)