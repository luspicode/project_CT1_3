import subprocess
import os
from utils import nama_barang, jumlah_barang, harga_barang
from edit_harga_dan_stok import edit_harga, edit_stok

def clear():
    subprocess.run(
        'cls' if os.name == 'nt' else 'clear',shell=True)

clear()

def menu_owner():
    print("|", "="*50, "|")
    print("|", " "*8 ,"Selamat Datang Di Vending Machine", " "*7 ,"|")
    print("|", "="*50, "|")
    print("|", " "*19 ,"Pilih Menu: ", " "*17 ,"|")
    print("|", "="*50, "|")
    print("|", "1. Edit Harga", " "*36, "|")
    print("|", "2. Edit Stok", " "*37, "|")
    print("|", "0. Kembali", " "*39, "|")
    print("|", "="*50, "|")
    
    temp = input("Masukkan Pilihan: ")
    
    if temp == "0":
        print("Keluar dari owner...")
        return
    
    elif temp == "1":
        edit_harga()

    elif temp == "2":
        edit_stok()
    
    else:
        pass