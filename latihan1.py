daftarkontak = {
    "nama" : "nomor",
    "ari"  : 6281267888,
    "dina" : 6287677776,    
}
print (daftarkontak["ari"])

daftarkontak.update({"riko": 62087654544})
daftarkontak["dina"]= 6288999776
del daftarkontak["dina"]
print(daftarkontak.keys())
print(daftarkontak.values())
print(daftarkontak.items())