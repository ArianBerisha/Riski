#!/bin/sh
cd "$(dirname "$0")" || exit 1
python3 -m http.server 8783 --bind 127.0.0.1 &
sleep 1
open "http://127.0.0.1:8783/"
