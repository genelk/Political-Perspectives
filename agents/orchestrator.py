from agents import BaseAgent

class OrchestratorAgent(BaseAgent):
    """Coordinates the workflow between specialized agents."""
    
    def __init__(self, agents=None):
        super().__init__("orchestrator")
        self.agents = agents or {}
    
    def add_agent(self, agent_id, agent):
        """Register an agent with the orchestrator."""
        self.agents[agent_id] = agent
    
    def process(self, user_request):
        """Process user request and coordinate agent workflow."""
        # Initial analysis of the request
        topic = self._extract_topic(user_request)
        
        # Create initial workflow
        workflow_code = f"""
        # Orchestrator workflow plan
        research_results = research_agent.process('{topic}')
        bias_analysis = bias_analysis_agent.process(research_results)
        final_report = content_agent.process(bias_analysis)
        return final_report
        """
        
        # Start with research agent
        research_msg = self.create_message(
            code=f"gather_information(topic='{topic}')",
            reasoning=f"Researching political topic: {topic}",
            data={"topic": topic}
        )
        
        # Execute the workflow by passing messages between agents
        research_results = self.agents["research"].process(research_msg)
        
        bias_msg = self.create_message(
            code="analyze_bias(research_data)",
            reasoning="Analyzing political bias in gathered information",
            data=research_results.data
        )
        bias_results = self.agents["bias_analysis"].process(bias_msg)
        
        content_msg = self.create_message(
            code="create_report(analysis_data)",
            reasoning="Generating balanced political report",
            data=bias_results.data
        )
        final_report = self.agents["content"].process(content_msg)
        
        return final_report
    
    def _extract_topic(self, user_request):
        """Extract the main political topic from user request."""
        # Simple implementation for prototype
        return user_request.replace("Analyze ", "").strip()
