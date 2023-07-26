#!/bin/bash
#Sends DELETE request and prints response body
echo -n "$(curl -s -X DELETE "$1")"
