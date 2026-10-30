import time

nama_barang = ["SUKRO", "POCKY CHOCOLATE", "NISSIN CUP NOODLES", "FLORIDINA", "BIG THUNDER", "YOU C1000 ORANGE WATER", "YOU C1000 LEMON WATER", "TEH BOTOL", "TWISTER", "ULTRAMILK PLAIN", "CHIC CHOC", "LARUTAN CAP BADAK", "SARI KACANG HIJAU", "POCARI SWEAT","MIZONE"]
stok_barang = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
harga_barang = [10900, 9500, 8500, 3500, 9000, 9000, 9000, 4500, 8000, 8400, 11500, 8900, 5900, 8800, 6500]
keranjang = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_harga = 0

def lihat_keranjang():
    print("Isi Keranjang: ")
    total_harga = 0
    for i in range(len(keranjang)):
        if keranjang[i] > 0:
            print(f"{keranjang[i]} buah {nama_barang[i]} = Rp{keranjang[i] * harga_barang[i]}")
            total_harga += keranjang[i] * harga_barang[i]
    print(f"Total Harga = Rp{total_harga}")
    return

def kosongkan_keranjang():
    for i in range(len(keranjang)):
        keranjang[i] = 0
    return

def reset_keranjang():
    for i in range(len(keranjang)):
        stok_barang[i] += keranjang[i]
        keranjang[i] = 0
    return

def Pembayaran():
    print(f"Anda akan membayar: ")
    lihat_keranjang()

    konfirmasi = input("Masukkan (Y) jika sudah dan (N) jika tidak jadi membeli: ")
    if konfirmasi == "y" or konfirmasi == "Y":
        print("Pembayaran Berhasil!")
        print(f"Silakan ambil barang Anda. Terima kasih!")
        kosongkan_keranjang()
        reset_keranjang()
        return
    else:
        print("Pembayaran dibatalkan. Kembali ke menu utama...") 
        return

def Output_Data_Item():
    print("|", "="*50, "|")
    print("|", " "*8 ,"Selamat Datang Di Vending Machine", " "*7 ,"|")
    print("|", "="*50, "|")
    print("|", " "*19 ,"Pilih Menu: ", " "*17 ,"|")
    print("|", "="*50, "|")
    print("|","Kode - Daftar Barang - Harga - Stok:", " "*13 ,"|")
    for i in range(len(nama_barang)):
        print("|", f"{i+1} - {nama_barang[i]} - Rp{harga_barang[i]} - {stok_barang[i]} pcs")
    print("|", "0 - Lihat Keranjang")
    print("|", "00 - Reset Keranjang")
    print("|", "000 - Pembayaran")
    print("|", "="*50, "|")
    return

def menu_customer():
    Output_Data_Item()

    choice = str(input("Masukkan Nomor Barang: "))

    if choice == "0":
        if sum(keranjang) == 0:
            print("Keranjang kosong.")
            time.sleep(1.5)
            return
        lihat_keranjang()
        konfirmasi = input("Klink Enter untuk kembali" )
        return

    if choice == "00":
        reset_keranjang()
        print("Keranjang telah direset.")
        time.sleep(1.5)
        return

    if choice == "000":
        if sum(keranjang) == 0:
            print("Keranjang kosong, silakan isi terlebih dahulu.")
            time.sleep(1.5)
            return
        else:
            Pembayaran()
            time.sleep(2)
            return

    jumlah_barang = int(input("Masukkan Jumlah Barang: "))
    
    for i in range(len(nama_barang)):
        if int(choice) == i+1:
            if stok_barang[i] <= jumlah_barang:
                print("Maaf, stok barang kurang.")
                time.sleep(1.5)
                return
            else: 
                stok_barang[i] -= jumlah_barang
                keranjang[i] += jumlah_barang
                print(f"Berhasil menambahkan {jumlah_barang} buah {nama_barang[i]} ke keranjang.")
                time.sleep(1.5)
                return
    print("Barang tidak ditemukan!, coba lagi")
    time.sleep(1.5)
    return

while True:
    menu_customer()

print("Vending Machine Dimatikan...")
