#!/bin/bash
# Returns body size

curl -s "$1" | wc -c
