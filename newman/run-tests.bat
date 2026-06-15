@echo off
echo ====================================================
echo Starting Cinema Booking API Automated Tests (Newman)
echo ====================================================

REM Check if node is installed
node -v >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Node.js is not installed. Please install Node.js first.
    pause
    exit /b
)

echo Installing dependencies if missing...
call npm install

echo.
echo Running Postman Collection...
call npx newman run ../Cinema_Booking_API.postman_collection.json ^
  --env-var "baseUrl=http://localhost:8000" ^
  -r cli,htmlextra ^
  --reporter-htmlextra-export ./reports/report.html

echo.
echo ====================================================
echo Test execution complete!
echo Your detailed HTML report is saved in the 'reports' folder.
echo ====================================================
pause
