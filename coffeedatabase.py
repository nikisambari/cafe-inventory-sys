import mysql.connector

con=mysql.connector.connect(host='localhost',user="root",passwd='root',database="coffee")
cur=con.cursor()
cur.execute("create table orders(orno int(4) not null AUTO_INCREMENT,TIME varchar(40),subtotal varchar(20),discount varchar(20),GST varchar(20),total varchar(20),primary key(orno))")
con.commit()
#cur.execute("create table customer(Mno bigint(20),Name varchar(40))")
#con.commit()
cur.close()
con.close()
