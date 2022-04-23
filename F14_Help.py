# Program - F14 Help
# Program Memerlukan file User yang berisi data user
# Akses - Admin dan User

from A_Functions import *

def help (user_id, data_user): 
    # Mencari Role berdasarkan user_id
    for i in range (length_manual(data_user)): 
        if data_user[i][0] == user_id:
            role = data_user[i][4]
            break
        else: role = ''

    if role == "Admin" : #Jika role adalah Admin, maka akan ditampilkan help yang cukup jelas dengan akses yang bersesuaian dengan admin
        print("""
             ============ BMNO HELP ============
┌-------------------------------------------------------------------┑
| NO |    COMMAND      |                   FUNGSI                   |
|-------------------------------------------------------------------|
|  1. | register       |  Melakukan registrasi user baru            |
|  2. | login          |  Melakukan login ke dalam sistem           |
|  3. | tambah_game    |  Menambah game yang dijual pada toko       |
|  4. | ubah_game      |  Mengubah game pada toko game              |
|  5. | ubah_stok      |  Mengubah stok sebuah game pada toko       |
|  6. | urutkan_game   |  Melihat list game yang dijual pada toko   |
|  7. | cari_game      |  Mencari game di Toko dari ID, nama game,  |
|     |                |    harga, kategori dan tahun rilis         |
|  8. | topup          |  Menambahkan saldo kepada user             |
|  9. | help           |  Memberikan panduan penggunaan sistem      |
| 10. | save           |  Melakukan penyimpanan data ke dalam file  |
|     |                |       setelah dilakukan perubahan          |
| 11. | exit           |  Keluar dari aplikasi                      |
┗-------------------------------------------------------------------┘
✩ Mohon untuk mengetikkan command, dan bukan nomor, ya! ✩ """)

    elif role == "User": #Jika role adalah User, maka akan ditampilkan help yang cukup jelas dengan akses yang bersesuaian dengan User
        print ("""
             ============ BMNO HELP ============
┌-------------------------------------------------------------------┑
| NO |    COMMAND      |                   FUNGSI                   |
|-------------------------------------------------------------------|
|  1. | login          |  Melakukan login ke dalam sistem           |
|  2. | urutkan_game   |  Melihat list game yang dijual pada toko   |
|  3. | beli_game      |  Membeli game                              |
|  4. | gameku         |  Melihat game yang dimiliki user           |
|  5. | cari_gameku    |  Mencari game yang dimiliki user           |
|     |                |     dari ID dan tahun rilis                |
|  6. | cari_game      |  Mencari game di Toko dari ID, nama game,  |
|     |                |    harga, kategori dan tahun rilis         |
|  7. | riwayat        |  Melihat riwayat pembelian                 |
|  8. | help           |  Memberikan panduan penggunaan sistem      |
|  9. | save           |  Melakukan penyimpanan data ke dalam file  |
|     |                |       setelah dilakukan perubahan          |
| 10. | exit           |  Keluar dari aplikasi                      |
┗-------------------------------------------------------------------┘ 
✩ Mohon untuk mengetikkan command, dan bukan nomor, ya! ✩ """)

    else :
        print ("""
             ============ BMNO HELP ============
┌-------------------------------------------------------------------┑
| NO |    COMMAND      |                   FUNGSI                   |
|-------------------------------------------------------------------|
|  1. | login          |  Melakukan login ke dalam sistem           |
|  2. | help           |  Memberikan panduan penggunaan sistem      |
|  3. | exit           |  Keluar dari aplikasi                      |
┗-------------------------------------------------------------------┘ 
✩ Mohon untuk mengetikkan command, dan bukan nomor, ya! ✩""")

    return

