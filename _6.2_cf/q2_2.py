from dbconnector import GetCursor

with GetCursor() as cur:
    with GetCursor() as subcur:
        cur.execute('SELECT DISTINCT uid FROM rating')
        for user in cur:
            subcur.callproc('apred', (user[0],))
            for res in subcur.stored_results():
                print(res.fetchall())
