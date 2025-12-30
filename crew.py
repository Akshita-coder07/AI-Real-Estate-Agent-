from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from agents import property_researcher, property_analyst
from tasks import research_task, analysis_task
from datetime import datetime

crew = Crew(
    agents=[property_researcher, property_analyst], 
    tasks=[research_task, analysis_task], 
    verbose=True
)

try:
    # Get location from user
    print("="*50)
    print("RETAIL PROPERTY INVESTMENT ANALYZER")
    print("="*50)
    location = input("\nEnter location for property analysis: ").strip()
    
    if not location:
        location = "Delhi NCR"
        print(f"No location entered. Using default: {location}")
    
    print(f"\nAnalyzing properties in: {location}")
    print("="*50)
    print("\nStarting analysis... Please wait...")
    
    task_output = crew.kickoff(
        inputs={
            "location": location
        }
    )
    
    # Create formatted output
    formatted_output = f"""
{'='*80}
RETAIL PROPERTY INVESTMENT ANALYSIS REPORT
{'='*80}
Location: {location}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*80}

{task_output}

{'='*80}
End of Report
{'='*80}
"""
    
    # Save to file
    with open('research_task_output.txt', 'w', encoding='utf-8') as f:
        f.write(formatted_output)
    
    print("\n" + "="*50)
    print("ANALYSIS COMPLETE!")
    print("="*50)
    print(f"\nLocation Analyzed: {location}")
    print("\nResults saved to:")
    print("- research_task_output.txt")
    print("- research_report.json")
    print("- investment_summary.txt")
    print("\n" + "="*50)
    
except KeyboardInterrupt:
    print("\n\nAnalysis cancelled by user.")
except Exception as e:
    print(f"\nError during execution: {e}")
    print("\nPlease check:")
    print("1. Your .env file has valid GROQ_API_KEY and SERPER_API_KEY")
    print("2. All required packages are installed")
    print("3. You have internet connection")