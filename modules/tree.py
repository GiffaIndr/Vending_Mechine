import json

# Node tree untuk produk
class ProdukNode:
    def __init__(self, produk):
        self.produk = produk
        self.left = None
        self.right = None

# Binary Search Tree berdasarkan harga
class ProdukTree:
    def __init__(self):
        self.root = None
        self._load_produk()

    def _load_produk(self):
        with open("data/produk.json", "r") as f:
            data = json.load(f)
            for id_produk, p in data.items():
                p["id"] = id_produk
                self.insert(p)

    def insert(self, produk):
        def _insert(node, produk):
            if node is None:
                return ProdukNode(produk)
            if produk["harga"] < node.produk["harga"]:
                node.left = _insert(node.left, produk)
            else:
                node.right = _insert(node.right, produk)
            return node

        self.root = _insert(self.root, produk)

    def filter(self, kategori=None, harga_min=None, harga_max=None):
        result = []

        def _inorder(node):
            if node is None:
                return
            _inorder(node.left)
            p = node.produk
            if ((kategori is None or p["kategori"].lower() == kategori.lower()) and
                (harga_min is None or p["harga"] >= harga_min) and
                (harga_max is None or p["harga"] <= harga_max)):
                result.append(p)
            _inorder(node.right)

        _inorder(self.root)
        return result

# Objek yang bisa langsung dipanggil dari main.py
filter_by = ProdukTree()
