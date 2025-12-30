from crewai import Task
from agents import property_researcher, property_analyst

research_task = Task(
    description="""Conduct a comprehensive analysis of potential retail property investments in {location}.

    Specific research requirements:
    1. Market Analysis:
       - Identify top 3-5 potential retail property investment locations
       - Analyze current market trends and economic indicators
       - Assess demographic data and consumer spending patterns
       - Evaluate local retail ecosystem and potential tenant mix

    2. Property Evaluation Criteria:
       - Foot traffic analysis
       - Accessibility and transportation infrastructure
       - Proximity to complementary businesses
       - Local economic development plans

    3. Financial Analysis:
       - Estimate potential rental yields
       - Calculate projected ROI
       - Assess property valuation and appreciation potential
       - Identify potential renovation or repositioning opportunities

    4. Risk Assessment:
       - Analyze competitor landscape
       - Evaluate e-commerce impact on local retail
       - Assess potential regulatory or zoning challenges
       - Identify potential long-term growth barriers

    Deliverable: A comprehensive, data-driven investment recommendation report.""",
    agent=property_researcher,
    expected_output="""Detailed JSON report containing:
    - market_summary: Brief overview of the market
    - recommended_properties: List of 3-5 properties with details
    - financial_projections: ROI and rental yield estimates
    - risk_assessment: Key risks and mitigation strategies
    - recommendations: Next steps for due diligence""",
    output_file="research_report.json"
)


analysis_task = Task(
    description="""Review the property research data and create a concise investor-focused summary report.
    
    Your analysis should:
    - Summarize key findings in bullet points
    - Highlight top investment opportunities
    - Identify critical risk factors
    - Provide clear, actionable recommendations
    - Format for easy executive review""",
    expected_output="""A well-structured summary report with:
    - Executive Summary (2-3 sentences)
    - Top Property Recommendations (bullet points)
    - Key Market Insights (bullet points)
    - Risk Considerations (bullet points)
    - Final Investment Recommendation""",
    agent=property_analyst,
    output_file="investment_summary.txt",
    context=[research_task]  # This passes research_task output to analysis_task
)