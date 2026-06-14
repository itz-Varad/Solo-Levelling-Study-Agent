# ⚔️ Solo Levelling Study Agent

An AI-powered study assistant inspired by Solo Leveling.

## Features

### Hunter System
Ask study-related questions using a local AI model powered by Ollama.

### Shadow Archive
Convert long notes into:
- Summaries
- Key Concepts
- Important Formulas
- Revision Tips

### Quiz Dungeon
Generate topic-based quizzes instantly.

### Hunter Training
Create AI-generated study plans and learning roadmaps.

### Progression System
- XP Tracking
- Hunter Rank System
- Solo Levelling Inspired Interface

## Tech Stack

- Python
- Streamlit
- Ollama
- Phi-3 Mini

## Installation

```bash
git clone <repo-url>
cd Solo-Levelling-Study-Agent

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

ollama pull phi3:mini

streamlit run app.py