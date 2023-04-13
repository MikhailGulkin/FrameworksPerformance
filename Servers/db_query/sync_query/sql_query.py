import psycopg2

conn = psycopg2.connect(
    dbname='SpeedTest',
    user='postgres',
    port='5431',
    password='1234',
    host='localhost'
)
cursor = conn.cursor()