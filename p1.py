from sqlite3 import * 
con = None
try:
	con =  connect('bmi.db') 
	cursor = con.cursor()
	sql = "select count(*) from bmi"
	count = cursor.execute(sql)
	p =  len(cursor.fetchall())
	print(p)
	con.commit()
except Exception as e:
	print('Failure', e)
