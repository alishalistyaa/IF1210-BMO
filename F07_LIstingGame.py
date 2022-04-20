# Sabtu, 9 April 2022
# Catatan: 

# Mengimport Fungsi dari direktori lain
from A_CSVParser import *
from A_DataFunctions import max_length
from A_Functions import *


array = CSV_Parser("database/game.csv")
arrayboongan = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], ['G001', 'Tetris', 'Puzzle', '1984', '170000', '4'], ['G002', 'Mario Kart Wii', 'Race', '1985', '48000', '5'], ['G003', 'Minecraft', 'Adventure', '2011', '176000', '6'], ['G004', 'Wii ', 'Sports', '2006', '83000', '7'], ['G005', 'Pubg', 'Battle', '2017', '5000', '8'], ['G006', 'Pokemon', 'Adventure', '1996', '47000', '11'], ['G007', 'Skyrim', 'Race', '2011', '30000', '13'], ['G008', 'Duck Hunt', 'Adventure', '1984', '28000', '15'], ['G009', 'Terraria', 'Puzzle', '2011', '27000', '17'], ['G010', 'Fifa 18', 'Sports', '2017', '24000', '18'], ['G011', 'Sonic', 'Race', '1991', '2400', '91'], ['G012', 'Kinect', 'Adventure', '2010', '27000', '19'], ['G013', 'Bonderlands', 'Adventure', '2012', '22000', '45'], ['G014', 'Frogger', 'Puzzle', '1981', '21000', '34'], ['G015', 'Lemmings', 'Battle', '1991', '20000', '25'], ['G016', 'Brain Age', 'Adventure', '2005', '19000', '36'], ['G017', 'The Sims ', 'Sports', '2000', '16000', '47'], ['G018', 'Mobile Legends', 'Battle', '2015', '13000', '54'], ['G019', 'Roblox', 'Puzzle', '2016', '12000', '67'], ['G020', 'Candy Crush', 'Puzzle', '2009', '28000', '49'], ['G021', 'Pou', 'Adventure', '2005', '50000', '43'], ['G022', 'Clash Of Clans', 'Battle', '2009', '10000', '46'], ['G023', 'Hay Day', 'Adventure', '2008', '21000', '45'], ['G024', 'Angry Bird', 'Sports', '2007', '9000', '44'], ['G025', 'Ball Pool', 'Sports', '2011', '38000', '82'], ['G026', 'Plants vs Zombie', 'Battle', '2010', '29000', '73'], ['G027', 'Real Racing', 'Race', '2019', '10100', '46'], ['G028', 'Farm Heroes', 'Puzzle', '2013', '31200', '52'], ['G029', 'Shadow Fight', 'Battle', '1997', '21450', '37'], ['G030', 'Looney Tunes Dash', 'Race', '2000', '50101', '51'], ['G031', 'Cut The Rope', 'Puzzle', '2003', '21800', '30'], ['G032', 'Death Rally', 'Race', '2014', '76400', '21'], ['G033', 'Naughty Kitties', 'Battle', '2018', '26500', '22'], ['G034', 'Farm Clan', 'Adventure', '2009', '53000', '26'], ['G035', 'Ragnarok', 'Battle', '2005', '10300', '41'], ['G036', 'Donkey Kong', 'Race', '1981', '8000', '67'], ['G037', 'Galaga', 'Adventure', '1981', '36000', '98'], ['G038', 'Pac Man', 'Adventure', '1982', '6500', '48'], ['G039', 'Contra', 'Battle', '1987', '8200', '86'], ['G040', 'Zelda', 'Adventure', '1987', '4700', '35'], ['G041', 'Mega Man', 'Battle', '1990', '3900', '89'], ['G042', 'Iechuks', 'Adventure', '1991', '4900', '94'], ['G043', 'Street Fighter', 'Battle', '1991', '5020', '15'], ['G044', 'Doom', 'Battle', '1993', '4800', '19'], ['G045', 'Tie Fighter', 'Battle', '1994', '33000', '58'], ['G046', 'Super Metroid', 'Adventure', '1994', '2400', '4'], ['G047', 'X Com', 'Adventure', '1994', '36490', '75'], ['G048', 'Chrono Trigger', 'Adventure', '1995', '19180', '18'], ['G049', 'Warcraft', 'Battle', '1995', '10980', '97'], ['G050', 'Undertale', 'Adventure', '2015', '12400', '91']]

