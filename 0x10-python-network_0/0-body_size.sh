#!/usr/bin/env bash
# Displays the size of the body of the response

# Check if a URL is provided as an argument
if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL from the command-line argument
url=$1

# Send the request using curl and capture the response body
response=$(curl -s -o /dev/null -w "%{size_download}" "$url")

# Display the size of the response body in bytes
echo "$response"
