import subprocess
import os

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
    print("|", "1. Tambah Barang", " "*33, "|")
    print("|", "2. Hapus Barang", " "*34, "|")
    print("|", "3. Edit Harga", " "*36, "|")
    print("|", "0. ", " "*43, "|")
    print("|", "="*50, "|")
    
    temp = input("Masukkan Pilihan: ")
    
    if temp == "0":
        print("Keluar dari owner...")
        return
    
    elif temp == "1":
        pass
    
    else:
        pass