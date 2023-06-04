#!/bin/bash

# Set database credentials
DB_HOST="192.168.1.41"
DB_PORT="8989"
DB_USER="root"
DB_PASS="root"
DB_NAME="sales"

# Dump data to SQL file
mysqldump -h $DB_HOST -P $DB_PORT -u $DB_USER -p$DB_PASS $DB_NAME sales_data > sales_data.sql

# Check if the export was successful
if [ $? -eq 0 ]; then
  echo "Data export successful. File 'sales_data.sql' created."
else
  echo "Error exporting data."
fi
