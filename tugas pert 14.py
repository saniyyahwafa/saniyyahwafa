from prettytable import PrettyTable

class Mahasiswa:
 def __init__(self, nm, no_induk, jurusan):
  self.nama = str(nm);
  self.nim = str(no_induk);
  self.prodi = str(jurusan);

 def getNama(self):
  return self.nama;

 def getNim(self):
  return self.nim;
 
 def getProdi(self):
  return self.prodi;

 def setNama(self, nm):
  self.nama = nm;

 def setNim(self, no_induk):
  self.nim = no_induk;
 
 def setProdi(self, jurusan):
  self.prodi = jurusan;


DftrMhs = {};
loop = True;


print("===================================");
print("=         Daftar Mahasiswa        =");
print("===================================");
print("= # MENU                          =");
print("= 1. Tambah Mahasiswa             =");
print("= 2. Hapus Mahasiswa              =");
print("= 3. Tampilkan Semua Mahasiswa    =");
print("= 4. Cari Mahasiswa               =");
print("= 5. Edit Mahasiswa               =");
print("= 6. Jumlah Total Mahasiswa       =");
print("= 0. Keluar                       =");
print("===================================");

while(loop):
 print("\n\n");
 menu = int(input("Masukan menu : "));
 print("\n")

 if menu == 1:
  nama = str(input("Masukan nama : "));
  nim = str(input("Masukan nim : "));
  prodi = str(input("Masukan prodi : "));
  mhs = Mahasiswa(nama, nim, prodi);
  DftrMhs[nim] = mhs;
 elif menu == 2:
  nim = str(input("Masukan nim : "));
  if(nim in DftrMhs):
   del DftrMhs[nim];
  else:
   print("Data tidak ditemukan!!!");
 elif menu == 3:
  table = PrettyTable(["Nama","NIM", "Prodi"]) 
  for i in DftrMhs:
   table.add_row([DftrMhs[i].getNama(), DftrMhs[i].getNim(), DftrMhs[i].getProdi()])
  print(table);
 elif menu == 4:
  nim = str(input("Masukan nim : "));
  if(nim in DftrMhs):
   print("Nama : ", DftrMhs[nim].getNama());
   print("Nim : ", DftrMhs[nim].getNim());
   print("Prodi : ", DftrMhs[nim].getProdi());
  else:
   print("Data tidak ditemukan!!!");
 elif menu == 5:
  nim = str(input("Masukan nim : "));
  if(nim in DftrMhs):
   namaBaru = str(input("Masukan Nama Baru : "));
   DftrMhs[nim].setNama(namaBaru);
   nimBaru = str(input("Masukan NIM Baru : "));
   DftrMhs[nim].setNim(nimBaru);
   prodiBaru = str(input("Masukan Prodi Baru : "));
   DftrMhs[nim].setProdi(prodiBaru);
   mhs = DftrMhs[nim];
   DftrMhs[nimBaru] = mhs;
   del DftrMhs[nim];
  else:
   print("Data tidak ditemukan!!!");
 elif menu == 6:
  print("Jumlah Mahasiswa : ", len(DftrMhs));
 elif menu == 0:
  loop = False;
 else:
  print("Kode Tidak Ditemukan");
