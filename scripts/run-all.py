import os
import sys
import subprocess
import requests

def check_health():
    print("[*] Running: API Health Check (GET /health)...")
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("[+] PASS: API is healthy.\n")
            return True
    except Exception:
        pass
    print("[-] FAIL: API is not running.")
    print("Please start FastAPI first:\n    python -m uvicorn app.main:app\n")
    return False

def run_command(name, command):
    print(f"[*] Running: {name}...")
    try:
        result = subprocess.run(command, shell=True, check=True)
        print(f"[+] PASS: {name}\n")
    except subprocess.CalledProcessError:
        print(f"[-] FAIL: {name}\n")
        sys.exit(1)

def main():
    print("=========================================")
    print("      QA Automation Runner               ")
    print("=========================================\n")
    
    if not check_health():
        sys.exit(1)
        
    os.makedirs('reports/newman', exist_ok=True)
    os.makedirs('reports/pytest', exist_ok=True)
    
    run_command("Newman API Automation", "npx newman run Cinema_Booking_API.postman_collection.json -r cli,json --reporter-json-export reports/newman/report.json")
    run_command("Pytest Test Suite", "python -m pytest tests/ --junitxml=reports/pytest/junit.xml -v")
    run_command("Database Verification", "python scripts/verify-db.py")
    run_command("Generate Metrics & Dashboard", "python scripts/generate_metrics.py")
    run_command("Generate Traceability Matrix", "python scripts/generate_rtm.py")

    print("=========================================")
    print("      E2E QA WORKFLOW COMPLETED          ")
    print("=========================================")

if __name__ == "__main__":
    main()
