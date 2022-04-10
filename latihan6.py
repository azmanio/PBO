import psycopg2 as db
con = None
connected = None
cursor = None

def connect():
	global connected
	global con
	global cursor
	try:
		con = db.connect(
			host = "localhost",
			database = "umc",
			port = 5432,
			user = "azis",
			password = "123"
		)
		cursor = con.cursor()
		connected = True
	except:
		connected = False
	return cursor

def disconnect():
	global connected
	global con
	global cursor
	if(connected==True):
		cursor.close()
		con.close()
	else:
		con = None
	connected = False
	
def Tampil(sql):
	a = connect()
	a.execute(sql)
	record = a.fetchall()
	if a.rowcount < 0:
		print("Tidak ada data")
	else:
		print("Data yang Tersimpan:")
		for data in record:
				print(data)

def Entry():
	global connected
	global con
	global cursor
	xnim = input("Masukkan NIM: ")
	xnama = input("Masukkan Nama Lengkap: ")
	xidfk = input("Masukkan ID Fakultas (1...5): ")
	xidpr = input("Masukkan ID Prodi (1...10): ")
	a = connect()
	sql = "insert into mahasiswa (nim, nama, idfakultas, idprodi) values ('"+xnim+"','"+xnama+"','"+xidfk+"','"+xidpr+"')"
	a.execute(sql)
	con.commit()
	print("Entry is done.")
	
def Cari():
	global connected
	global con
	global cursor
	xnim = input("Masukkan NIM yang dicari: ")
	a = connect()
	sql = "select * from mahasiswa where nim = '" + xnim + "'"
	a.execute(sql)
	record = a.fetchall()
	print(record)
	print("Search is done.")
	
def Ubah():
	global connected
	global con
	global cursor
	xnim = input("Masukkan NIM yang dicari: ")
	a = connect()
	sql = "select * from mahasiswa where nim = '" + xnim + "'"
	a.execute(sql)
	record = a.fetchall()
	print("Data saat ini :")
	print(record)
	row = a.rowcount
	if(row==1):
		print("Silahkan untuk mengubah data...")
		xnama = input("Masukkan Nama Lengkap: ")
		xidfk = input("Masukkan ID Fakultas (1...5): ")
		xidpr = input("Masukkan ID Prodi (1...10): ")
		a = connect()
		sql = "update mahasiswa set nama ='" + xnama + "', idfakultas='" + xidfk + "', idprodi='" + xidpr + "' where nim='" + xnim + "'"
		a.execute(sql)
		con.commit()
		print("Update is done.")
		sql = "select * from mahasiswa where nim = '" + xnim + "'"
		a.execute(sql)
		rec = a.fetchall()
		print("Data setelah diubah :")
		print(rec)
	
	else:
		print("Data tidak ditemukan...")
		
def Hapus():
	global connected
	global con
	global cursor
	xnim = input("Masukkan NIM yang dicari: ")
	a = connect()
	sql = "select * from mahasiswa where nim = '" + xnim + "'"
	a.execute(sql)
	record = a.fetchall()
	print("Data saat ini :")
	print(record)
	row = a.rowcount
	if (row==1):
		jwb = input("Apakah ingin menghapus data? (y/t): ")
		if(jwb.upper()=="Y"):
			a = connect()
			sql = "delete from mahasiswa where nim = '" + xnim + "'"
			a.execute(sql)
			con.commit()
			print("Delete is done.")
		else:
			print("Data batal untuk dihapus.")
	else:
		print("Data tidak ditemukan...")
		
def show_menu(sql):
	print("\n=== APLIKASI DATABASE PYTHON ===")
	print("1. Insert Data")
	print("2. Tampilkan Data")
	print("3. Update Data")
	print("4. Hapus Data")
	print("5. Cari Data")
	print("0. Keluar")
	print("------------------")
	menu = input("Pilih Menu: ")
	a = connect()
	if menu == "1":
		Entry()
	elif menu == "2":
		Tampil(sql)
	elif menu == "3":
		Ubah()
	elif menu == "4":
		Hapus()
	elif menu == "5":
		Cari()
	elif menu == "0":
		exit()
	else:
		print("Menu salah!")


if __name__ == "__main__":
	while(True):
		sql = "select * from mahasiswa"
		show_menu(sql)