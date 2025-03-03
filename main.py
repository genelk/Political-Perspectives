from agents.orchestrator import OrchestratorAgent
from agents.research_agent import ResearchAgent
from agents.bias_analysis_agent import BiasAnalysisAgent
from agents.content_agent import ContentAgent

def main():
    # Create agents
    orchestrator = OrchestratorAgent()
    research_agent = ResearchAgent()
    bias_analysis_agent = BiasAnalysisAgent()
    content_agent = ContentAgent()
    
    # Register specialized agents with orchestrator
    orchestrator.add_agent("research", research_agent)
    orchestrator.add_agent("bias_analysis", bias_analysis_agent)
    orchestrator.add_agent("content", content_agent)
    
    print("Political Perspectives Analysis System")
    print("-------------------------------------")
    print("Enter a political topic to analyze (e.g., 'climate change policy', 'immigration reform'):")
    user_input = input("> ")
    
    print("\nProcessing request...\n")
    
    # Process the request through the orchestrator
    result = orchestrator.process(user_input)
    
    # Display the agent reasoning throughout the process
    print("System Reasoning Process:")
    print(f"1. Research Agent: {result.data.get('research_reasoning', 'Researching topic')}")
    print(f"2. Bias Analysis Agent: {result.data.get('bias_reasoning', 'Analyzing perspectives')}")
    print(f"3. Content Agent: {result.reasoning}")
    
    # Display the final report
    report = result.data.get("report", {})
    print("\n" + "=" * 50)
    print(f"\n{report.get('title', 'Report')}")
    print("=" * 50)
    print(f"\n{report.get('summary', '')}\n")
    
    for section in report.get("sections", []):
        print(f"\n## {section.get('heading', '')}")
        print(f"{section.get('content', '')}\n")
    
    print(f"\nConclusion: {report.get('conclusion', '')}")

if __name__ == "__main__":
    main()
