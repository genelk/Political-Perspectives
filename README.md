# Political Perspectives

A multi-agent system that generates balanced political analysis by combining perspectives from across the political spectrum.

## Overview

Political Perspectives is an experimental system inspired by Ground News that demonstrates how multiple specialized AI models can work together to analyze political topics from different viewpoints. The system uses a code-based communication protocol between agents while providing human-readable reasoning snippets to show its thought process.

## Key Features

- **Multi-perspective analysis:** Combines viewpoints from left, center, and right political sources
- **Bias transparency:** Shows the distribution of political perspectives in the analysis
- **Agent specialization:** Uses dedicated agents for research, bias analysis, and content creation
- **Code-based communication:** Agents communicate through Python code for efficiency
- **Reasoning visibility:** Provides concise reasoning explanations for human users

## System Architecture

The system consists of three specialized agents coordinated by an orchestrator:

1. **Research Agent:** Gathers information on political topics from diverse sources
2. **Bias Analysis Agent:** Evaluates the political leaning of different sources and extracts key points
3. **Content Agent:** Creates a balanced report incorporating multiple perspectives
4. **Orchestrator:** Coordinates the workflow between specialized agents

![Architecture Diagram](https://github.com/user-attachments/assets/49a41611-5068-4b34-905c-1c5446c64204)

## Communication Protocol

Agents communicate using a standardized message format that includes:

- **Code:** Python code snippets for direct execution
- **Reasoning:** Brief natural language explanation for human users
- **Data:** Structured information payload

Example:
```python
{
    "agent_id": "research",
    "code": "gather_information(topic='immigration reform')",
    "reasoning": "Researching political topic: immigration reform",
    "data": {"topic": "immigration reform"}
}
```

## Getting Started

### Prerequisites

- Python 3.8+
- Required packages (see requirements.txt)

### Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/political-perspectives.git
cd political-perspectives
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the application:
```
python main.py
```

## Usage

1. Enter a political topic when prompted (e.g., "immigration reform", "climate change policy")
2. The system will process the request through its agent pipeline
3. Review the system's reasoning process and final balanced report

## Example Output

```
Political Perspectives Analysis System
-------------------------------------
Enter a political topic to analyze: climate change policy

Processing request...

System Reasoning Process:
1. Research Agent: Found information on climate change policy from 5 diverse sources
2. Bias Analysis Agent: Identified political perspectives across the spectrum
3. Content Agent: Generated balanced report incorporating multiple perspectives

==================================================

Balanced Analysis: climate change policy
==================================================

A multi-perspective examination of climate change policy incorporating viewpoints from across the political spectrum.

## Left-Leaning Perspective
Analysis of climate change policy focusing on social impacts and environmental justice

## Centrist Perspective
Factual reporting on climate change policy developments and international agreements

## Right-Leaning Perspective
Conservative-leaning analysis of climate change policy examining economic effects and market-based solutions

Conclusion: This analysis shows that climate change policy is viewed differently across the political spectrum, with varying emphasis on different aspects of the issue.
```

## Future Enhancements

- Integration with real news APIs and sources
- Implementation of NLP models for more sophisticated bias detection
- Interactive visualization of perspective distribution
- User customization of source preferences
- Expanded analysis to include international perspectives

## Research Background

This project explores concepts from compositional AI research, particularly how specialized models can communicate and collaborate. While traditional approaches often use natural language for inter-model communication, this implementation uses code as the communication medium for greater efficiency, while preserving natural language reasoning for human users.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by Ground News' approach to multi-perspective news analysis
- Based on research in compositional AI and multi-agent systems
