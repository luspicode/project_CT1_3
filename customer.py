import subprocess
import os
from utils import nama_barang, jumlah_barang, harga_barang

def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear',shell=True)

def menu_customer():
    clear()
    print("|", "="*50, "|")
    print("|", " "*8 ,"Selamat Datang Di Vending Machine", " "*7 ,"|")
    print("|", "="*50, "|")
    print("|", " "*19 ,"Pilih Menu: ", " "*17 ,"|")
    print("|", "="*50, "|")
    print("|","Daftar Barang - Stok - Harga:", " "*19 ,"|")
    for i in range(len(nama_barang)):
        print("|", f"{i+1}. {nama_barang[i]} - {jumlah_barang[i]} pcs - Rp{harga_barang[i]}", " "*(49-len(f"{i+1}. {nama_barang[i]} - {jumlah_barang[i]} pcs - Rp{harga_barang[i]}")), "|")
    print("|", "0. Kembali", " "*39, "|")
    print("|", "="*50, "|")
    
    temp = input("Masukkan Pilihan: ")
    
    if temp == "0":
        print("Keluar dari owner...")
        return
    
    jumlah = int(input("Masukkan Jumlah Barang: "))
    if jumlah == 0:
        print("Jumlah Barang Tidak Boleh 0")
        return
    
    for i in range(len(nama_barang)):
        if temp == str(i+1):
            if jumlah_barang[i] >= jumlah:
                print(f"Anda akan membayar {jumlah} buah {nama_barang[i]} dengan total harga Rp{jumlah * harga_barang[i]}?")
                konfirmasi = input("Masukkan Y/N: ")
                if konfirmasi == "y" or konfirmasi == "Y":
                    jumlah_barang[i] -= jumlah
                    print("Pembayaran Berhasil!")
                    print(f"Terima kasih telah membeli {jumlah} buah {nama_barang[i]}!")
                    return
                else: return
            else:
                print(f"Stok {nama_barang[i]} kurang!")
                return
    print("Barang tidak ditemukan!")
    return
