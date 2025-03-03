from abc import ABC, abstractmethod
from communication.message import AgentMessage

class BaseAgent(ABC):
    """Base class for all agents in the system."""
    
    def __init__(self, agent_id):
        self.agent_id = agent_id
    
    @abstractmethod
    def process(self, message):
        """Process incoming message and return response."""
        pass
    
    def create_message(self, code=None, reasoning=None, data=None):
        """Create a standardized message."""
        return AgentMessage(
            agent_id=self.agent_id,
            code=code,
            reasoning=reasoning,
            data=data
        )
