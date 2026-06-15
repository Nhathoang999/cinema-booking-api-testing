@echo off
echo Installing Newman dependencies...
call npm install

echo.
echo Running Postman Automation Suite...
mkdir reports 2>nul
call npm test
