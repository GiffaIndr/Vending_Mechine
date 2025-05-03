import json
from modules.produk import load_produk, DATA_FILE
from modules.linkedlist import LinkedList
from modules.transaksi import TRANSAKSI_FILE

def lihat_riwayat_transaksi_linked_list():
    # Menampilkan riwayat transaksi menggunakan struktur data linked list
    riwayat = LinkedList()
    riwayat.load_from_file(TRANSAKSI_FILE) 
    riwayat.display() 

def simpan_produk(data):
    """Simpan data produk ke file JSON."""
    with open(DATA_FILE, 'w') as file: 
        # Menyimpan data produk dalam format JSON dengan indentasi
        json.dump(data, file, indent=4) 

def tambah_produk():
    produk = load_produk()  
    id_produk = input("ID Produk: ") 
    if id_produk in produk:
        print("ID sudah digunakan.")  
        return
    nama = input("Nama Produk: ")  
    kategori = input("Kategori: ")  
    
    # Validasi harga dan stok
    try:
        harga = int(input("Harga: "))  
        stok = int(input("Stok: "))
    except ValueError:
        # Menangani kesalahan jika input bukan angka
        print("Harga dan stok harus berupa angka.")  
        return

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
        # Menghapus produk dari data
        del produk[id_produk]  
        simpan_produk(produk)  
        print("Produk berhasil dihapus.")  
    else:
        print("ID tidak ditemukan.") 

def edit_produk():
    produk = load_produk()  
    id_produk = input("ID Produk yang ingin diedit: ")  
    # Menangani jika ID produk tidak ditemukan
    if id_produk not in produk:
        print("ID tidak ditemukan.")  
        return
    nama = input("Nama Baru (Enter untuk skip): ")  
    kategori = input("Kategori Baru (Enter untuk skip): ") 
    
    # Validasi harga dan stok
    harga = input("Harga Baru (Enter untuk skip): ")  
    stok = input("Stok Baru (Enter untuk skip): ") 

    if harga and not harga.isdigit():
        print("Harga harus berupa angka.")  
        return
    
    if stok and not stok.isdigit():
        print("Stok harus berupa angka.")  
        return
    
    if nama: produk[id_produk]['nama_produk'] = nama  # Jika ada input nama baru, perbarui
    if kategori: produk[id_produk]['kategori'] = kategori  # Jika ada input kategori baru, perbarui
    if harga: produk[id_produk]['harga'] = int(harga)  # Jika ada input harga baru, perbarui
    if stok: produk[id_produk]['stok'] = int(stok)  # Jika ada input stok baru, perbarui
    
    # Menyimpan data produk yang telah diperbarui
    simpan_produk(produk)  
    print("Produk berhasil diperbarui.") 
