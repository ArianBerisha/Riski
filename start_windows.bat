@echo off
cd /d "%~dp0"
start "" http://127.0.0.1:8783/
py -m http.server 8783
