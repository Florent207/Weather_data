import pandas as pd
import psycopg2
import streamlit as st

'''def getDatas():
    # Database connection
    conn = psycopg2.connect(dbname='dbname', user='users', password='password')
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
    print("Database logout")'''



st.title('Uber pickups in NYC')

DATE_COLUMN = 'date'
DATA_URL = ('DATA.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, encoding='latin1', nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(5)
data_load_state.text("Done!")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Some number in the range 0-23
day_to_filter = st.slider('day', 0, 5, 1)
filtered_data = data[data[DATE_COLUMN].dt.day == day_to_filter]

st.subheader('Essai filter' % day_to_filter)
st.map(filtered_data)


#getDatas()
