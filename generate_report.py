import os
from openai import OpenAI
import time

def generate_markdown_report():
    print("Initiating report generation via OmniRoute...")
    
    # Initialize OpenAI client pointed to OmniRoute
    client = OpenAI(
        base_url="http://localhost:20128/v1",
        api_key="omniroute-local-key"
    )

    try:
        response = client.chat.completions.create(
            model="auto",
            messages=[
                {"role": "system", "content": "You are a professional technical analyst."},
                {
                    "role": "user", 
                    "content": "Generate a short 3-point Markdown report on AI Performance and Token Efficiency. Title it 'AI Performance Analysis Report 📊'. Include an Executive Summary, Key Insights (Token Efficiency, Provider Stability, Cost Analytics), and a footer."
                }
            ],
            max_tokens=300
        )
        report_content = response.choices[0].message.content
        print("Successfully generated report from OmniRoute API!")
        
        # Write the output file
        output_path = "outputs.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_content)
            
        print(f"Report successfully saved to {output_path}")
        
    except Exception as e:
        print(f"\n[ERROR] Failed to connect to OmniRoute at localhost:20128 or process request.")
        print(f"[ERROR] Details: {e}\n")
        raise e

if __name__ == "__main__":
    generate_markdown_report()
