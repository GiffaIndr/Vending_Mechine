from modules.produk import tampilkan_produk
from modules.queue_system import Queue

def main():
    antrean = Queue()
    
    while True:
        print("\n===== VENDING MACHINE =====")
        print("1. Lihat Daftar Produk")
        print("2. Masuk Antrean Pembelian")
        print("3. Lihat Antrean")
        print("4. Proses Pembelian Berikutnya")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tampilkan_produk()

        elif pilihan == '2':
            nama = input("Masukkan nama Anda: ")
            antrean.enqueue(nama)
            print(f"{nama} telah masuk ke antrean.")

        elif pilihan == '3':
            antrean.show()

        elif pilihan == '4':
            if antrean.is_empty():
                print("Tidak ada antrean saat ini.")
            else:
                user = antrean.dequeue()
                print(f"\nGiliran {user} untuk membeli.")
                # Proses pembelian user akan disambung di sini (nanti dibuat)

        elif pilihan == '0':
            print("Terima kasih telah menggunakan vending machine.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == '__main__':
    main()
