# Tanggal
# Catatan

# Import bonus
from B01_Cipher import *
from B02_MagicConchShell import *
from B03_GameTictactoe import *

# Import setiap fitur
from F02_Register import *
from F03_Login import *
from F04_MenambahGamekeTokoGame import *
from F05_MengubahGamePadaToko import *
from F06_MengubahStok import *
from F07_ListingGame import *
from F08_MembeliGame import *
from F09_MelihatGameKu import *
from F10_MencariGamedariIDGamedanTahunRilis import *
from F11_MencariGamediToko import *
from F12_TopUpSaldo import *
from F13_MelihatRiwayatPembelian import *
from F14_Help import *
from F15_Load import *
from F16_Save import *
from F17_Exit import *

# Import data
import A_Data as data

# ========== MEMBUAT FUNGSI UTAMA ==============
def main():
    global data
    # Loading data
    if not load():
        return
    else:
        loggedin = False

        print("Jangan lupa! BNMO akan selalu membantumu dengan mengetik 'help'!")
        while not loggedin:
            perintah = str(input(">>> ")).lower()
            if perintah == 'help':
                help(0, data.user)
            elif perintah =='login':
                id_user = login(data.user)
                loggedin = True
            elif perintah == 'exit':
                exit(data.game, data.kepemilikan, data.riwayat, data.user)
                return()
        
        while loggedin:
            for i in range(length_manual(data.user)):
                if data.user[i][0] == id_user:
                    nama_user = data.user[i][2]
                    role_user = data.user[i][4]

            print(f"Mau melakukan apa, {nama_user}?")
            perintah = str(input(">>> ")).lower()
            
            # Fitur yang bisa dilakukan kedua role
            if perintah == "help":
                help(id_user, data.user)
            elif perintah == "list_game_toko":
                list_game_toko(data.game)
            elif perintah == "search_game_at_store":
                search_game_at_store(data.game)            
            elif perintah == "save":
                save(data.game, data.kepemilikan, data.riwayat, data.user)
            elif perintah == "exit":
                exit(data.game, data.kepemilikan, data.riwayat, data.user)          
                return()  
            

            # Fitur admin only
            elif role_user == "Admin":
                if perintah == "register":
                    data.user = register(data.user)
                elif perintah == "login":
                    id_user = login(data.user)
                elif perintah == "tambah_game":
                    data.game = tambah_game(data.game)
                elif perintah == "ubah_game":
                    data.game = ubah_data_game(data.game)
                elif perintah == "ubah_stok":
                    data.game = ubah_stok(data.game)
                elif perintah == "topup":
                    data.user = topup_saldo(data.user) 
                elif perintah == "buy_game" or perintah == "list_game" or perintah == "search_my_game" or perintah == "riwayat": 
                    print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                else: 
                    print("Maaf, mohon masukkan input yang valid.")
                    print("BNMO dapat selalu membantumu dengan fitur 'help'!")
            elif role_user == "User":
                if perintah == 'buy_game':
                    data = buy_game(id_user, data.game, data.riwayat, data.user, data.kepemilikan)
                    data.game = data[0]
                    data.riwayat = data[1]
                    data.kepemilikan = data[2]
                elif perintah == "list_game":
                    melihat_gameku(id_user, data.riwayat, data.game)
                elif perintah == "search my_game":
                    cek_id_game_dan_tahun_rilis(data.game, data.riwayat)
                elif perintah == "riwayat":
                    lihat_riwayat(data.riwayat)
                
if __name__ == "__main__":
    main()