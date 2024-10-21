#!/usr/local/bin/python
# Connect to MariaDB Platform
import mysql.connector #mariadb

try:
	conn = mysql.connector.connect(
		user="root",
		password="",
		host="localhost",
		port=3306,
		database="test"
	)

except mysql.connector.Error as e: # mariadb.Error as e:
	print(e)
	print("Error connecting to DB")
	exit(1)

cursor=conn.cursor(dictionary=True)
def add(data):
	sql=""
	param=()
	cursor.execute(sql,param)
	return
	
def delete(id):
	sql=""
	cur.execute(sql,(id,))
	return

def update(id,data):
	sql=""
	param=()
	cursor.execute(sql,param)
	return
	
def getList():
	sql=""
	cursor.execute(sql)
	return cursor.fetchall()


