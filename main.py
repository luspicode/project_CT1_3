from owner import menu_owner
from customer import menu_customer
from utils import nama_barang, jumlah_barang, harga_barang
import subprocess
import os


def clear():
    subprocess.run(
        'cls' if os.name == 'nt' else 'clear',shell=True)

clear()

while True:

    print("|", "="*50, "|")
    print("|", " "*8 ,"Selamat Datang Di Vending Machine", " "*7 ,"|")
    print("|", "="*50, "|")
    print("|", " "*19 ,"Pilih Menu: ", " "*17 ,"|")
    print("|", "="*50, "|")
    print("|", "1. Owner", " "*41, "|")
    print("|", "2. Customer", " "*38, "|")
    print("|", "0. Out", " "*43, "|")
    print("|", "="*50, "|")
    
    temp = input("Masukkan Pilihan: ")

    if temp == "0":
        break
    elif temp == "1":
        menu_owner()
    else:
        menu_customer()

print("Vending Machine Dimatikan...")