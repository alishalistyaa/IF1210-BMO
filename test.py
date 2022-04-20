from A_CSVParser import *
from A_Functions import *

array = CSV_Parser("database/game.csv")

def kolom(array, namaKategori):
#mengembalikan satu kolom berdasarkan kategori array
    arrayKolom = [0 for i in array]

    for i in range(len(array)):
        arrayKolom[i] = array[i][kodeKategori(array, namaKategori)]
        
    return arrayKolom


def kodeKategori(array, namaKategori):
#mengembalikan index kategori berdasarkan namanya
    for i in range(len(array[0])):
        if namaKategori == array[0][i]:
            markerKategori = i

    return markerKategori

    

def kalimat2Lebih(kalimat1, kalimat2):
#True kalau kalimat2 harus keluar lebih awal dari kalimat1
    ya = False
    if kalimat1 == kalimat2:
        ya = False
    else:
        if len(kalimat1) > len(kalimat2):
            limit = len(kalimat2)
        else:
            limit = len(kalimat1)
        
        for i in range(limit):
            mentok = False
            if i == limit - 1:
                mentok = True

            if (ord(kalimat1[i]) >= 65 and ord(kalimat1[i]) <= 90) or (ord(kalimat1[i]) - 32 >= 65 and ord(kalimat1[i]) - 32 <= 90):
                if (ord(kalimat1[i]) - 32 >= 65 and ord(kalimat1[i]) - 32 <= 90):
                    urutan1 = ord(kalimat1[i]) - 32
                else:
                    urutan1 = ord(kalimat1[i])

                if (ord(kalimat2[i]) >= 65 and ord(kalimat2[i]) <= 90) or (ord(kalimat2[i]) - 32 >= 65 and ord(kalimat2[i]) - 32 <= 90):
                    if (ord(kalimat2[i]) - 32 >= 65 and ord(kalimat2[i]) - 32 <= 90):
                        urutan2 = ord(kalimat2[i]) - 32
                    else:
                        urutan2 = ord(kalimat2[i])

                    if urutan2 < urutan1:
                        ya = True
                        break
                    elif urutan2 > urutan1:
                        ya = False
                        break
                    else:
                        pass
                    
                else:
                    ya = True
                    break
            
            elif (ord(kalimat1[i]) >= 48 and ord(kalimat1[i]) <= 57):
                if (ord(kalimat2[i]) >= 65 and ord(kalimat2[i]) <= 90) or (ord(kalimat2[i]) - 32 >= 65 and ord(kalimat2[i]) - 32 <= 90):
                    ya = False
                    break
                elif (ord(kalimat2[i]) >= 48 and ord(kalimat2[i]) <= 57):

                    if ord(kalimat1[i]) > ord(kalimat2[i]):
                        ya = True
                        break
                    elif ord(kalimat1[i]) < ord(kalimat2[i]):
                        ya = False
                        break
                    else:
                        pass
                else:
                    ya = True
                    break
                
            elif kalimat1[i] == kalimat2[i]:
                pass
            else:
                ya = False
                break

        if mentok == True and len(kalimat2) < len(kalimat1):
            ya = True
        else:
            pass

    return ya

print(kalimat2Lebih('Alisha Listya w','Alisha ListyP w'))
def sortKategoriHuruf(array, namaKategori, cara):
#sorting array, pastikan kategori isinya huruf semua
#sorting dilakukan dengan cara bubblesort
    arrayKolom = kolom(array, namaKategori)

    if cara == '+':
        swap = True
        while swap == True:
            swap = False
            for i in range(1, len(array)-1):
                if kalimat2Lebih(arrayKolom[i], arrayKolom[i+1]):
                    cacheSwap = array[i]
                    cacheSwapKolom = arrayKolom[i]

                    array[i] = array[i+1]
                    array[i+1] = cacheSwap

                    arrayKolom[i] = arrayKolom[i+1]
                    arrayKolom[i+1] = cacheSwapKolom

                    swap = True

    else: #cara == '-':
        swap = True
        while swap == True:
            swap = False
            for i in range(1, len(array)-1):
                if not kalimat2Lebih(arrayKolom[i], arrayKolom[i+1]):
                    cacheSwap = array[i]
                    cacheSwapKolom = arrayKolom[i]

                    array[i] = array[i+1]
                    array[i+1] = cacheSwap

                    arrayKolom[i] = arrayKolom[i+1]
                    arrayKolom[i+1] = cacheSwapKolom

                    swap = True

    return array

sortKategoriHuruf([[['de','da','ca','aab','aaa'],['alisha''da','ca','aab','aaa'],['c',5,4,3,2,1],['awe',1,2,3,4,5]]],'de','-')