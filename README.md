# Semantic Similarity Analysis
Analyzing semantic similarities between words or phrases.

This project demonstrates semantic similarity analysis using spaCy.

## Prerequisites

Before you get started with this project, make sure you have the following prerequisites installed on your system:

- **Python 3.x**: You'll need Python 3.x to run the analysis script.
- **Docker (Optional)**: If you prefer running the script in a containerized environment, you can install Docker.

## Installation

Follow these steps to set up the project:

### 1. Clone this repository
Open your terminal or command prompt and run the following command to clone this repository:

```bash
git clone https://github.com/vdp11/semantic-similarity-analysis.git


Usage
Running the Semantic Similarity Analysis
To analyze semantic similarity between words or phrases, run the semantic.py script:

bash
Copy code
python semantic_similarity/semantic.py
Running the Docker Container
Alternatively, you can run the script in a Docker container:

Build the Docker image (from the root of the repository):

bash
Copy code
docker build -t semantic-analysis .
Run the Docker container:

bash
Copy code
docker run -it semantic-analysis
Results
The script will calculate and display semantic similarity scores between words or phrases.
When run in a Docker container, the results will be shown in the container's terminal.
Notes
The semantic similarity scores depend on the spaCy language model used. This repository uses 'en_core_web_md' for better accuracy.

