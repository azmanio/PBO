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

def insert_data():
	global connected
	global con
	global cursor
	nama = input("Masukan Nama: ")
	nim = input("Masukan NIM: ")
	kelas = input("Masukan Kelas: ")
	a = connect()
	sql = "insert into dataKelas (nim, nama, kelas) values ('"+nim+"','"+nama+"','"+kelas+"')"
	a.execute(sql)
	con.commit()
	print("Data Berhasil Disimpan.")

def show_data(sql):
	a = connect()
	a.execute(sql)
	results = a.fetchall()
 
	if a.rowcount < 0:
		print("Tidak ada data")
	else:
		print("Data yang Tersimpan:")
		for data in results:
				print(data)

def update_data(sql):
	global connected
	global con
	global cursor
	a = connect()
	print("Data Tersedia: ")
	show_data(sql)
	nim = input("Masukkan NIM: ")
	sql = "select * from dataKelas where nim = '" + nim + "'"
	a.execute(sql)
	row = a.rowcount
	if (row==1):
		print("Data Ditemukan:")
		print(a.fetchall())
		print("Silahkan untuk mengubah data...")
		nama = input("Nama Baru: ")
		kelas = input("Kelas Baru: ")
		a = connect()
		sql = "update dataKelas set nama = '" + nama + "', kelas='" + kelas + "' where nim='" + nim + "'"
		a.execute(sql)
		con.commit()
		print("Data Berhasil Diubah.")
	else:
		print("Data Tidak Ditemukan.")

def delete_data(sql):
	global connected
	global con
	global cursor
	show_data(sql)
	a = connect()
	nim = input("Masukkan NIM yang Ingin Dihapus: ")
	sql = "delete from dataKelas where nim = '" + nim + "'"
	a.execute(sql)
	con.commit()
	print("Data Berhasil Dihapus.")

def search_data():
	global connected
	global con
	global cursor
	a = connect()
	nim = input("Masukkan NIM: ")
	sql = "select * from dataKelas where nim = '" + nim + "'"
	a.execute(sql)
	results = a.fetchall()
	
	if a.rowcount < 1:
		print("Data Tidak Ditemukan")
	else:
		print("Data Ditemukan:")
		for data in results:
			print(data)

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
		insert_data()
	elif menu == "2":
		show_data(sql)
	elif menu == "3":
		update_data(sql)
	elif menu == "4":
		delete_data(sql)
	elif menu == "5":
		search_data()
	elif menu == "0":
		exit()
	else:
		print("Menu salah!")


if __name__ == "__main__":
	while(True):
		sql = "select * from dataKelas"
		show_menu(sql)