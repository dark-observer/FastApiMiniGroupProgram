#!/bin/bash

HOST=0.0.0.0
PORT=8000
VIR=venv

cd /home/ubuntu/code/FastApiMiniGroupProgram
source $VIR/bin/activate

exec $VIR/bin/nvicorn main:app --host $HOST --port $PORT --reload