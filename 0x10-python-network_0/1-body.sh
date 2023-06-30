#!/usr/bin/env bash
#displays the body of the response of a url
url=$1
response=$(curl -s -o /dev/null -w "%{Content-Type}" "url")
echo "$response"
