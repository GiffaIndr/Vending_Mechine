from modules.produk import load_produk

# Mencari produk berdasarkan harga menggunakan algoritma binary search
def binary_search_produk_by_harga(target_harga):
    produk_dict = load_produk()
    produk_list = [
        {"id": pid, "nama": data["nama_produk"], "harga": data["harga"], "stok": data["stok"]}
        for pid, data in produk_dict.items()
    ]

    # Urutkan berdasarkan harga (ascending)
    produk_list.sort(key=lambda x: x["harga"])

    # Proses Binary Search
    low = 0
    high = len(produk_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if produk_list[mid]["harga"] == target_harga:
            # Jika ditemukan, kembalikan data produk
            return produk_list[mid]
        elif produk_list[mid]["harga"] < target_harga:
            low = mid + 1
        else:
            high = mid - 1
    return None
