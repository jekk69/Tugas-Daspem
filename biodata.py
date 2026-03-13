# ============================================
# Program Biodata + Manipulasi String
# ============================================

# 1. Biodata sederhana dengan input() dan format()
print("=== Program Biodata Sederhana ===")
name = input("Masukkan nama: ")
age = input("Masukkan umur: ")
address = input("Masukkan alamat: ")
province = input("Masukkan provinsi: ")

print("\n=== Biodata Anda ===")
print("Nama: {0}\nUmur: {1}\nAlamat: {2}\nProvinsi: {3}".format(name, age, address, province))

# 2. Manipulasi string "UNIVERSITAS NUSA PUTRA SUKABUMI"
print("\n=== Manipulasi String ===")
kalimat = "UNIVERSITAS NUSA PUTRA SUKABUMI"

# a. putra nusa
print("a.", "putra nusa".title())  # hasil: Putra Nusa

# b. NIVERSITAS NSA PTRA SKABMI (hapus huruf 'U')
print("b.", kalimat.replace("U", ""))

# c. SUKABUMI PUTRA NUSA UNIVERSITAS (dibalik urutan kata)
kata = kalimat.split()
print("c.", " ".join(kata[::-1]))

# d. UNPS (ambil huruf pertama tiap kata)
singkatan = "".join([word[0] for word in kata])
print("d.", singkatan)

# e. TAS SAPU BUMI (ambil huruf terakhir tiap kata)
akhir = "".join([word[-1] for word in kata])
print("e.", akhir)