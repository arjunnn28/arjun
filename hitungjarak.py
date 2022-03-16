def Jarak(Kecepatan, Waktu):
    Jarak = Kecepatan*Waktu
    return Jarak
Kecepatan = int(input('Kecepataan kendaraan (km/jam): '))
Waktu = int(input('Waktu tempuh (jam): '))
print(f'Jarak kota A ke kota B adalah {Jarak(Kecepatan, Waktu)} km')