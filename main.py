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

# Import pemanis
from A_Pemanis import *

# ========== MEMBUAT FUNGSI UTAMA ==============
def main():
    global data
    # Loading data
    if not load():
        return
    else:
        animatedbmo_start(folder_start)
        loggedin = False
        print('\nLoading...')
        print('Selamat datang di antarmuka "Binomo"!')
        print("\nJangan lupa! BNMO akan selalu membantumu dengan mengetik 'help'!")
        while not loggedin:
            perintah = str(input("\n>>> ")).lower()
            if perintah == 'help':
                help(0, data.user)
            elif perintah =='login':
                id_user = login(data.user)
                loading()
                if id_user != 9999:
                    loggedin = True
                else: print("Silahkan login kembali.")
            elif perintah == 'exit':
                exit(data.game, data.kepemilikan, data.riwayat, data.user)
                return()
            else:
                print("Maaf! Anda harus login terlebih dahulu untuk mengirim perintah selain login!")
        
        while loggedin:
            for i in range(length_manual(data.user)):
                if data.user[i][0] == id_user:
                    username = data.user[i][1]
                    nama_user = data.user[i][2]
                    role_user = data.user[i][4]
                    

            print(f"\nApa yang akan kita lakukan, {nama_user}?")
            perintah = str(input(">>> ")).lower()
            
            # Fitur yang bisa dilakukan kedua role
            if perintah == "help":
                help(id_user, data.user)
            elif perintah == "urutkan_game":
                loading()
                list_game_toko(data.game)
            elif perintah == "login":
                id_user = login(data.user)
                loading()
            elif perintah == "cari_game":
                search_game_at_store(data.game)            
            elif perintah == "save":
                loading()
                save(data.game, data.kepemilikan, data.riwayat, data.user)
            elif perintah == "minigames":
                print('''
                1 ) 'kerangajaib'
                Tanyakan pertanyaanmu ke KerangAjaib!

                2 ) 'tictactoe'
                Bermain tictactoe,, minum coklat panas,, menyusun puzzle,,

                ''')
            elif perintah == "kerangajaib":
                kerangajaib()
            elif perintah == "tictactoe":
                tictactoe()
            elif perintah == "exit":
                exit(data.game, data.kepemilikan, data.riwayat, data.user)          
                return()  
            

            # Fitur admin only
            elif role_user == "Admin":
                if perintah == "register":
                    data.user = register(data.user)
                elif perintah == "tambah_game":
                    data.game = tambah_game(data.game)
                elif perintah == "ubah_game":
                    data.game = ubah_data_game(data.game)
                elif perintah == "ubah_stok":
                    data.game = ubah_stok(data.game)
                elif perintah == "topup":
                    data.user = topup_saldo(data.user) 
                elif perintah == "beli_game" or perintah == "gameku" or perintah == "cari_gameku" or perintah == "riwayat": 
                    print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
                else: 
                    print("Maaf, mohon masukkan input yang valid.")
                    print("BNMO dapat selalu membantumu dengan fitur 'help'!")
            elif role_user == "User":
                if perintah == 'beli_game':
                        temp_data = buy_game(id_user, data.game, data.riwayat, data.user, data.kepemilikan)
                        if temp_data == None:
                            pass
                        else:
                            data.game = temp_data[0]
                            data.riwayat = temp_data[1]
                            data.kepemilikan = temp_data[2]
                elif perintah == "gameku":
                    melihat_gameku(id_user, data.riwayat, data.game)
                elif perintah == "cari_gameku":
                    cek_id_game_dan_tahun_rilis(data.game, data.riwayat,data.kepemilikan,data.user,username)
                elif perintah == "riwayat":
                    lihat_riwayat(data.riwayat, id_user)
                elif perintah == "register" or perintah == "tambah_game" or perintah == "ubah_game" or perintah == "ubah_stok" or perintah == "topup":
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
                else:
                    print("Maaf, mohon masukkan input yang valid.")
                    print("BNMO dapat selalu membantumu dengan fitur 'help'!")
                
if __name__ == "__main__":
    main()