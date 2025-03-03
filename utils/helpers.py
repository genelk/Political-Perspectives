import json
import os

def load_json_file(filepath):
    """Load data from a JSON file."""
    if not os.path.exists(filepath):
        return {}
    
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json_file(data, filepath):
    """Save data to a JSON file."""
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)

def format_report_for_display(report):
    """Format a report dictionary for display."""
    output = []
    
    # Add title
    output.append(f"# {report.get('title', 'Report')}\n")
    
    # Add summary
    output.append(f"{report.get('summary', '')}\n")
    
    # Add sections
    for section in report.get('sections', []):
        output.append(f"## {section.get('heading', '')}")
        output.append(f"{section.get('content', '')}\n")
    
    # Add conclusion
    output.append(f"**Conclusion:** {report.get('conclusion', '')}")
    
    return "\n".join(output)
