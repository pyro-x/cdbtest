use database gis ;

/* table creation */
CREATE TABLE postal_codes ( 
    the_geom geometry,
    code VARCHAR(5),
    id INTEGER PRIMARY KEY

);

CREATE TABLE payment_stats (
    amount FLOAT,
    p_month VARCHAR(10),
    p_age VARCHAR(6),
    p_gender VARCHAR(1),
    postal_code_id integer,
    id integer primary key
);
create index postal_code_pk on payment_stats(postal_code_id);

/* import the postal_codes into the table using copy */
\copy payment_stats (ammount,p_month,p_age,p_gender,postal_code_id,id) from 'payment_stats.csv' (format csv, header, delimiter ',')

\copy postal_codes (the_geom,code,id) from 'postal_codes.csv' (format csv, header, delimiter ',')
