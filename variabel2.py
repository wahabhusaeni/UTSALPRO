#// UTS Algoritma dan Pemrograman //
data = {
    'nama_lengkap': "Muhamad Wahab Husaeni",          # string
    'tempat_tanggal_lahir': "Bogor, 01 Januari 2006", # string
    'jenis_kelamin': "Laki-laki",                     # string 
    'alamat_lengkap': "Jl. Pasir Muncang",            # string
    'no_hp': 88811112222,                             # integer
    'penghasilan_sebulan': 20000000                   # integer
}

def perkenalan():
    print("Assalamu’alaikum")
    print("Izinkan saya memperkenalkan diri \n")
    print(f"Nama Lengkap            : {data['nama_lengkap']}")
    print(f"Tempat & Tanggal Lahir  : {data['tempat_tanggal_lahir']}")
    print(f"Jenis Kelamin           : {data['jenis_kelamin']}")
    print(f"Alamat Lengkap          : {data['alamat_lengkap']}")
    print(f"No Hp                   : +62{data['no_hp']}")
    print(f"Penghasilan Sebulan     : Rp.{data['penghasilan_sebulan']}")

perkenalan()