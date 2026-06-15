#!/bin/bash

echo "===================================================="
echo "Starting Cinema Booking API Automated Tests (Newman)"
echo "===================================================="

# Check if node is installed
if ! command -v node &> /dev/null
then
    echo "[ERROR] Node.js is not installed. Please install Node.js first."
    exit
fi

echo "Installing dependencies if missing..."
npm install

echo ""
echo "Running Postman Collection..."
npx newman run ../Cinema_Booking_API.postman_collection.json \
  --env-var "baseUrl=http://localhost:8000" \
  -r cli,htmlextra \
  --reporter-htmlextra-export ./reports/report.html

echo ""
echo "===================================================="
echo "Test execution complete!"
echo "Your detailed HTML report is saved in the 'reports' folder."
echo "===================================================="
