#!/bin/bash
# Sends JSON post request
curl -sX "$1" POST -H "Content-Type: application/json" -d "$(cat "$2")"
