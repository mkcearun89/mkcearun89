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

insert_script = 'INSERT INTO DEP (depid, dept_name) VALUES (%s, %s)'
insert_values = (10, 'fsdcg')
cur.execute(insert_script,insert_values)

conn.commit()

cur.close()
conn.close()
