import subprocess
import os
from utils import nama_barang, jumlah_barang, harga_barang

def clear():
    subprocess.run(
        'cls' if os.name == 'nt' else 'clear',shell=True)

clear()

def edit_harga():
    print("|", "="*50, "|")
    print("|", " "*8 ,"Selamat Datang Di Vending Machine", " "*7 ,"|")
    print("|", "="*50, "|")
    print("|", " "*19 ,"Pilih Barang: ", " "*15 ,"|")
    print("|", "="*50, "|")
    print("|","Daftar Barang- Harga:", " "*19 ,"|")
    for i in range(len(nama_barang)):
        print("|", f"{i+1}. {nama_barang[i]} - Rp{harga_barang[i]}", " "*(49-len(f"{i+1}. {nama_barang[i]} - Rp{harga_barang[i]}")), "|")
    print("|", "0. Kembali", " "*39, "|")
    print("|", "="*50, "|")
    temp = int(input("Masukkan Pilihan: "))-1
    harga_baru = int(input("Masukkan harga baru: "))
    harga_barang[temp] = harga_baru
    print(f"Harga {nama_barang[temp]} diubah menjadi Rp{harga_barang[temp]}!")
    return

def edit_stok():
    print("|", "="*50, "|")
    print("|", " "*8 ,"Selamat Datang Di Vending Machine", " "*7 ,"|")
    print("|", "="*50, "|")
    print("|", " "*19 ,"Pilih Barang: ", " "*15 ,"|")
    print("|", "="*50, "|")
    print("|","Daftar Barang - Stok:", " "*27 ,"|")
    for i in range(len(nama_barang)):
        print("|", f"{i+1}. {nama_barang[i]} - {jumlah_barang[i]} pcs", " "*(49-len(f"{i+1}. {nama_barang[i]} - {jumlah_barang[i]} pcs")), "|")
    print("|", "0. Kembali", " "*39, "|")
    print("|", "="*50, "|")
    temp = int(input("Masukkan Pilihan: "))-1
    stok_baru = int(input("Masukkan stok baru: "))
    jumlah_barang[temp] = stok_baru
    print(f"Stok {nama_barang[temp]} diubah menjadi {jumlah_barang[temp]}!")
    return