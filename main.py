import subprocess
import os
import time


def clear():
    subprocess.run(
        'cls' if os.name == 'nt' else 'clear',shell=True)

nama_barang = ["Air Mineral", "Teh", "Kopi Instan", "Susu"]
jumlah_barang = [10, 10, 10, 10]
harga_barang = [3000, 3000, 4000, 6000]

clear()

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

def edit_harga():
    clear()
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
    time.sleep(1.5)
    clear()
    return

def edit_stok():
    clear()
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
    time.sleep(1.5)
    clear()
    return

def menu_owner():
    clear()
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