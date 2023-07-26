#!/bin/bash
#displays the body of the response of the url
echo -n "$(curl -sL "$1")"
