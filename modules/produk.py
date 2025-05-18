import json
from modules.transaksi import save_transaksi
from modules.kembalian import proses_kembalian

DATA_FILE = "data/produk.json"

# Memuat data produk dari file JSON dan mengembalikannya sebagai dictionary
def load_produk():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Menyimpan data produk ke file JSON secara permanen
def save_produk(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Menampilkan daftar semua produk dalam format tabel ke terminal
def tampilkan_produk():
    produk = load_produk()
    print("\nDaftar Produk:")
    print(f"{'ID':<6} {'Nama':<20} {'Harga':<10} {'Stok':<5}")
    for id_produk, detail in produk.items():
        print(f"{id_produk:<6} {detail['nama_produk']:<20} {detail['harga']:<10} {detail['stok']:<5}")
    input("Klik Enter Untuk Melanjutkan...")

# Menangani proses pembelian produk oleh user
def beli_produk(user):
    produk = load_produk()
    tampilkan_produk()
    
    id_produk = input("\nMasukkan ID produk yang ingin dibeli: ")
    produk_terpilih = produk.get(id_produk)  # Ambil langsung dari dictionary, bukan pakai next()

    if not produk_terpilih:
        print("Produk tidak ditemukan.")
        return

    if produk_terpilih['stok'] <= 0:
        print("Stok produk habis.")
        return

    try:
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
    except ValueError:
        print("Input jumlah tidak valid.")
        return

    if jumlah > produk_terpilih['stok']:
        print("Jumlah melebihi stok yang tersedia.")
        return

    total_harga = jumlah * produk_terpilih['harga']
    print(f"Total harga: Rp{total_harga}")

    try:
        uang = int(input("Masukkan uang Anda: "))
    except ValueError:
        print("Input uang tidak valid.")
        return

    if uang < total_harga:
        print("Uang tidak cukup untuk melakukan pembelian.")
        return

    kembalian = uang - total_harga
    kombinasi_kembalian = proses_kembalian(kembalian)
    if kombinasi_kembalian is None:
        print("Maaf, uang kembalian tidak mencukupi. Transaksi dibatalkan.")
        return

    # Update stok dan simpan perubahan
    produk_terpilih['stok'] -= jumlah
    save_produk(produk)

    # Simpan transaksi
    # save_transaksi(user, id_produk, jumlah, total_harga, "tunai")

    print("Pembelian berhasil. Kembalian Anda:")
    for pecahan, jumlah in kombinasi_kembalian.items():
        print(f"Rp{pecahan} x {jumlah}")
