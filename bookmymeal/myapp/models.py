import MySQLdb

db=MySQLdb.connect('localhost','root','root','mypython23')

cursor=db.cursor()

print('connection done....')

