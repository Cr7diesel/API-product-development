#!/bin/sh

export PGUSER="postgres"

psql -c "CREATE DATABASE newdb"

psql newdb -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"