#!/bin/bash
#sends GET request to url and displays the response body

url=$1
header="X-School-User-Id: 98"
response=$(curl -s -H "$header" "$url")
echo -n "$response"
