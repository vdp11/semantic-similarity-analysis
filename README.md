# Semantic Similarity Analysis

This project demonstrates semantic similarity analysis using spaCy.

## Prerequisites

- Python 3.x
- Docker (if you prefer running the script in a container)

## Installation

Clone this repository: git clone https://github.com/vdp11/semantic-similarity-analysis.git
   cd semantic-similarity-analysis

## Usage
Running the Semantic Similarity Analysis
To analyze semantic similarity between words or phrases, run the semantic.py script:

'''bash

python semantic_similarity/semantic.py

Running the Docker Container
Alternatively, you can run the script in a Docker container:

Build the Docker image (from the root of the repository):

'''bash

docker build -t semantic-analysis .

Run the Docker container:

'''bash

docker run -it semantic-analysis

## Results
The script will calculate and display semantic similarity scores between words or phrases.
When run in a Docker container, the results will be shown in the container's terminal.

## Notes
The semantic similarity scores depend on the spaCy language model used. This repository uses 'en_core_web_md' for better accuracy.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
