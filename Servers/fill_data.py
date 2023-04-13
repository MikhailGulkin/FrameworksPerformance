import psycopg2

conn = psycopg2.connect(
    dbname='SpeedTest',
    user='postgres',
    port='5431',
    password='1234',
    host='localhost'
)
cursor = conn.cursor()
cursor.execute(
    """
   CREATE TABLE IF NOT EXISTS Speed
    (
    speed_id INTEGER PRIMARY KEY,  
    speed_1 TEXT, 
    speed_2 TEXT, 
    speed_3 TEXT
    ) 
    """
)


def generate_queries(number_records: int = 1_000_000) -> str:
    return ','.join([
        f"""({i}, 'speed_{i + 1}', 'speed_{i + 2}', 'speed_{i + 3}')"""
        for i in range(number_records)]
    )


cursor.execute(
    f"""
          INSERT INTO Speed (speed_id, speed_1, speed_2, speed_3) VALUES
          {generate_queries()};
          """
)

conn.commit()
