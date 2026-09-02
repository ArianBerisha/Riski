@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  start "RISK-i local server" /min cmd /c "py -m http.server 8783 --bind 127.0.0.1"
) else (
  where python >nul 2>nul
  if errorlevel 1 (
    echo Python was not found. Install Python 3 or start another local web server in this folder.
    pause
    exit /b 1
  )
  start "RISK-i local server" /min cmd /c "python -m http.server 8783 --bind 127.0.0.1"
)
powershell -NoProfile -Command "Start-Sleep -Milliseconds 900; Start-Process 'http://127.0.0.1:8783/'"
endlocal
