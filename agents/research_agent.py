from agents import BaseAgent

class ResearchAgent(BaseAgent):
    """Gathers information on political topics from various sources."""
    
    def __init__(self):
        super().__init__("research")
        
    def process(self, message):
        """Research political topic and gather information."""
        # Extract topic from incoming message
        topic = message.data.get("topic", "")
        
        # This would use a model to gather information
        # For prototype, we'll simulate the process
        sources = self._simulate_research(topic)
        
        # Return findings with code, reasoning and data
        return self.create_message(
            code=f"return research_results('{topic}')",
            reasoning=f"Found information on {topic} from 5 diverse sources",
            data={
                "topic": topic,
                "sources": sources
            }
        )
    
    def _simulate_research(self, topic):
        """Simulate research process for prototype."""
        # In a real implementation, this would use a model to search and extract information
        return [
            {"source": "CNN", "perspective": "left", "summary": f"Analysis of {topic} focusing on social impacts"},
            {"source": "Fox News", "perspective": "right", "summary": f"Coverage of {topic} examining economic effects"},
            {"source": "Reuters", "perspective": "center", "summary": f"Factual reporting on {topic} developments"},
            {"source": "MSNBC", "perspective": "left", "summary": f"Progressive view on {topic}"},
            {"source": "Wall Street Journal", "perspective": "right-center", "summary": f"Conservative-leaning analysis of {topic}"}
        ]
