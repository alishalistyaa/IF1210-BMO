# Selasa, 12 April 2022
# Catatan : Prosedur ini adalah prosedur untuk memberikan panduan penggunaan sistem.

from A_Functions import *

def help (user_id, data_user): 
    # Mencari Role berdasarkan user_id
    for i in range (length_manual(data_user)): 
        if data_user[i][0] == user_id:
            role = data_user[i][4]
            break
        else: role = ''

    if role == "Admin" : #Jika role adalah Admin, maka akan ditampilkan help yang cukup jelas dengan akses yang bersesuaian dengan admin
        print("""============ HELP ============
1. register - Untuk melakukan registrasi user baru
2. login - Untuk melakukan login ke dalam sistem
3. tambah_game - Untuk menambah game yang dijual pada toko
4. ubah_game - Untuk mengubah game pada toko game
5. ubah_stok - Untuk mengubah stok sebuah game pada toko
6. list_game_toko - Untuk melihat list game yang dijual pada toko
7. search_game_at_store - Untuk mencari game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis 
8. topup - Untuk menambahkan saldo kepada user (Top Up Saldo)
9. help - Untuk memberikan panduan penggunaan sistem
10. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
11. exit - Untuk keluar dari aplikasi""")

    elif role == "User": #Jika role adalah User, maka akan ditampilkan help yang cukup jelas dengan akses yang bersesuaian dengan User
        print ("""============ HELP ============
1. login - Untuk melakukan login ke dalam sistem
2. list_game_toko - Untuk melihat list game yang dijual pada toko
3. buy_game - Untuk membeli game
4. list_game - Untuk melihat game yang dimiliki user
5. search_my_game - Untuk mencari game yang dimiliki user dari ID dan tahun rilis
6. search_game_at_store - Untuk mencari game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis 
7. riwayat - Untuk melihat riwayat pembelian
8. help - Untuk memberikan panduan penggunaan sistem
9. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan
10. exit - Untuk keluar dari aplikasi""")

    else :
        print ("""============ HELP ============
1. login - Untuk melakukan login ke dalam sistem
2. exit - Untuk keluar dari aplikasi""")

    return

