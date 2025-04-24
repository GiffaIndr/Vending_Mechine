
import json

DATA_FILE = 'data/produk.json'

def load_produk():
    """Membaca data produk dari file JSON."""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def tampilkan_produk():
    """Menampilkan daftar produk dengan format tabel."""
    produk = load_produk()
    print("\n===== Daftar Produk =====")
    print(f"{'ID':<5}{'Nama':<20}{'Kategori':<15}{'Harga':<10}{'Stok':<5}")
    for id_produk, item in produk.items():
        print(f"{id_produk:<5}{item['nama_produk']:<20}{item['kategori']:<15}{item['harga']:<10}{item['stok']:<5}")

# Contoh penggunaan (sementara untuk testing)
if __name__ == '__main__':
    tampilkan_produk()
