# 18 April 2022
# Catatan:

# Mengimport library
import os
from A_Functions import *

def array_to_csv(array):
    # KAMUS LOKAL
    # array : matriks
    # data, header : str

    # ALGORITMA
    # Inisialisasi data pertama = kosong
    data = ''
    # melakukan .join manual
    for i in range(length_manual(array)):
        for j in range(length_manual(array[i])):
            data += str(array[i][j])
            # jika sudah di akhir baris tidak udah ada ;
            if j != (length_manual(array)-1): 
                data += ';'
        # jika sudah di akhir baris, make a new line
        data += "\n"
    return(data)

def pilih_folder(nama_folder):

    # checking folder
    path = os.getcwd() + '/' + nama_folder

    # Jika folder sudah ada
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return

def write_file(data_array,nama_folder, nama_file):
    f = open(nama_folder+'/'+nama_file, "w")
    f.write(array_to_csv(data_array))
    f.close()

def save(data_game, data_kepemilikan, data_riwayat, data_user):
    nama_folder = str(input("Masukkan nama folder penyimpanan: "))
    pilih_folder(nama_folder)

    # Inisialisasi write folder 
    write_file(data_game,nama_folder,'game.csv')
    write_file(data_kepemilikan,nama_folder,'kepemilikan.csv')
    write_file(data_riwayat,nama_folder,'riwayat.csv')
    write_file(data_user,nama_folder,'user.csv')

    print("Saving...")
    print(f"Data telah disimpan pada folder {nama_folder}!")


