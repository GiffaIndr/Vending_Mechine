from modules.produk import load_produk, save_produk
from modules.kembalian import proses_kembalian
from modules.transaksi import save_transaksi 
# Untuk mencatat waktu transaksi
from datetime import datetime

# Fungsi utama untuk melakukan transaksi pembelian
def transaksi_pembelian(username):
    produk = load_produk()
    
    # Menampilkan daftar produk
    print("\n=== TRANSAKSI PEMBELIAN ===")
    print(f"{'ID':<5} {'Nama':<20} {'Harga':<10} {'Stok':<5}")
    for pid, item in produk.items():
        print(f"{pid:<5} {item['nama_produk']:<20} {item['harga']:<10} {item['stok']:<5}")
    input("Klik Enter Untuk Melanjutkan...")
    
    # Input ID produk
    id_produk = input("Masukkan ID produk yang ingin dibeli: ").strip().upper()
    if id_produk not in produk:
        print("ID produk tidak ditemukan.")
        input("Klik Enter Untuk Melanjutkan...")
        return

    item = produk[id_produk]
    
    # Input jumlah yang ingin dibeli
    try:
        jumlah = int(input(f"Berapa banyak {item['nama_produk']} yang ingin dibeli? "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0.")
            input("Klik Enter Untuk Melanjutkan...")
            return
        if jumlah > item['stok']:
            print("Stok tidak mencukupi.")
            input("Klik Enter Untuk Melanjutkan...")
            return
    except ValueError:
        print("Input tidak valid.")
        input("Klik Enter Untuk Melanjutkan...")
        return

    # Hitung total harga
    total = jumlah * item['harga']
    print(f"Total harga: Rp{total}")

    # Input uang yang dibayarkan
    try:
        bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
        if bayar < total:
            print("Uang tidak cukup.")
            input("Klik Enter Untuk Melanjutkan...")
            return
    except ValueError:
        print("Input tidak valid.")
        input("Klik Enter Untuk Melanjutkan...")
        return

    # Hitung kembalian dan proses jika ada
    kembalian = bayar - total
    kombinasi_kembalian = proses_kembalian(kembalian)
    
    # Gagal jika tidak bisa memberi kembalian
    if kembalian > 0 and kombinasi_kembalian is None:
        print("Mesin tidak bisa memberikan kembalian yang sesuai. Transaksi dibatalkan.")
        input("Klik Enter Untuk Melanjutkan...")
        return

    # Kurangi stok produk
    produk[id_produk]['stok'] -= jumlah
    save_produk(produk)

    # Simpan informasi transaksi ke file
    transaksi = {
        "username": username,
        "id_produk": id_produk,
        "nama_produk": item['nama_produk'],
        "jumlah": jumlah,
        "total": total,
        "bayar": bayar,
        "kembalian": kembalian,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_transaksi(transaksi)

    # Tampilkan konfirmasi dan detail kembalian
    print("Pembelian berhasil!")
    print(f"Kembalian: Rp{kembalian}")
    input("Klik Enter Untuk Melanjutkan...")
    if kembalian > 0:
        print("Rincian kembalian:")
        for pecahan, jml in kombinasi_kembalian.items():
            print(f"Rp{pecahan}: {jml} lembar/koin")
        input("Klik Enter Untuk Melanjutkan...")
