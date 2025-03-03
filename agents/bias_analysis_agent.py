from agents import BaseAgent

class BiasAnalysisAgent(BaseAgent):
    """Analyzes potential bias in political reporting."""
    
    def __init__(self):
        super().__init__("bias_analysis")
        
    def process(self, message):
        """Analyze bias in gathered information."""
        # Extract research data
        research_data = message.data
        sources = research_data.get("sources", [])
        
        # Analyze bias distribution
        bias_distribution = self._calculate_bias_distribution(sources)
        
        # Identify key points from across the spectrum
        key_points = self._extract_key_points(sources)
        
        return self.create_message(
            code="return bias_analysis_results(research_data)",
            reasoning="Identified political perspectives across the spectrum",
            data={
                "topic": research_data.get("topic"),
                "bias_distribution": bias_distribution,
                "key_points": key_points,
                "sources": sources
            }
        )
    
    def _calculate_bias_distribution(self, sources):
        """Calculate the distribution of political perspectives."""
        perspectives = {}
        for source in sources:
            perspective = source.get("perspective")
            perspectives[perspective] = perspectives.get(perspective, 0) + 1
            
        return perspectives
    
    def _extract_key_points(self, sources):
        """Extract key points from sources across the political spectrum."""
        # In a real implementation, this would use NLP to identify and compare key points
        perspectives = {"left": [], "center": [], "right": []}
        
        for source in sources:
            perspective = source.get("perspective")
            if "left" in perspective:
                perspectives["left"].append(source.get("summary"))
            elif "right" in perspective:
                perspectives["right"].append(source.get("summary"))
            else:
                perspectives["center"].append(source.get("summary"))
                
        return perspectives
