#!/bin/bash

hostname=$(hostname)

if [[ "$hostname" = "app1" ]];
then
    uvicorn app.api:app --host=0.0.0.0 --port=8000 --reload
elif [[ "$hostname" = "app2" ]];
    then 
        uvicorn app.api:app --host=0.0.0.0 --port=8015 --reload
fi