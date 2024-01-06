# Input nilai
nilai_ipk = float(input("Masukkan nilai IPK: "))
nilai_toefl = int(input("Masukkan nilai TOEFL: "))

# Proses seleksi
if nilai_ipk >= 3.5 and nilai_toefl >= 550:
    print("Selamat, Anda berhak mendapatkan beasiswa!")
else:
    print("Maaf, Anda belum berhak mendapatkan beasiswa.")