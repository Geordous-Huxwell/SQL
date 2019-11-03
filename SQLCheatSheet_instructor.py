import pymysql

database = pymysql.connect("ictceweb.ict.sait.ca","instructors","con Ed","cprg104")
cursor = database.cursor()


###############Update############################
#sql = "DELETE FROM `jordan` WHERE id = {}".format(2)
#cursor.execute(sql)
#database.commit()


###############UPDATE######################
#sql = 'UPDATE `jordan` SET `fname` = "{}" WHERE `id` = {}'.format("Robert",2)
#cursor.execute(sql)
#database.commit()

###############INSERT#####################
#sql = 'INSERT INTO `jordan`(`fname`,`lname`,`DOB`) VALUES("{}","{}","{}")'.format("Jordan","Doerksen","1980-01-01")
#cursor.execute(sql)
#database.commit()



#############VERSION############
#sql = "SELECT VERSION()"
#cursor.execute(sql)
#result = cursor.fetchone()
#print(result)

sql = 'SELECT * FROM `jordan`'
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
	for data in row:
		print(data , end = '\t')
	print()



database.close()