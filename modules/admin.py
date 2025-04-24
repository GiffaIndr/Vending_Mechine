import json
from modules.produk import load_produk, DATA_FILE

def simpan_produk(data):
    """Simpan data produk ke file JSON."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def tambah_produk():
    produk = load_produk()
    id_produk = input("ID Produk: ")
    if id_produk in produk:
        print("ID sudah digunakan.")
        return
    nama = input("Nama Produk: ")
    kategori = input("Kategori: ")
    harga = int(input("Harga: "))
    stok = int(input("Stok: "))
    produk[id_produk] = {
        "nama_produk": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok
    }
    simpan_produk(produk)
    print("Produk berhasil ditambahkan.")

def hapus_produk():
    produk = load_produk()
    id_produk = input("ID Produk yang ingin dihapus: ")
    if id_produk in produk:
        del produk[id_produk]
        simpan_produk(produk)
        print("Produk berhasil dihapus.")
    else:
        print("ID tidak ditemukan.")

def edit_produk():
    produk = load_produk()
    id_produk = input("ID Produk yang ingin diedit: ")
    if id_produk not in produk:
        print("ID tidak ditemukan.")
        return
    nama = input("Nama Baru (Enter untuk skip): ")
    kategori = input("Kategori Baru (Enter untuk skip): ")
    harga = input("Harga Baru (Enter untuk skip): ")
    stok = input("Stok Baru (Enter untuk skip): ")

    if nama: produk[id_produk]['nama_produk'] = nama
    if kategori: produk[id_produk]['kategori'] = kategori
    if harga: produk[id_produk]['harga'] = int(harga)
    if stok: produk[id_produk]['stok'] = int(stok)

    simpan_produk(produk)
    print("Produk berhasil diperbarui.")
