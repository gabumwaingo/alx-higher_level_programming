#!/bin/bash
#sends a post request and dislays the body of the response
email="test@gmail.com"; subject="I will always be here for PLD"; response=$(curl -s -X POST -d "email=$email&subject=$subject" "$1"); echo -n "$response"
