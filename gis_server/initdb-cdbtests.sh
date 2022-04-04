#!/bin/bash
set -e

export PGUSER="$POSTGRES_USER"
echo "BLA"
echo "${psql[@]}"
echo "CREATING GIS DATABASE"
psql --username "$POSTGRES_USER" <<- 'EOSQL'
create database gis with template template_postgis;
EOSQL

echo "CREATING AND IMPORTING TABLES...321"
psql --username "$POSTGRES_USER" < sql/create_tables.sql gis


