#!/usr/bin/env bash
#Sends DELETE request and prints response body
url=$1
response=$(curl -s -X DELETE $url)
echo -n "$response"
