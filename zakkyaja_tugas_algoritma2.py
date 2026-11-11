print("=== APLIKASI KASIR RESTORAN SUKA MAJU ===")
total = 0

while True:
    print("\n--- Daftar Menu ---")
    print("1. Nasi Goreng - Rp25.000")
    print("2. Mie Ayam - Rp15.000")
    print("3. Ayam Geprek - Rp20.000")
    print("4. Sate Ayam - Rp30.000")
    print("5. Bakso - Rp18.000")
    print("0. selesai memilih ")
    
    pilihan = int(input("mau yg mana pak/bu (0-5): "))
    
    if pilihan == 0:
        break
    elif pilihan == 1:
        harga = 25000
        nama_menu = "Nasi Goreng"
    elif pilihan == 2:
        harga = 15000
        nama_menu = "Mie Ayam"
    elif pilihan == 3:
        harga = 20000
        nama_menu = "Ayam Geprek"
    elif pilihan == 4:
        harga = 30000
        nama_menu = "Sate Ayam"
    elif pilihan == 5:
        harga = 18000
        nama_menu = "Bakso"
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        continue
        
    jumlah = int(input(f"mau beli berapa pak/bu {nama_menu}: "))
    subtotal = harga * jumlah
    total += subtotal
    print(f"Subtotal {nama_menu} ({jumlah}x): Rp{subtotal:,}")

if total > 200000:
    diskon_persen = 20
    potongan = total * 0.20
else:
    diskon_persen = 0
    potongan = 0

total_bayar = total - potongan

print("\n================================")
print("       STRUK PEMBAYARAN         ")
print("================================")
print(f"Total Belanja : Rp{total:,}")
print(f"Diskon        : {diskon_persen}%")
print(f"Potongan      : Rp{int(potongan):,}")
print("--------------------------------")
print(f"Total Bayar   : Rp{int(total_bayar):,}")
print("================================")
print("          Terima Kasih          ")
print("================================")