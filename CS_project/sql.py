from sys import exec_prefix
import pandas as pd
from mysql.connector import Error
import mysql.connector as msq



# class Database:

#     def __init__(self, host_name, user_name, user_password, db_name):
#         self.host = host_name,
#         self.user = user_name,
#         self.pwd = user_password,
#         self.db = db_name

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = msq.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print(f"MySQL Database connection successfully connected to ({db_name})")
    except Error as err:
        print(f"Error: '{err}'")    

    return connection


def create_database(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE {db_name}")
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # print("Query successful")
        for x in cursor:
            print(x)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")


def insert_data(connection, table, data):
    cursor = connection.cursor()
    try:
        # provide data in (), (), () format
        cursor.execute(f"INSERT INTO {table} VALUES {data}")
        connection.commit()
        print('Data Entry Added')
        for x in cursor:
            print(x)
    except Error as err:
        print(f"Error: '{err}'")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def pd_data_view(results):
    # Returns a list of lists and then creates a pandas DataFrame
    from_db = []

    for result in results:
        result = list(result)
        from_db.append(result)


    columns = ["Patient_ID", "Name", "language", "Age", "Gender"]
    df = pd.DataFrame(from_db)
    print(df)


#---------------------------------------------------------

TABLES = {}

TABLES['Patients'] = (
    """
    CREATE TABLE Patients (
        Patient_ID int PRIMARY KEY,
        Name varchar(50) NOT NULL,
        Age int,
        Date_of_admit date NOT NULL,
        Gender enum('M', 'F') NOT NULL,
        Weight int,
        Height int,
        Concern varchar(400) NOT NULL,
        Diagnostics varchar(200),
        Medications varchar(250)  
    )
    """
)

#---------------------------------------------------------

if __name__ == "__main__":
    con = create_server_connection('localhost', 'root', 'normandy', 'HOSPITAL')
    # insert_data(con, 'Patients', (4,'Girija', 40, "2018-09-15", 'F', 70, 160, 'test', 'demo', 'none'))

    # sql = '''
    # INSERT INTO Patients (Patient_ID, Name, Age, Date_of_admit, Gender, weight, Height, Concern, Diagnostics, Medications) 
    # VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    # '''

    # patients = [
    #     (1, 'Samarth', 18, '2014-08-09', 'M', 80, 178, 'none', 'none', 'none'),
    #     (2, 'Shashank', 17, '2014-05-09', 'M', 70, 180, 'none', 'none', 'none'),
    #     (3, 'Girija', 45, '2014-09-09', 'F', 80, 165, 'none', 'none', 'none')
    # ]

    # execute_list_query(con, sql, patients)

    # testing database using fake data
    
    from faker import Faker 
    import random
    f = Faker('en_IN')

    
    sql = '''
    INSERT INTO Patient_test (Patient_ID, Name, Age, Date_of_admit, contact) 
    VALUES (%s, %s, %s, %s, %s)
    '''
    # execute_query(con, 'CREATE TABLE patient_test (Patient_ID int PRIMARY KEY, Name varchar(50), Age int, Date_of_admit date, contact int)')
    
    patients = []
    
    for i in range(1, 100):
        t = (i, f.name(), random.randint(3, 79), f.date_between_dates(date_start='-1y', date_end='+5m'), f.phone_number())
        patients.append(t)

    # print(patients)
    execute_list_query(con, sql, patients)
    

    rs = read_query(con, "SELECT * FROM Patients")   # reading data
    for i in rs:
        print(i)
    con.close()



