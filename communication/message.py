class AgentMessage:
    """Message format for inter-agent communication."""
    
    def __init__(self, agent_id, code=None, reasoning=None, data=None):
        self.agent_id = agent_id
        self.code = code  # Python code to be executed
        self.reasoning = reasoning  # Brief explanation for the user
        self.data = data or {}  # Structured data payload
    
    def to_dict(self):
        return {
            "agent_id": self.agent_id,
            "code": self.code,
            "reasoning": self.reasoning,
            "data": self.data
        }
    
    @classmethod
    def from_dict(cls, message_dict):
        return cls(
            agent_id=message_dict["agent_id"],
            code=message_dict.get("code"),
            reasoning=message_dict.get("reasoning"),
            data=message_dict.get("data", {})
        )