# ALGORITMA

# Membuat fungsi memilih kolom mana yang disort
def pilih_kolom(array,pilihan):
    # KAMUS LOKAL
    # array         : matriks
    # pilihan       : string (header pada csv)
    # kolom_pilihan : array
    # i, j          : integer iterasi

    # Inisialisasi array kosong
    kolom_pilihan = []

    # Looping
    for i in range(length_manual(array[0])):
        if array[0][i] == pilihan:
            for j in range(length_manual(array)):
                kolom_pilihan = append_manual(kolom_pilihan, array[j][i])

    return(kolom_pilihan)

# Membuat fungsi membandingkan angka
def bandingkan_angka(array,kolom_pilihan,skema):
    panjang_array = length_manual(kolom_pilihan)

    # For loop untuk traversi semua elemen
    for i in range(panjang_array):
        for j in range(0, panjang_array-i-1):
            if skema[-1] == '+':
                if int(kolom_pilihan[j]) > int(kolom_pilihan[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
                    kolom_pilihan[j], kolom_pilihan[j+1] = kolom_pilihan[j+1], kolom_pilihan[j]
            else: # (skema[-1] == '-')
                if int(kolom_pilihan[j]) < int(kolom_pilihan[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
                    kolom_pilihan[j], kolom_pilihan[j+1] = kolom_pilihan[j+1], kolom_pilihan[j]
                
    return array

# Membuat fungsi membandingkan id
def bandingkan_id(array,kolom_pilihan,skema):
    array_id = []
    for i in range(length_manual(kolom_pilihan)):
        id_baru = ''
        temp = ((remove_manual(kolom_pilihan[i],0)))
        for i in temp:
            id_baru += i
        array_id = append_manual(array_id, id_baru)
    
    bandingkan_angka(array,array_id,skema)
    return array


# Membuat fungsi membandingkan huruf
def banding_2_kata(kata_satu, kata_dua):
    # Inisialisasi kata_satu dan dua
    panjang_kata_satu = length_manual(kata_satu)
    panjang_kata_dua = length_manual(kata_dua)

    kata_satu = (kata_satu).upper()
    kata_dua  = (kata_dua).upper() 

    urutan_beda = False
    if kata_satu == kata_dua :
        urutan_beda = False
    else:
        # Mencari limit untuk membandingkan
        # Misal ABE dibandingkan dengan ABCDE, limitnya pembandingnya 3
        if panjang_kata_satu < panjang_kata_dua:
            limit = panjang_kata_satu
        else: # panjang kata_satu > kata_dua
            limit = panjang_kata_dua

        # Membandingkan sampai alphabetnya berbeda
        for i in range(limit):
            if ord(kata_dua[i]) < ord(kata_satu[i]):
                urutan_beda = True
                break
            else : urutan_beda = False
        if i == limit-1 and length_manual(kata_dua) < length_manual(kata_satu):
           urutan_beda = True
    return urutan_beda

def bandingkan_huruf(array, kolom_pilihan,skema):
    panjang_array = length_manual(kolom_pilihan)
    for i in range(panjang_array):
        for j in range(0, panjang_array-i-1):

            if skema[-1] == '+':
                if banding_2_kata(kolom_pilihan[j], kolom_pilihan[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
                    kolom_pilihan[j], kolom_pilihan[j+1] = kolom_pilihan[j+1], kolom_pilihan[j]
            
            if skema[-1] == '-':
                if not(banding_2_kata(kolom_pilihan[j], kolom_pilihan[j+1])):
                    array[j], array[j+1] = array[j+1], array[j]
                    kolom_pilihan[j], kolom_pilihan[j+1] = kolom_pilihan[j+1], kolom_pilihan[j]

    return array
# ======================================================
    
def list_game_toko(array):
    # Menginput jenis skema
    skema = str(input("Masukkan skema: ")).lower()
    array_tanpa_header = remove_manual(array,0)

    # Menentukan kolom mana yang disort
    if 'id' in skema:
        nama_kategori = "id"
        tipe_data = "id"
    elif 'nama' in skema:
        nama_kategori = "nama"
        tipe_data = "huruf"
    elif 'kategori' in skema:
        nama_kategori = "kategori"
        tipe_data = "huruf"
    elif ('tahun_rilis' in skema) or ('tahunrilis' in skema):
        nama_kategori = "tahun_rilis"
        tipe_data = "angka"
    elif 'harga' in skema:
        nama_kategori = "harga"  
        tipe_data = "angka"
    elif 'stok' in skema:
        nama_kategori = "stok"
        tipe_data = "angka"
    elif skema == '\n':
        nama_kategori = "id"
        skema = 'id+'
        tipe_data = "id"
    else: 
        return(print("Skema sorting tidak valid!"))
        

    kolom_pilihan = remove_manual(pilih_kolom(array, nama_kategori),0)

    if tipe_data == "angka":
        sorted_array = bandingkan_angka(array_tanpa_header, kolom_pilihan,skema)
    elif tipe_data == "huruf":
        sorted_array = bandingkan_huruf(array_tanpa_header, kolom_pilihan,skema)
    elif tipe_data == "id":
        sorted_array = bandingkan_id(array_tanpa_header,kolom_pilihan,skema)

    # Mengeprint array

    # Mencari maksimum dari setiap kolom
    # game id apsti 4 digit
    max_nama = max_length(sorted_array,1)
    if max_nama < (length_manual('NAMA')):
        max_nama = 4

    max_kategori = max_length(sorted_array,2)
    if max_kategori < (length_manual('KATEGORI')):
        max_kategori = 8
    # tahun rilis pasti 9 digit 

    max_harga = max_length(sorted_array,4)
    if max_harga < (length_manual('HARGA')):
        max_harga = 5
    
    max_nomor = (length_manual(array) % 10) + 1
    
    

    print(f"   ID   | NAMA{' '*(max_nama-4)} | KATEGORI{' '*(max_kategori-8)} | TAHUN RILIS | HARGA{' '*(max_harga-5)} | STOK")
    print('----------------------------------------------------------')
    for i in range(length_manual(sorted_array)):
        spasi_nama = ' '*(max_nama-length_manual(sorted_array[i][1]))
        spasi_kategori = ' '*(max_kategori-length_manual(sorted_array[i][2]))
        spasi_harga = ' '*(max_harga-length_manual(sorted_array[i][4]))
        spasi_nomor = ' '*(max_nomor-length_manual(str(i+1)))
        print(f"{spasi_nomor}{i+1}. {sorted_array[i][0]} | {sorted_array[i][1]}{spasi_nama} | {sorted_array[i][2]}{spasi_kategori} | {sorted_array[i][3]}{' '* 7} | {sorted_array[i][4]}{spasi_harga} | {sorted_array[i][5]}")
    
    return sorted_array

list_game_toko(array)
# print(remove_manual(pilih_kolom(array, 'nama'),0))

# print(bandingkan_huruf([['G001', 'A', 'A', '2000', '15', '1'], ['G004', 'D', 'D', '200033', '3', '20'], ['G003', 'C', 'C', '2000', '2', '10'], ['G002', 'B', 'B', '2000', '1', '5']], ['A','D','C','B'],'nama+'))