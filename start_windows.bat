@echo off
cd /d "%~dp0"
start "RiskAI" /min cmd /c "py -m http.server 8792 --bind 127.0.0.1"
powershell -NoProfile -Command "Start-Sleep -Milliseconds 700; Start-Process 'http://127.0.0.1:8792/'"
