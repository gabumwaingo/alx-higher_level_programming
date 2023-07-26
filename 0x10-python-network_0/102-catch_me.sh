#!/bin/bash
#Sends a rewuest to the server and server responds with you got me
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
