import os
import json
import google.generativeai as genai

# Setup your API key as an environment variable before running
# export GEMINI_API_KEY="your-api-key"

def analyze_test_cases():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not found. Skipping actual API call.")
        return

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # In a real workflow, this would read from artifacts/test-cases.xlsx using pandas/openpyxl
    # For this script, we'll simulate the input
    existing_cases = [
        {"id": "TC001", "desc": "Register with valid email and password"},
        {"id": "TC002", "desc": "Register with duplicate email"}
    ]
    
    prompt = f"""
    You are an expert QA Engineer. Review the following existing test cases for an Authentication API:
    {json.dumps(existing_cases, indent=2)}
    
    Suggest 3 missing boundary or negative test cases. Format the output as a Markdown table with columns: Proposed ID, Description, Reason.
    """
    
    print("Sending request to Gemini API...")
    try:
        response = model.generate_content(prompt)
        print("AI Suggestion received:\n")
        print(response.text)
        
        # Save raw output to a temporary file for QA review
        with open(os.path.join(os.path.dirname(__file__), 'raw-ai-output.md'), 'w') as f:
            f.write(response.text)
            
    except Exception as e:
        print(f"Error calling Gemini API: {e}")

if __name__ == "__main__":
    analyze_test_cases()
