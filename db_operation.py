import sqlite3

#------------------------------------------- getting admin count id -----------#
def get_aid():
    con = sqlite3.connect('test.db')
    if( con ):
        sql = "SELECT * FROM adminid;"
        result = con.execute( sql )
        for row in result:
            id = row[0]
    return id

#------------------------------------------- getting user count id ------------#
def get_uid():
    con = sqlite3.connect('test.db')
    if( con ):
        sql = "SELECT * FROM userid;"
        result = con.execute( sql )
        for row in result:
            id = row[0]
    return id

#------------------------------ inserting admin data to database --------------#

def admin_insert(id,name,email,aptno,city,state,phn,pw):

    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute( '''INSERT INTO admin (id,name,email,aptno,city,state,phn,pw) VALUES (?,?,?,?,?,?,?,?);''',(id,name,email,aptno,city,state,phn,pw) )
    con.commit()
    con.close()

    #-------------------- incrementing admin count after successful regestration
    id =  id + 1
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute('''UPDATE adminid SET id=%d;'''%(id))
    con.commit()
    con.close()
    return 1
#-------------------------------- inserting user data to database -------------#

def user_insert(id,name,email,aptno,city,state,phn,pw):

    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute( '''INSERT INTO user (id,name,email,aptno,city,state,phn,pw) VALUES (?,?,?,?,?,?,?,?);''',(id,name,email,aptno,city,state,phn,pw) )
    con.commit()
    con.close()

    #-------------------- incrementing user count after successful regestration
    id =  id + 1
    con = sqlite3.connect('test.db')
    c = con.cursor()
    c.execute('''UPDATE userid SET id=%d;'''%(id))
    con.commit()
    con.close()
    return 1

#------------------------------------------------------------------------------#
