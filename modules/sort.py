def quick_sort_produk(produk_list, ascending=True):
    if len(produk_list) <= 1:
        return produk_list

    pivot = produk_list[0]
    left = []
    right = []

    for item in produk_list[1:]:
        if ascending:
            if item["harga"] < pivot["harga"]:
                left.append(item)
            else:
                right.append(item)
        else:
            if item["harga"] > pivot["harga"]:
                left.append(item)
            else:
                right.append(item)

    return quick_sort_produk(left, ascending) + [pivot] + quick_sort_produk(right, ascending)
