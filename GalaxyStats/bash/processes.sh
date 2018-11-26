#!/bin/sh

OUT=$1

if [ $# != 1 ]; then
       echo "***ERROR*** Use: processes output"
       exit -1
fi       

psql -U galaxy-bitlab -d galaxy-bitlab -c "SELECT j.id,j.create_time,j.tool_id,j.exit_code FROM job j ORDER BY j.create_time;" > $1
