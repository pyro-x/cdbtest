from fastapi import FastAPI,Depends
from fastapi_asyncpg import configure_asyncpg


app = FastAPI()

dsn ="postgresql://postgres:mysecretpassword@localhost/gis"
db = configure_asyncpg(app,dsn)
@db.on_init
async def initialization(conn):
    # force to have this initiator or it won't configure itself properly
    await conn.execute("SELECT 1")

@app.on_event("startup")
async def startup():
    print ("Starting up ....")

@app.get('/')
async def root():
    return {'pof': 'CartoDB GIS'} 

@app.get('/turnover/')
async def turnover(db=Depends(db.connection)):

    record = await db.fetch("SELECT round(sum(amount)) FROM payment_stats")
    return {'turnover': record}


@app.get('/turnover_fromdate_todate/{fromdate}/{todate}')
async def turnover_from_date_to_date(fromdate: str, todate: str,db=Depends(db.connection)):
    print ("from data:" + fromdate)
    record = await db.fetch ("SELECT round(sum(amount)) FROM payment_stats WHERE p_month >= $1 AND p_month <= $2", fromdate, todate)
    return {'turnover': record}
    


@app.get('/turnover/series/{fromdate}/{todate}')
async def turnover_series(fromdate: str, todate: str,db=Depends(db.connection)):
    record = await db.fetch ("SELECT p_month as month, round(sum(amount)) as total FROM payment_stats WHERE p_month >= $1 AND p_month < $2 GROUP BY p_month", fromdate, todate)
    return {'turnover': record}

@app.get('/turnover/postal_code/{postal_code}')
async def turnover_by_postal_code  (postal_code: str,db=Depends(db.connection)):
    record = await db.fetch ("select round(sum(ps.amount)) from payment_stats as ps, postal_codes as pc where ps.postal_code_id = pc.id and pc.code=$1", (postal_code))
    return {'turnover': record}


@app.get('/turnover/postal_code/by_age_and_gender/{postal_code}/')
async def turnover_by_postal_code_age_and_gender(postal_code:str,db=Depends(db.connection)):
    record = await db.fetch ("SELECT p_age, p_gender, round(sum(amount)) as agegender_amount FROM payment_stats  GROUP BY p_age,p_gender")
    return {'turnover': record}



@app.get('/geo/postal_codes/from_lat_long/{lat}/{long}')
def geo_postal_codes_from_lat_long(lat: float, long: float):
    pass
