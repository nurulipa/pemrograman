def hitung_bmi(berat_badan, tinggi):
    48bmi = berat_badan / (tinggi ** 2)
    return bmi

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi (cm): "))

bmi = hitung_bmi(berat, tinggi)
print("BMI Anda adalah:", bmi)