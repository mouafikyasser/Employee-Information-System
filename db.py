import sqlite3
class Database:
    #create table of data
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id  Integer Primary Key ,
            name text ,
            age text ,
            job text ,
            email text ,
            gender text ,
            contact text ,
            address text 
        )
        """

        self.cur.execute(sql)
        self.con.commit()


    #add new employee
    def insert(self,name,age,job,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",
                         (name,age,job,email,gender,contact,address))
        self.con.commit()
    

    #send list data of employee
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows
    

    #delete a employee
    def remove(self,id):
        self.cur.execute("delete from employees where id=?" ,(id,))
        self.con.commit()


    #update information of employee
    def update(self,id,name,age,job,email,gender,contact,address):
        self.cur.execute("update employees set name=? ,age=? ,job=? ,email=? ,gender=? ,contact=? ,address=? where id=?" ,
                         (name,age,job,email,gender,contact,address, id))
        self.con.commit()
    

