import json
with open("data_barang.json", "r", encoding="utf-8") as f:
    data = json.load(f)

while True:

    print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
    print("Sistem Manajemen Inventaris Barang")
    print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
    print("1. Tampilkan stok barang")
    print("2. Tambah data barang")
    print("3. Keluar")
    print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    pilihan = input("Pilih menu 1-3: ")

    if pilihan == "1":
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("\nDAFTAR STOK BARANG")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        
        for barang in data:
            print(f"Kode Barang : {barang['kode']}")
            print(f"Nama Produk : {barang['nama produk']}")
            print(f"Stok Barang : {barang['stok']}")
            print(f"Harga       : {barang['harga']}")
            print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    elif pilihan == "2": 
        nomor_baru = len(data) + 1
        kode_otomatis = f"BN0{nomor_baru}"
        
        produk_baru = input("Masukkan nama produk baru: ")
        stok = input("Masukkan stok produk : ")
        harga = input("Masukkan harga produk : ")
        
        data_baru = {
            "kode": kode_otomatis,
            "nama produk": produk_baru,
            "stok": stok,
            "harga": harga
        }

        data.append(data_baru)
        
        with open("data_barang.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"\n[Berhasil:D] Barang sudah ditambahkan dengan kode: {kode_otomatis}.")

    elif pilihan == "3":
        print("Terimakasih:D")
        break 
        
    else:
        print("Pilihan menu salah!! Silahkan masukkan angka 1, 2, atau 3 yaa:D")