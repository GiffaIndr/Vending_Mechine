from modules.produk import tampilkan_produk
from modules.queue_system import Queue
from modules.auth import login, register
from modules.admin import tambah_produk, hapus_produk, edit_produk, lihat_riwayat_transaksi_linked_list
from modules.kembalian import isi_uang_kembalian, lihat_stok_pecahan
from modules.transaksi_fungsi import transaksi_pembelian
from modules.binary_search import binary_search_produk_by_harga

# Inisialisasi antrean global untuk seluruh user
global_antrean = Queue()

# Fungsi untuk menu yang digunakan oleh admin
def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tampilkan Produk")
        print("2. Tambah Produk")
        print("3. Hapus Produk")
        print("4. Edit Produk")
        print("5. Lihat Laporan Transaksi")
        print("6. Lihat Stok Pecahan")
        print("7. Isi Ulang Pecahan")
        print("0. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_produk()  
        elif pilihan == '2':
            tambah_produk() 
        elif pilihan == '3':
            hapus_produk()  
        elif pilihan == '4':
            edit_produk()  
        elif pilihan == '5':
            lihat_riwayat_transaksi_linked_list()  
        elif pilihan == '6':
            lihat_stok_pecahan()  
        elif pilihan == '7':
            isi_uang_kembalian()  
        elif pilihan == '0':
            break  
        else:
            print("Pilihan tidak valid.")  # Menangani pilihan yang salah

# Fungsi untuk menu yang digunakan oleh user
def menu_user(username):
    while True:
        print(f"\n===== VENDING MACHINE (User: {username}) =====")
        print("1. Lihat Daftar Produk")
        print("2. Masuk Antrean Pembelian")
        print("3. Lihat Antrean")
        print("4. Proses Pembelian Berikutnya")
        print("5. Cari Produk Berdasarkan Harga")
        print("0. Logout")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_produk() 
        elif pilihan == '2':
             # Menambah user ke antrean
            global_antrean.enqueue(username) 
            print(f"{username} telah masuk ke antrean.")
        elif pilihan == '3':
            # Menampilkan antrean saat ini
            global_antrean.show()  
        elif pilihan == '4':
            if global_antrean.is_empty():
                print("Tidak ada antrean saat ini.") 
            else:
                # Proses pembelian user yang pertama
                user = global_antrean.dequeue()  
                print(f"\nGiliran {user} untuk membeli.")
                transaksi_pembelian(user)  
        elif pilihan == '5':
            try:
                # Mencari produk berdasarkan harga
                harga = int(input("Masukkan harga yang dicari: "))  
                hasil = binary_search_produk_by_harga(harga)
                if hasil:
                    print(f"Ditemukan: ID={hasil['id']}, Nama={hasil['nama']}, Harga={hasil['harga']}, Stok={hasil['stok']}")
                else:
                    print("Tidak ada produk dengan harga tersebut.")  
            except ValueError:
                # Menangani input yang tidak valid
                print("Input tidak valid.")  
        elif pilihan == '0':
            # Logout dari menu user
            break  
        else:
            print("Pilihan tidak valid.") 

# Fungsi utama yang menangani login dan memilih menu berdasarkan role
def main():
    print("\n=== Selamat Datang di Vending Machine ===")
    while True:
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        menu = input("Pilih menu: ")
        if menu == '1':
            result = login()  
            if result:
                username, role = result
                if role == 'admin':
                    # Menampilkan menu admin jika role admin
                    menu_admin()  
                else:
                    # Menampilkan menu user jika role user
                    menu_user(username)  
        elif menu == '2':
            register() 
        elif menu == '0':
            print("Sampai jumpa!") 
            # Keluar dari program
            break  
        else:
            print("Pilihan tidak valid.") 
            
# Menjalankan fungsi main ketika program dimulai
if __name__ == '__main__':
    main()
