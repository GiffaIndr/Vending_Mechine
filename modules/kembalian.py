import json

PATH_UANG = "data/uang_kembalian.json"

def load_uang_kembalian():
    # Membaca data stok uang kembalian dari file JSON
    with open(PATH_UANG, 'r') as f:
        return json.load(f)  

def save_uang_kembalian(data):
    # Menyimpan data stok uang kembalian ke file JSON
    with open(PATH_UANG, 'w') as f:
        json.dump(data, f, indent=4)  

def hitung_kembalian(total_kembalian): 
    uang = sorted(
        ((int(nominal), stok) for nominal, stok in load_uang_kembalian().items()), 
        reverse=True
    )
    hasil = {}
    sisa = total_kembalian
    for nominal, stok in uang:
        if sisa <= 0:
            break
        jumlah = min(sisa // nominal, stok)
        if jumlah > 0:
            hasil[nominal] = jumlah
            sisa -= nominal * jumlah
    return hasil


def proses_kembalian(total_kembalian):
    uang_asli = load_uang_kembalian()
    uang = {int(k): v for k, v in uang_asli.items()}  # ubah key ke int

    kombinasi = hitung_kembalian(total_kembalian)
    if not kombinasi:
        return None

    for nominal, jumlah in kombinasi.items():
        uang[nominal] -= jumlah

    uang_str = {str(k): v for k, v in uang.items()}  # ubah key kembali ke str
    save_uang_kembalian(uang_str)

    return kombinasi


def isi_uang_kembalian():
    # Admin mengisi ulang stok pecahan uang secara manual
    uang = load_uang_kembalian()
    print("\n=== Isi Ulang Kembalian ===")
    for pecahan in sorted(uang.keys()):
        print(f"Pecahan Rp{pecahan} saat ini: {uang[pecahan]}")
        try:
            tambahan = int(input(f"Tambah berapa lembar untuk Rp{pecahan}? "))
            if tambahan >= 0:
                uang[pecahan] += tambahan
        except ValueError:
            print("Input tidak valid, lewati")
            
    save_uang_kembalian(uang)
    print("Uang kembalian berhasil diperbarui.")
    
def lihat_stok_pecahan():
    # Menampilkan stok uang kembalian yang tersedia
    uang = load_uang_kembalian()
    print("\n=== STOK PECAHAN UANG ===")
    for pecahan in sorted(uang.keys(), reverse=True):  
        print(f"Pecahan Rp{pecahan}: {uang[pecahan]} lembar/koin")
