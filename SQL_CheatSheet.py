import pymysql

database = pymysql.connect("ictceweb.ict.sait.ca", "instructors", "con Ed", "cprg104")
cursor = database.cursor()

sql = 'UPDATE `SQL_ex` SET `lname` = "Ekky-ekky-ekky-ekky-z\'Bang, zoom-Boing, z\'nourrrwringnmmm"  WHERE `fname` = "Knights who say"'
cursor.execute(sql)
database.commit()

# sql = 'ALTER TABLE `SQL_ex` ADD PRIMARY KEY (ID)'
# cursor.execute(sql)
# database.commit()

##########INSERT##########
# sql = 'INSERT INTO `SQL_ex`(`fname`, `lname`, `dob`) VALUES("{}", "{}", "{}")'.format("steve", "rogers", "1918-07-04")
# cursor.execute(sql)
# database.commit()


# sql = 'INSERT INTO `SQL_ex`(`fname`, `lname`, `dob`) VALUES("{}", "{}", "{}")'.format("Knights who say", "Ni", "1970-01-01")
# cursor.execute(sql)
# database.commit()


##########VERSION##########
# sql = "SELECT VERSION()"
# cursor.execute(sql)
# result = cursor.fetchone()
# print(result)


database.close()