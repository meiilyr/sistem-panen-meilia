def hitung_total_panen(jumlah_kg, harga_per_kg):
    return jumlah_kg * harga_per_kg


jumlah_panen = 100
harga_per_kg = 5000

total = hitung_total_panen(jumlah_panen, harga_per_kg)

print("Total hasil panen:", total)