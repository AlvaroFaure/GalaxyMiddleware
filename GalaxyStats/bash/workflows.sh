#!/bin/sh

OUT=$1

if [ $# != 1 ]; then
       echo "***ERROR*** Use: processes output"
       exit -1
fi       

psql -U galaxy-bitlab -d galaxy-bitlab -c "SELECT wi.id, wi.create_time, w.name, wi.workflow_step_id FROM workflow_invocation_step wi INNER JOIN workflow w ON wi.workflow_invocation_id = w.id ORDER BY wi.create_time;" > $1

