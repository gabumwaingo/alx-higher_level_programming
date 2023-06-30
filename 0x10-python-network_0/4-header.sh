#!/bin/bash
#sends GET request to url and displays the response body
echo -n "$(curl -s -H "X-School-User-Id: 98" "$1")"
