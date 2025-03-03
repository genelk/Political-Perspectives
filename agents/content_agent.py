from agents import BaseAgent

class ContentAgent(BaseAgent):
    """Creates the final balanced political report."""
    
    def __init__(self):
        super().__init__("content")
        
    def process(self, message):
        """Generate balanced political content."""
        # Extract analysis data
        analysis_data = message.data
        topic = analysis_data.get("topic")
        bias_distribution = analysis_data.get("bias_distribution")
        key_points = analysis_data.get("key_points")
        
        # Generate report
        report = self._generate_report(topic, bias_distribution, key_points)
        
        return self.create_message(
            code="return final_report(analysis_data)",
            reasoning="Generated balanced report incorporating multiple perspectives",
            data={
                "topic": topic,
                "report": report,
                "bias_distribution": bias_distribution
            }
        )
    
    def _generate_report(self, topic, bias_distribution, key_points):
        """Generate balanced political report."""
        # In a real implementation, this would use a language model to generate content
        
        # For prototype, construct a simple report format
        report = {
            "title": f"Balanced Analysis: {topic}",
            "summary": f"A multi-perspective examination of {topic} incorporating viewpoints from across the political spectrum.",
            "sections": [
                {
                    "heading": "Left-Leaning Perspective",
                    "content": "\n".join(key_points.get("left", ["No left-leaning perspectives found."]))
                },
                {
                    "heading": "Centrist Perspective",
                    "content": "\n".join(key_points.get("center", ["No centrist perspectives found."]))
                },
                {
                    "heading": "Right-Leaning Perspective",
                    "content": "\n".join(key_points.get("right", ["No right-leaning perspectives found."]))
                }
            ],
            "conclusion": f"This analysis shows that {topic} is viewed differently across the political spectrum, with varying emphasis on different aspects of the issue."
        }
        
        return report
