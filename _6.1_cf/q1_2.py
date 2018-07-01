import pandas as pd
from dbconnector import GetCursor

df = pd.read_table('user_artists.dat')
values = df.values.tolist()

with GetCursor() as cur:
    sql = 'INSERT INTO rating (uid, aid, weight) VALUES (%s, %s, %s)'
    cur.executemany(sql, values)
