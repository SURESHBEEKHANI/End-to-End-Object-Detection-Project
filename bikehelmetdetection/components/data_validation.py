import os  # Importing the os module to interact with the operating system
import sys  # Importing sys to handle system-specific parameters and functions
import shutil  # Importing shutil to handle file operations like copying
from bikehelmetdetection.logger import logging  # Importing logging for recording events and debugging information
from bikehelmetdetection.exception import bhdException  # Importing custom exception handling
from bikehelmetdetection.entity.config_entity import DataValidationConfig  # Importing configuration settings for data validation
from bikehelmetdetection.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact  # Importing data entities

class DataValidation:
    def __init__(self, 
                 data_ingestion_artifact: DataIngestionArtifact, 
                 data_validation_config: DataValidationConfig):
        """Initializes the DataValidation class."""
        try:
            # Storing the input parameters as class attributes
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise bhdException(e, sys)  # Handling exceptions using a custom exception class

    def validate_all_files_exist(self) -> bool:
        """Checks if all required files exist in the feature store directory."""
        try:
            validation_status = True  # Assume all files are present unless proven otherwise
            
            # Get a list of all files in the directory where features are stored
            feature_store_files = set(os.listdir(self.data_ingestion_artifact.feature_store_path))
            
            # Get a list of required files as specified in the configuration
            required_files = set(self.data_validation_config.required_file_list)
            
            # Find any missing files by subtracting sets
            missing_files = required_files - feature_store_files
            
            # If there are missing files, set validation_status to False and log a warning
            if missing_files:
                validation_status = False
                logging.warning(f"Missing files: {missing_files}")
            
            # Ensure the validation directory exists before writing the validation status
            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            
            # Write the validation result to a file
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            
            return validation_status  # Return whether the files are all present or not
        
        except Exception as e:
            raise bhdException(e, sys)  # Handle any errors that occur during validation
    
    def initiate_data_validation(self) -> DataValidationArtifact:
        """Initiates data validation and returns a DataValidationArtifact."""
        logging.info("Starting data validation process.")  # Log the start of validation
        try:
            # Call the function to check if required files exist
            status = self.validate_all_files_exist()
            
            # Create a validation artifact containing the validation status
            data_validation_artifact = DataValidationArtifact(validation_status=status)
            
            # Log the completion status of validation
            logging.info(f"Data validation completed with status: {status}")
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            
            # If validation was successful, copy the zip file to the current directory
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
                logging.info("Copied data zip file to the current working directory.")
            
            return data_validation_artifact  # Return the validation artifact
        
        except Exception as e:
            raise bhdException(e, sys)  # Handle any exceptions that occur