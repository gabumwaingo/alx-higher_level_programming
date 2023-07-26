#!/bin/bash
#Displays only the status code of the response of the url
echo -n "$(curl -s -o /dev/null -w "%{http_code}" "$1")"
