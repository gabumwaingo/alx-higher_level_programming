#!/bin/bash
#displays the body of the response of a url

url=$1
response=$(curl -sL $url)
echo -n "$response"
