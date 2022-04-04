from fastapi import FastAPI,Depends,HTTPException,status
from fastapi_asyncpg import configure_asyncpg


app = FastAPI()

dsn ="postgresql://postgres:cdbtest@localhost/gis"
db = configure_asyncpg(app,dsn)
@db.on_init
async def initialization(conn):
    # had to have this initiator or it won't configure itself properly
    await conn.execute("SELECT 1")

@app.on_event("startup")
async def startup():
    print ("Starting up ....")

@app.get('/')
async def root():
    return {'pof': 'CartoDB GIS'} 

@app.get('/turnover/')
async def turnover(db=Depends(db.connection)):
    record = await db.fetch("SELECT round(sum(amount)) as amount FROM payment_stats")
    return {'turnover': record}


@app.get('/turnover_fromdate_todate/{fromdate}/{todate}')
async def turnover_from_date_to_date(fromdate: str, todate: str,db=Depends(db.connection)):
    print ("from data:" + fromdate)
    record = await db.fetch ("SELECT round(sum(amount)) as amount FROM payment_stats WHERE p_month >= $1 AND p_month <= $2", fromdate, todate)
    return {'turnover': record}


@app.get('/turnover/series/{fromdate}/{todate}')
async def turnover_series(fromdate: str, todate: str,db=Depends(db.connection)):
    record = await db.fetch ("SELECT p_month as month, round(sum(amount)) as amount FROM payment_stats WHERE p_month >= $1 AND p_month < $2 GROUP BY p_month", fromdate, todate)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Cannot find any data for dates range bwetween {fromdate} and {todate}')
    return {'turnover': record}

@app.get('/turnover/postal_code/{postal_code}')
async def turnover_by_postal_code  (postal_code: str,db=Depends(db.connection)):
    record = await db.fetchval ("select round(sum(ps.amount)) as amount from payment_stats as ps, postal_codes as pc where ps.postal_code_id = pc.id and pc.code=$1", postal_code)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Cannot find any data for postal code {postal_code}')
    return {'turnover': record}


@app.get('/turnover/by_age_and_gender/{postal_code}/')
async def turnover_by_postal_code_age_and_gender(postal_code:str,db=Depends(db.connection)):
    record = await db.fetch ("select ps.p_age as age , ps.p_gender as gender,  round(sum(ps.amount)) as amount from payment_stats as ps, postal_codes as pc where ps.postal_code_id = pc.id and pc.code=$1 GROUP BY ps.p_age,ps.p_gender",postal_code)
    # If empty that's because the postalcode was incorrect    
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Cannot find any data for postal code {postal_code}')
    return {'turnover': record}


@app.get('/geo/postal_codes/bounding_box/{min_lat}/{min_lon}/{max_lat}/{max_lon}/')
async def get_postal_codes_by_bounding_box(min_lat: float, min_lon: float, max_lat: float, max_lon: float,db=Depends(db.connection)):
    record = await db.fetch ("SELECT ST_AsGeoJSON(the_geom) as the_geom, code as postal_code from postal_codes where \
                                the_geom && ST_MakeEnvelope ($1,$2,$3,$4)",min_lon,min_lat,max_lon,max_lat)

    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Cannot find any postalcode in that bounding box')
    return {'postal_codes': record}