# arraygame = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], ['G001', 'Tetris', 'Puzzle', '1984', '170000', '4'], ['G002', 'Mario Kart Wii', 'Race', '1985', '48000', '5'], ['G003', 'Minecraft', 'Adventure', '2011', '176000', '6'], ['G004', 'Wii ', 'Sports', '2006', '83000', '7'], ['G005', 'Pubg', 'Battle', '2017', '5000', '8'], ['G006', 'Pokemon', 'Adventure', '1996', '47000', '11'], ['G007', 'Skyrim', 'Race', '2011', '30000', '13'], ['G008', 'Duck Hunt', 'Adventure', '1984', '28000', '15'], ['G009', 'Terraria', 'Puzzle', '2011', '27000', '17'], ['G010', 'Fifa 18', 'Sports', '2017', '24000', '18'], ['G011', 'Sonic', 'Race', '1991', '2400', '91'], ['G012', 'Kinect', 'Adventure', '2010', '27000', '19'], ['G013', 'Bonderlands', 'Adventure', '2012', '22000', '45'], ['G014', 'Frogger', 'Puzzle', '1981', '21000', '34'], ['G015', 'Lemmings', 'Battle', '1991', '20000', '25'], ['G016', 'Brain Age', 'Adventure', '2005', '19000', '36'], ['G017', 'The Sims ', 'Sports', '2000', '16000', '47'], ['G018', 'Mobile Legends', 'Battle', '2015', '13000', '54'], ['G019', 'Roblox', 'Puzzle', '2016', '12000', '67'], ['G020', 'Candy Crush', 'Puzzle', '2009', '28000', '49'], ['G021', 'Pou', 'Adventure', '2005', '50000', '43'], ['G022', 'Clash Of Clans', 'Battle', '2009', '10000', '46'], ['G023', 'Hay Day', 'Adventure', '2008', '21000', '45'], ['G024', 'Angry Bird', 'Sports', '2007', '9000', '44'], ['G025', 'Ball Pool', 'Sports', '2011', '38000', '82'], ['G026', 'Plants vs Zombie', 'Battle', '2010', '29000', '73'], ['G027', 'Real Racing', 'Race', '2019', '10100', '46'], ['G028', 'Farm Heroes', 'Puzzle', '2013', '31200', '52'], ['G029', 'Shadow Fight', 'Battle', '1997', '21450', '37'], ['G030', 'Looney Tunes Dash', 'Race', '2000', '50101', '51'], ['G031', 'Cut The Rope', 'Puzzle', '2003', '21800', '30'], ['G032', 'Death Rally', 'Race', '2014', '76400', '21'], ['G033', 'Naughty Kitties', 'Battle', '2018', '26500', '22'], ['G034', 'Farm Clan', 'Adventure', '2009', '53000', '26'], ['G035', 'Ragnarok', 'Battle', '2005', '10300', '41'], ['G036', 'Donkey Kong', 'Race', '1981', '8000', '67'], ['G037', 'Galaga', 'Adventure', '1981', '36000', '98'], ['G038', 'Pac Man', 'Adventure', '1982', '6500', '48'], ['G039', 'Contra', 'Battle', '1987', '8200', '86'], ['G040', 'Zelda', 'Adventure', '1987', '4700', '35'], ['G041', 'Mega Man', 'Battle', '1990', '3900', '89'], ['G042', 'Iechuks', 'Adventure', '1991', '4900', '94'], ['G043', 'Street Fighter', 'Battle', '1991', '5020', '15'], ['G044', 'Doom', 'Battle', '1993', '4800', '19'], ['G045', 'Tie Fighter', 'Battle', '1994', '33000', '58'], ['G046', 'Super Metroid', 'Adventure', '1994', '2400', '4'], ['G047', 'X Com', 'Adventure', '1994', '36490', '75'], ['G048', 'Chrono Trigger', 'Adventure', '1995', '19180', '18'], ['G049', 'Warcraft', 'Battle', '1995', '10980', '97'], ['G050', 'Undertale', 'Adventure', '2015', '12400', '91']]
# arraykepemilikan = [['game_id', 'user_id'], ['G001', '1'], ['G002', '2'], ['G003', '3'], ['G004', '4'], ['G005', '5'], ['G006', '6'], ['G007', '7'], ['G008', '8'], ['G009', '9'], ['G010', '10'], ['G011', '1'], ['G012', '2'], ['G013', '3'], ['G014', '4'], ['G015', '5'], ['G016', '6'], ['G017', '7'], ['G018', '8'], ['G019', '9'], ['G020', '10'], ['G021', '1'], ['G022', '2'], ['G023', '3'], ['G024', '4'], ['G025', '5'], ['G026', '6'], ['G027', '7'], ['G028', '8'], ['G029', '9'], ['G030', '10'], ['G031', '1'], ['G032', '2'], ['G033', '3'], ['G034', '4'], ['G035', '5'], ['G036', '6'], ['G037', '7'], ['G038', '8'], ['G039', '9'], ['G040', '10'], ['G041', '1'], ['G042', '2'], ['G043', '3'], ['G044', '4'], ['G045', '5'], ['G046', '6'], ['G047', '7'], ['G048', '8'], ['G049', '9'], ['G050', '10']]
# arrayriwayat = [['game_id', 'nama', 'harga', 'user_id', 'tahun_beli'], ['G001', 'Tetris', '170000', '1', '1990'], ['G002', 'Mario Kart Wii', '48000', '2', '1992'], ['G003', 'Minecraft', '176000', '3', '2013'], ['G004', 'Wii ', '83000', '4', '2010'], ['G005', 'Pubg', '5000', '5', '2021'], ['G006', 'Pokemon', '47000', '6', '1998'], ['G007', 'Skyrim', '30000', '7', '2016'], ['G008', 'Duck Hunt', '28000', '8', '1987'], ['G009', 'Terraria', '27000', '9', '2019'], ['G010', 'Fifa 18', '24000', '10', '2020'], ['G011', 'Sonic', '2400', '1', '2000'], ['G012', 'Kinect', '27000', '2', '2015'], ['G013', 'Bonderlands', '22000', '3', '2020'], ['G014', 'Frogger', '21000', '4', '1993'], ['G015', 'Lemmings', '20000', '5', '1999'], ['G016', 'Brain Age', '19000', '6', '2009'], ['G017', 'The Sims ', '16000', '7', '2002'], ['G018', 'Mobile Legends', '13000', '8', '2019'], ['G019', 'Roblox', '12000', '9', '2017'], ['G020', 'Candy Crush', '28000', '10', '2010'], ['G021', 'Pou', '50000', '1', '2008'], ['G022', 'Clash Of Clans', '10000', '2', '2011'], ['G023', 'Hay Day', '21000', '3', '2009'], ['G024', 'Angry Bird', '9000', '4', '2012'], ['G025', 'Ball Pool', '38000', '5', '2014'], ['G026', 'Plants vs Zombie', '29000', '6', '2016'], ['G027', 'Real Racing', '10100', '7', '2022'], ['G028', 'Farm Heroes', '31200', '8', '2014'], ['G029', 'Shadow Fight', '21450', '9', '1998'], ['G030', 'Looney Tunes Dash', '50101', '10', '2005'], ['G031', 'Cut The Rope', '21800', '1', '2007'], ['G032', 'Death Rally', '76400', '2', '2018'], ['G033', 'Naughty Kitties', '26500', '3', '2020'], ['G034', 'Farm Clan', '53000', '4', '2011'], ['G035', 'Ragnarok', '10300', '5', '2009'], ['G036', 'Donkey Kong', '8000', '6', '1986'], ['G037', 'Galaga', '36000', '7', '1996'], ['G038', 'Pac Man', '6500', '8', '1983'], ['G039', 'Contra', '8200', '9', '1989'], ['G040', 'Zelda', '4700', '10', '1999'], ['G041', 'Mega Man', '3900', '1', '1194'], ['G042', 'Lechuks', '4900', '2', '1995'], ['G043', 'Street Fighter', '5020', '3', '1998'], ['G044', 'Doom', '4800', '4', '2001'], ['G045', 'Tie Fighter', '33000', '5', '2003'], ['G046', 'Super Metroid', '2400', '6', '2006'], ['G047', 'X Com', '36490', '7', '2008'], ['G048', 'Chrono Trigger', '19180', '8', '2003'], ['G049', 'Warcraft', '10980', '9', '2004'], ['G050', 'Undertale', '12400', '10', '2021']]
# arrayuser = [['id', 'username', 'nama', 'password', 'role', 'saldo'], ['1', 'Vina', 'Nana', '123', 'Admin', '1000000'], ['2', 'Alisha', 'Shasha', '456', 'User', '7800000'], ['3', 'Listya', 'Yaya', '111', 'User', '3400000'], ['4', 'Gibran', 'Raran', '222', 'Admin', '2500000'], ['5', 'Dastin', 'Asti', '888', 'User', '2800000'], ['6', 'Fauzi', 'Auzi', '798', 'Admin', '4390000'], ['7', 'Bahtiar', 'Tiar', '834', 'Admin', '6330000'], ['8', 'Vivin', 'Devina', '647', 'User', '4090000'], ['9', 'Wardhani', 'Wani', '918', 'Admin', '5980000'], ['10', 'Dino', 'Nono', '210', 'User', '6000000']]

#save(arraygame,arraykepemilikan,arrayriwayat,arrayuser)