import subprocess
import os
<<<<<<< HEAD
from utils import nama_barang, jumlah_barang, harga_barang
=======
>>>>>>> afdb1fe77286e9b2c30fe7f266b9904fe9fbe008

def clear():
    subprocess.run(
        'cls' if os.name == 'nt' else 'clear',shell=True)

clear()

def menu_customer():
    print("|", "="*50, "|")
    print("|", " "*8 ,"Selamat Datang Di Vending Machine", " "*7 ,"|")
    print("|", "="*50, "|")
    print("|", " "*19 ,"Pilih Menu: ", " "*17 ,"|")
    print("|", "="*50, "|")
<<<<<<< HEAD
    print("|","Daftar Barang - Stok - Harga:", " "*19 ,"|")
    for i in range(len(nama_barang)):
        print("|", f"{i+1}. {nama_barang[i]} - {jumlah_barang[i]} pcs - Rp{harga_barang[i]}", " "*(49-len(f"{i+1}. {nama_barang[i]} - {jumlah_barang[i]} pcs - Rp{harga_barang[i]}")), "|")
    print("|", "0. Kembali", " "*39, "|")
=======
    print("|", "1. Tambah Barang", " "*33, "|")
    print("|", "2. Hapus Barang", " "*34, "|")
    print("|", "3. Edit Harga", " "*36, "|")
    print("|", "0. ", " "*43, "|")
>>>>>>> afdb1fe77286e9b2c30fe7f266b9904fe9fbe008
    print("|", "="*50, "|")
    
    temp = input("Masukkan Pilihan: ")
    
    if temp == "0":
        print("Keluar dari owner...")
        return
    
<<<<<<< HEAD
    jumlah = int(input("Masukkan Jumlah Barang: "))
    if jumlah == 0:
        print("Jumlah Barang Tidak Boleh 0")
        return
    
    for i in range(len(daftar_barang.nama_barang)):
        if temp == str(i+1):
            if daftar_barang.jumlah_barang[i] >= jumlah:
                print(f"Anda akan membayar {jumlah} buah {daftar_barang.nama_barang[i]} dengan total harga Rp{jumlah * daftar_barang.harga_barang[i]}?")
                konfirmasi = input("Masukkan Y/N: ")
                if konfirmasi == "y" or konfirmasi == "Y":
                    daftar_barang.jumlah_barang[i] -= jumlah
                    print("Pembayaran Berhasil!")
                    print(f"Terima kasih telah membeli {jumlah} buah {daftar_barang.nama_barang[i]}!")
                    return
                else: return
            else:
                print(f"Stok {daftar_barang.nama_barang[i]} kurang!")
                return
    print("Barang tidak ditemukan!")
    return
=======
    elif temp == "1":
        pass
    
    else:
        pass
>>>>>>> afdb1fe77286e9b2c30fe7f266b9904fe9fbe008
