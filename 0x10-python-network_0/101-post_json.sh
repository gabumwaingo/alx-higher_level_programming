#!/bin/bash
#Sends a json poat url and displays the body of the response
echo -n "$(curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1")"
