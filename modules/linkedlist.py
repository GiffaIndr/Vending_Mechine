class Node:
    def __init__(self, data):
        self.data = data  # Menyimpan data transaksi
        self.next = None  # Menunjuk ke node berikutnya

class LinkedList:
    def __init__(self):
        self.head = None 

    def append(self, data):
        # Menambahkan node baru di akhir linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def display(self):
        # Menampilkan semua isi linked list
        curr = self.head
        if not curr:
            print("Riwayat transaksi kosong.")
        else:
            print("=== RIWAYAT TRANSAKSI (Linked List) ===")
            while curr:
                t = curr.data
                print(f"ID: {t['id_transaksi']}, User: {t['user']}, Produk: {t['id_produk']}, Jumlah: {t['jumlah']}, Total: Rp{t['total_harga']}, Tanggal: {t['tanggal']}")
                curr = curr.next

    def load_from_file(self, filename):
        # Memuat data dari file JSON ke dalam linked list
        import json
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    self.append(item)
        except FileNotFoundError:
            print("File transaksi tidak ditemukan.")
