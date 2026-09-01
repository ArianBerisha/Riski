@echo off
cd /d "%~dp0"
where py >nul 2>nul && (set P=py) || (set P=python)
start "RiskAI" /min cmd /c "%P% -m http.server 8782 --bind 127.0.0.1"
powershell -NoProfile -Command "Start-Sleep -Milliseconds 700;Start-Process 'http://127.0.0.1:8782/'"
