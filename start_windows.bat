@echo off
cd /d "%~dp0"
start "RISK-i" /min cmd /c "py -m http.server 8797 --bind 127.0.0.1"
powershell -NoProfile -Command "Start-Sleep -Milliseconds 700; Start-Process 'http://127.0.0.1:8797/'"
