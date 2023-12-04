# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import psycopg2
import time

def importDB(*args):
    # Database connection
    conn = psycopg2.connect(dbname='APP', user='MCL1021', password='FloMar.07-23$')
    cur = conn.cursor()
    print("Connection to the DB")

    # Create table if not exists	
    cur.execute("CREATE TABLE IF NOT EXISTS Meteo (id SERIAL PRIMARY KEY, Date character varying(20), Day character varying(20), Temp_Max character varying(20), Temp_Min character varying(20), Wind character varying(20), Pluie character varying(20), Ensoleillement character varying(20));")
    
    # Data insertion
    cur.execute("INSERT INTO Meteo (Date, Day, Temp_Max, Temp_Min, Wind, Pluie, Ensoleillement) VALUES (%s, %s, %s, %s, %s, %s, %s)", (args))

    # Closing database connection
    conn.commit()
    cur.close()
    conn.close()
    print("Database logout")
    time.sleep(3)


# Instance Driver object
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define the URL and load
url = "https://www.meteoblue.com/fr/meteo/semaine/thielle-wavre_suisse_2658383?day=1"
driver.get(url)

# Set maximum time to load the web page in seconds
driver.implicitly_wait(10)

# Get elements
data = driver.find_element(By.ID, "day1")

for elem in driver.find_elements(By.XPATH, '//time[@class="date"]'):
    date = elem.get_attribute('datetime')
    break
   
day = driver.find_element(By.XPATH, '//time[@class="date"]/div[1]').text
tmax = driver.find_element(By.XPATH, '//div[@class="temps"]/div[1]').text
tmin = driver.find_element(By.XPATH, '//div[@class="tab-temp-min"]').text
wind = driver.find_element(By.XPATH, '//div[@class="wind"]').text
preci = driver.find_element(By.XPATH, '//div[@class="tab-precip"]').text
sun = driver.find_element(By.XPATH, '//div[@class="tab-sun"]').text

# Call function to load into the DB
importDB(date, day, tmax, tmin, wind, preci, sun)