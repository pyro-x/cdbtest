from fastapi import FastAPI
import psycopg2
app = FastAPI()


hostname ='localhost'
database ='gis'
username ='postgres'
password ='mysecretpassword'
port_id = 5432  # default port for postgres

try:
    conn = psycopg2.connect(host=hostname,database=database,user=username,password=password,port=port_id)
except:
    print("I am unable to connect to the database")


@app.get('/')
async def root():
    return {'pof': 'CartoDB GIS'} 

@app.get('/turnover/')
def turnover():

    cur = conn.cursor()
    cur.execute("SELECT sum(amount) FROM payment_stats")
    for record in cur.fetchall():
        return {'turnover': record}

@app.get ('/turnover_by_position_x_y/{x}/{y}')
def turnover_by_position_x_y(x: int, y: int):
    pass

@app.get('/turnover_fromdate_todate/{fromdate}/{todate}')
def turnover_from_date_to_date(fromdate: str, todate: str):
    print ("from data:" + fromdate)
    cur = conn.cursor()

    try:
        cur.execute("SELECT round(sum(amount)) FROM payment_stats WHERE p_month >= %s AND p_month < %s", (fromdate, todate))
        for record in cur.fetchall():
            return {'turnover': record}
    except Exception as error:
        print ("Error: unable to fetch data")
        print(error)  


@app.get('/turnover/series/{fromdate}/{todate}')
def turnover_series(fromdate: str, todate: str):
    cur = conn.cursor()
    cur.execute("SELECT p_month, round(sum(amount)) FROM payment_stats WHERE p_month >= %s AND p_month < %s GROUP BY p_month", (fromdate, todate))
    records = cur.fetchall()
    return {'turnover': records}


    pass
   
@app.get('/turnover/postal_code/{postal_code}')
def turnover_by_postal_code  (postal_code: str):
    cur = conn.cursor()
    cur.execute("SELECT round(sum(amount)) FROM payment_stats WHERE postal_code = %s", (postal_code))
    for record in cur.fetchall():
        return {'turnover': record}


@app.get('/turnover/postal_code/by_age_and_gender/{postal_code}/')
def turnover_by_postal_code_age_and_gender(postal_code:str):
    cur = conn.cursor()
    cur.execute ('SELECT p_age, p_gender, round(sum(amount)) as agegender_amount FROM payment_stats  GROUP BY p_age,p_gender ')
    records =  cur.fetchall()
    return {'turnover': records}



@app.get('/geo/postal_codes/from_lat_long/{lat}/{long}')
def geo_postal_codes_from_lat_long(lat: float, long: float):
    pass
