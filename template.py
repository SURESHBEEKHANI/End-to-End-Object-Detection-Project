################################################################################
# IMPORTS AND CONFIGURATION
################################################################################
# Import required libraries
import os
from pathlib import Path
import logging

# Configure basic logging with timestamp
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

################################################################################
# PROJECT STRUCTURE DEFINITION
################################################################################
# Project name that will be used throughout the application
project_name = "bike-helmet-detection"

# Define the complete project structure
# This list contains all files and directories that will be created
# Structure is organized in the following categories:
# 1. Data Storage
# 2. Core Components
# 3. Configuration
# 4. Constants
# 5. Entity Definitions
# 6. Error Handling
# 7. Logging
# 8. Pipeline Management
# 9. Utilities
# 10. Web Application
# 11. Deployment Configuration
list_of_files = [
    # Data directory
    "data/.gitkeep",
    
    # Main package initialization
    f"{project_name}/__init__.py",
    
    # Components module - contains core functionality
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",    # For data collection
    f"{project_name}/components/data_validation.py",   # For data validation
    f"{project_name}/components/model_trainer.py",     # For model training
    f"{project_name}/components/model_pusher.py",      # For model deployment
    
    # Configuration module - contains setup and config files
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",  # AWS S3 operations
    
    # Constants module - contains project constants
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    
    # Entity module - contains data structures and models
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    
    # Exception handling module
    f"{project_name}/exception/__init__.py",
    
    # Logging module
    f"{project_name}/logger/__init__.py",
    
    # Pipeline module - contains training workflows
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    
    # Utility functions module
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    
    # Web application files
    "template/index.html",
    
    # Docker related files
    ".dockerignore",
    "app.py",
    "Dockerfile",
    
    # Project dependencies and setup files
    "requirements.txt",
    "setup.py"
]

################################################################################
# FILE AND DIRECTORY CREATION LOGIC
################################################################################
# Iterate through the defined structure and create all necessary files/directories
for filepath in list_of_files:
    # Convert string path to Path object for better handling
    filepath = Path(filepath)

    # Split the filepath into directory and filename
    filedir, filename = os.path.split(filepath)

    # Directory Creation Phase
    if filedir !="":
        # Create directories if they don't exist
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # File Creation Phase
    # Only create file if it doesn't exist or is empty
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")
    
    # Skip if file already exists
    else:
        logging.info(f"{filename} is already created")