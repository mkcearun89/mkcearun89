import psycopg2

host_name = 'localhost'
db = 'master'
username = 'postgres'
pw = 'Jaisriram@123'
port_name = 5432


conn = psycopg2.connect(
        host=host_name,
        dbname=db,
        user=username,
        password=pw,
        port=port_name)
cur = conn.cursor()
create_script = '''CREATE TABLE IF NOT EXISTS DEP (
                        depid int PRIMARY KEY,
                        dept_name varchar(40) NOT NULL)'''
cur.execute(create_script)
conn.commit()
cur.close()
conn.close()





