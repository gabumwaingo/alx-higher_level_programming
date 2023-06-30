#!/bin/bash
if [[ $# -ne 1 ]]; then echo "Usage: $0 <URL>"; exit 1; fi
curl -s -o /dev/null -w "%{size_download}\n" "$1"
