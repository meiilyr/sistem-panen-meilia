def hitung_total_panen(jumlah_kg, harga_per_kg):
    return jumlah_kg * harga_per_kg


def hitung_diskon(total, persen_diskon):
    return total * persen_diskon / 100


jumlah_panen = 100
harga_per_kg = 5000
persen_diskon = 10

total = hitung_total_panen(jumlah_panen, harga_per_kg)
diskon = hitung_diskon(total, persen_diskon)
total_setelah_diskon = total - diskon

print("Total hasil panen:", total)
print("Diskon:", diskon)
print("Total setelah diskon:", total_setelah_diskon)