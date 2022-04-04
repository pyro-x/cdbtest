FROM postgis/postgis

COPY sql sql
COPY data data
COPY ./initdb-cdbtests.sh /docker-entrypoint-initdb.d/cdbtest.sh
RUN chmod 777 sql
run chmod 777 data
RUN chmod +x /docker-entrypoint-initdb.d/cdbtest.sh