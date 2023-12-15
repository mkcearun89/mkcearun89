import psycopg2
conn = psycopg2.connect("host=localhost dbname=master user=postgres password=Jaisriram@123")
cur = conn.cursor()
with open('department.csv', 'r') as f:
    # Notice that we don't need the csv module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'dep', sep=',')

conn.commit()
cur.close()
conn.close()
