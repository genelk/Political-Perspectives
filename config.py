import os

# Project paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Source configurations
DEFAULT_SOURCES = [
    {"name": "CNN", "perspective": "left"},
    {"name": "Fox News", "perspective": "right"},
    {"name": "Reuters", "perspective": "center"},
    {"name": "MSNBC", "perspective": "left"},
    {"name": "Wall Street Journal", "perspective": "right-center"},
    {"name": "BBC", "perspective": "center-left"},
    {"name": "Breitbart", "perspective": "far-right"},
    {"name": "The Guardian", "perspective": "left"},
    {"name": "Daily Wire", "perspective": "right"},
    {"name": "Associated Press", "perspective": "center"}
]

# Agent configurations
RESEARCH_CONFIG = {
    "max_sources": 5,
    "min_sources": 3,
    "require_diverse_perspectives": True
}

BIAS_ANALYSIS_CONFIG = {
    "perspective_categories": ["left", "center", "right"]
}

CONTENT_CONFIG = {
    "include_conclusion": True,
    "include_source_citations": True
}
