#!/bin/bash
# Sends request returns status code
curl -s -o /dev/null -w %{http_code} $1
