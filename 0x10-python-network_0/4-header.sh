#!/bin/bash
#sends a GET request to the URL, set custom header and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
