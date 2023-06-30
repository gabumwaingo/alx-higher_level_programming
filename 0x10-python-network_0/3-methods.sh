#!/bin/bash
# Display all acceptable HTTP methods to the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
