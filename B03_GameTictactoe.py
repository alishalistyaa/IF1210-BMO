# Senin, 4 April 2022
# Catatan: Aku lebih suka bikin tictactoe daripada spesifikasi utama WKWK

def tictactoe():
    # Inisialisasikan matriks keadaan semula
    T = [['#' for j in range(3)] for i in range(3)]

    # Menampilkan ke layar Legenda dan Status Papan
    print("""

Legenda:
X Pemain 1
X Pemain 2

""")

    # Algoritma Utama (Looping)

    # Menampilkan status papan
    for i in range(3):
        for j in range(3):
         print(T[i][j], end = " ")
        print("")

    # Ketika belum ada pemain yang menang,
    # Maka program akan berjalan
    programjalan = True 

    # Inisialiasi Giliran Pertama
    giliran = 1

    # Selama belum ada pemenang, maka
    while programjalan:
        # Menentukan Giliran pemain
        if giliran%2 == 0 :
            giliranpemain = "X"
        elif giliran%2 != 0 :
            giliranpemain = "O"

        # Input pemain pertama
        print(f"\nGiliran pemain {giliranpemain}")
        kolom = int(input("X: "))
        baris = int(input("Y: "))

        # Validasi Kotak
        # Input kotak tervalidasi jika kolom dan baris kurang dari tiga atau lebih dari satu
        # Input juga tervalidasi jika belum diisi pemain sebelumnya
        while not ((1<= kolom <= 3) or (1<=baris<=3)):
            print("\nKotak tidak valid.")
            print(f"\nGiliran pemain {giliranpemain}")
            kolom = int(input("X: "))
            baris = int(input("Y: "))

        while not (T[kolom-1][baris-1]=="#"):
            print("\nKotak sudah terisi. Silahkan pilih kotak lain.")
            print(f"\nGiliran pemain {giliranpemain}")
            kolom = int(input("X: "))
            baris = int(input("Y: "))

    # Menginput hasil tic tac toe
        T[kolom-1][baris-1] = giliranpemain


    # Menampilkan status papan setelah dilakukan input pemain
        print("\nStatus Papan")
        for i in range(3):
            for j in range(3):
                print(T[i][j], end = " ")
            print("")
    
    # Giliran + 1
        giliran += 1

    # Jika status papan = bener, salah satunya menang
    # Cek baris (3 kemungkinan)
        for i in range(3):
            if T[i][0]=="X":
                if T[i][1]=="X" and T[i][2]=="X":
                    programjalan = False
                    pemenang = "X"
            elif T[i][0] == "O":
                if T[i][1]=="O" and T[i][2]=="O":
                    programjalan = False
                    pemenang = "O"

        # Cek kolom (3 kemungkinan)
        for j in range(3):
            if T[0][j]=="X":
                if T[1][j]=="X" and T[2][j]=="X":
                    programjalan = False
                    pemenang = "X"
            elif T[0][j] == "O":
                if T[1][j]=="O" and T[2][j]=="O":
                    programjalan = False
                    pemenang = "O"

        # Cek diagonal (2 kemungkinan)
        if T[1][1] == "X":
            if T[0][0]=="X" and T[2][2]=="X":
                programjalan = False
                pemenang = "X"
            elif T[0][2]=="X" and T[2][0]=="X":
                programjalan = False
                pemenang = "X"  
        elif T[1][1] == "O":
            if T[0][0]=="O" and T[2][2]=="O":
                programjalan = False
                pemenang = "O"
            elif T[0][2]=="O" and T[2][0]=="O":
                programjalan = False
                pemenang = "O"  

        # Semua baris terisi tapi gaada pemenang
        if giliran == 10:
            programjalan = False
            pemenang = "None"
    
    # Deklarasi pemenang setelah program berhenti
    if pemenang == "O" or pemenang == "X":
        print(f'\nPemain "{pemenang}" menang')
    else : print("Yah tidak ada pemenang :(")

# tictactoe()