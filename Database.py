import psycopg2	



def insert_vendor(Username, Password, CompanyName, Address):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO Vendors(Username, Password, CompanyName, Address, AccountBalance)
             VALUES(%s, %s, %s, %s, %s) RETURNING VendorID;"""
    conn = None
    vendor_id = None
    try:
        
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database="dawgfood", user="postgres", password="INFOcapstone")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (Username, Password, CompanyName, Address, 0.0))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return(vendor_id)


# assuming that the account balance is zero because they are creating their profile
def insert_student(Username, Password, FirstName, LastName, EmailAddress):
    sql = """INSERT INTO Students(Username, Password, FirstName, LastName, EmailAddress, AccountBalance)
             VALUES(%s, %s, %s, %s, %s, %s) RETURNING StudentID;"""
    conn = None
    vendor_id = None
    try:
        
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database="dawgfood", user="postgres", password="INFOcapstone")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (Username, Password, FirstName, LastName, EmailAddress, 0.0))
        # get the generated id back
        student_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return(student_id)

# example inserting the student
#insert_student('user', 'pass', 'Andrea', 'Koozer', 'k@hotmail.com')


def is_student(Username, Password):
    conn = None
    try:
        sql = '''SELECT * FROM Students Where Username = %s and Password = %s'''
        conn = psycopg2.connect(database="dawgfood", user="postgres", password="INFOcapstone")
        cur = conn.cursor()
        cur.execute(sql, (Username, Password))

        row = cur.fetchone()
        if row is None:
            return False
        else: 
            return True
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#is_student('user', 'pass')


def is_vendor(Username, Password):
    conn = None
    try:
        sql = '''SELECT * FROM Vendors Where Username = %s and Password = %s'''
        conn = psycopg2.connect(database="dawgfood", user="postgres", password="INFOcapstone")
        cur = conn.cursor()
        cur.execute(sql, (Username, Password))

        row = cur.fetchone()
        if row is None:
            return False
        else: 
            return True
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()