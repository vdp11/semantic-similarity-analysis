# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Download and install the SpaCy model 'en_core_web_md'
RUN python -m spacy download en_core_web_md

# Copy the current directory contents into the container at /app
COPY . /app

# Run your script when the container launches
CMD ["python", "semantic.py"]

