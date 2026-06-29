import os
import openpyxl

def generate_rtm():
    """Generates a Traceability Matrix mapping Requirements to Test Cases."""
    os.makedirs('reports/generated', exist_ok=True)
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Traceability Matrix"
    
    headers = ["Req ID", "User Story", "Test Scenario", "Test Cases", "Coverage Status"]
    ws.append(headers)
    
    # In a real workflow, this would parse markdown/excel files dynamically
    # Simulating data for portfolio purposes
    rtm_data = [
        ["FR-01.1", "US-01", "TS-AUTH-01", "TC001, TC015", "Covered"],
        ["FR-01.2", "US-02", "TS-AUTH-03", "TC003, TC016", "Covered"],
        ["FR-02.1", "US-03", "TS-MOV-01", "TC005", "Covered"],
    ]
    
    for row in rtm_data:
        ws.append(row)
        
    output_path = 'reports/generated/traceability-matrix.xlsx'
    wb.save(output_path)
    print(f"RTM successfully generated at {output_path}")

if __name__ == "__main__":
    generate_rtm()
