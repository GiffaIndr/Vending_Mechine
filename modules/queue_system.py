# Node untuk menyimpan data dan pointer ke node berikutnya
class Node:
    def __init__(self, data):
        # Inisialisasi data pada node
        self.data = data
        # Inisialisasi pointer ke node berikutnya
        self.next = None

# Struktur data Queue (antrean) menggunakan linked list
class Queue:
    def __init__(self):
        # Node paling depan antrean
        self.front = None
        # Node paling belakang antrean
        self.rear = None

    # Mengecek apakah antrean kosong
    def is_empty(self):
        return self.front is None

    # Menambahkan elemen ke belakang antrean
    def enqueue(self, data):
        # Buat node baru dengan data
        new_node = Node(data)
        # Jika antrean kosong, front dan rear sama-sama menunjuk node baru
        if self.rear is None:
            self.front = self.rear = new_node
            return
        # Tambahkan node baru ke belakang antrean
        self.rear.next = new_node
        # Perbarui rear menjadi node baru
        self.rear = new_node

    # Menghapus elemen dari depan antrean
    def dequeue(self):
        # Jika antrean kosong, tidak ada yang dihapus
        if self.is_empty():
            return None
        # Simpan node paling depan
        temp = self.front
        # Pindahkan front ke node berikutnya
        self.front = temp.next
        # Jika setelah dequeue antrean menjadi kosong, rear diset None
        if self.front is None:
            self.rear = None
        # Kembalikan data dari node yang di-dequeue
        return temp.data

    # Melihat elemen paling depan tanpa menghapusnya
    def peek(self):
        # Jika antrean kosong, kembalikan None
        if self.is_empty():
            return None
        # Kembalikan data node paling depan
        return self.front.data

    # Menampilkan seluruh elemen dalam antrean
    def show(self):
        current = self.front
        print("\nAntrean saat ini:")
        # Telusuri dan tampilkan setiap node dalam antrean
        while current:
            print(f"- {current.data}")
            current = current.next
