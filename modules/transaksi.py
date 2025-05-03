import json

TRANSAKSI_FILE = "data/transaksi.json"

# Fungsi untuk menyimpan transaksi ke file
def save_transaksi(transaksi):
    try:
        with open(TRANSAKSI_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(transaksi)

    with open(TRANSAKSI_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Fungsi untuk memuat transaksi dari file
def load_transaksi():
    try:
        with open(TRANSAKSI_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []