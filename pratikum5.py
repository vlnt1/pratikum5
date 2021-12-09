data = {}
print("     PROGRAM INPUT NILAI     ")
print("=============================")

while True:
    a = input(" [(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] : ")

    ## MENU Tambah
    if (a.lower() == 't'):
        print("=========================")
        print("| TAMBAH DATA MAHASISWA |")
        print("=========================")
        nama          = input("Masukkan Nama        : ")
        nim           = input("Masukkan NIM         : ")
        nilaiTugas    = int(input("Masukkan Nilai Tugas : "))
        nilaiUts      = int(input("Masukkan Nilai UTS   : "))
        nilaiUas      = int(input("Masukkan Nilai UAS   : "))
        nilaiAkhir    = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        data[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("Data Berhasil Ditambahkan!")

    ## MENU Ubah
    elif (a.lower() == 'u'):
        print("=======================")
        print("| EDIT DATA MAHASISWA |")
        print("=======================")
        nama = input("Masukkan Nama: ")
        if nama in data.keys():
            nim           = input("Masukkan NIM Baru         : ")
            nilaiTugas    = int(input("Masukkan Nilai Tugas Baru : "))
            nilaiUts      = int(input("Masukkan Nilai UTS Baru   : "))
            nilaiUas      = int(input("Masukkan Nilai UAS Baru   : "))
            nilaiAkhir    = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
            data[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
            print("Data Berhasil Di Update!")
        else:
            print("Data tidak ditemukan!")

    ## MENU Cari
    elif (a.lower() == 'c'):
        print("=======================")
        print("| CARI DATA MAHASISWA |")
        print("=======================")
        nama = input("Masukan Nama:  ")
        if nama in data.keys():
            print("                     DAFTAR NILAI MAHASISWA                   ")
            print("==============================================================")
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir | ")
            print("==============================================================")
            print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(nama, nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir))
            print("==============================================================")
        else:
            print("Datanya {0} Tidak Ada ".format(nama))

    ## MENU Hapus
    elif (a.lower() == 'h'):
        nama = input("Masukkan Nama:  ")
        if nama in data.keys():
            del data[nama]
            print("Data Telah dihapus!")
        else:
            print("Data Mahasiswa Tidak Ada".format(nama))

    ## MENU Lihat
    elif (a.lower() == 'l'):
        if data.items():
            print("                        DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            i = 0
            for x in data.items():
                i += 1
                print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("==================================================================")
        else:
            print("                        DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")

    ## MENU Keluar
    elif (a.lower() == 'k'):
        print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]")
        break

    else:
        print("Pilih menu yang tersedia: ")