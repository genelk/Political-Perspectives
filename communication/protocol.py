from communication.message import AgentMessage

class CommunicationProtocol:
    """Handles message passing between agents."""
    
    @staticmethod
    def format_message(agent_id, code=None, reasoning=None, data=None):
        """Format a message for inter-agent communication."""
        return AgentMessage(agent_id, code, reasoning, data)
    
    @staticmethod
    def execute_code(code_snippet, context=None):
        """
        Simulates execution of code snippets.
        
        In a full implementation, this would use a secure sandbox
        to execute the code with proper isolation.
        """
        # For prototype, we just log the code that would be executed
        print(f"[DEBUG] Would execute code: {code_snippet}")
        return True
