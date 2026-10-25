nama_barang = ["SUKRO", "POCKY CHOCOLATE", "NISSIN CUP NOODLES", "FLORIDINA", "BIG THUNDER", "YOU C1000 ORANGE WATER", "YOU C1000 LEMON WATER", "TEH BOTOL", "TWISTER", "ULTRAMILK PLAIN", "CHIC CHOC", "LARUTAN CAP BADAK", "SARI KACANG HIJAU", "POCARI SWEAT","MIZONE"]
jumlah_barang = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
harga_barang = [10900, 9500, 8500, 3500, 9000, 9000, 9000, 4500, 8000, 8400, 11500, 8900, 5900, 8800, 6500]

def Output_Data_Item():
    print("|", "="*50, "|")
    print("|", " "*8 ,"Selamat Datang Di Vending Machine", " "*7 ,"|")
    print("|", "="*50, "|")
    print("|", " "*19 ,"Pilih Menu: ", " "*17 ,"|")
    print("|", "="*50, "|")
    print("|","Kode - Daftar Barang - Harga - Stok:", " "*13 ,"|")
    panjang_tulisan = len(f"{i+1} - {nama_barang[i]} - Rp{harga_barang[i]} - {jumlah_barang[i]} pcs ")
    for i in range(len(nama_barang)):
        print("|", f"{i+1} - {nama_barang[i]} - Rp{harga_barang[i]} - {jumlah_barang[i]} pcs", " "*(50-panjang_tulisan), "|")
    print("|", "0 - Kembali", " "*38, "|")
    print("|", "="*50, "|")

def menu_customer():
    Output_Data_Item()

    temp = int(input("Masukkan Nomor Barang: "))
    
    if temp == 0:
        print("Keluar dari owner...")
        return
    
    for i in range(len(nama_barang)):
        if temp == i+1:
            if jumlah_barang[i] <= 0:
                print("Maaf, stok barang habis.")
                return
            else: 
                print(f"Anda sudah membayar 1 buah {nama_barang[i]} dengan harga Rp{harga_barang[i]} melalui QR berikut?")
                konfirmasi = input("Masukkan (Y) jika sudah dan (N) jika tidak jadi membeli: ")
                if konfirmasi == "y" or konfirmasi == "Y":
                    jumlah_barang[i] -= 1
                    print("Pembayaran Berhasil!")
                    print(f"Silakan ambil {nama_barang[i]} Anda. Terima kasih!")
                    return
                else:
                    print("Pembayaran dibatalkan. Kembali ke menu utama...") 
                    return
    print("Barang tidak ditemukan!, coba lagi")
    return

while True:
    menu_customer()

print("Vending Machine Dimatikan...")
