#!/bin/bash
# 0-body_size.sh

URL=$1
response=$(curl -s "$URL")
size=$(echo -n "$response" | wc -c)
echo $size
