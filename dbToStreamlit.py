import pandas as pd
import psycopg2

def getDatas():
    # Database connection
    conn = psycopg2.connect(dbname='APP', user='MCL1021', password='FloMar.07-23$')
    cur = conn.cursor()
    print("Connection to the DB")

    cur.execute("SELECT * FROM public.meteo")

    # Export to csv
    fid = open('DATA.csv', 'w')
    sql = "COPY (SELECT * FROM meteo) TO STDOUT WITH CSV HEADER"
    cur.copy_expert(sql, fid)
    fid.close()

    # Closing database connection
    conn.commit()
    cur.close()
    conn.close()
    print("Database logout")

    # Cleaning file
    file = 'C:\\Database\\Exercices\\DATA.csv'
    df = pd.read_csv(file, encoding='unicode_escape')
    df.drop(columns = ['id'], inplace = True)
    df.to_csv('C:\\Database\\Exercices\\DATA_2.csv')


getDatas()