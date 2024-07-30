# Instructions for Using Aridia ML

## Prerequisites

1. **Python Version**: Ensure you have at least Python 3.12 installed on your system.
2. **Pip**: Make sure pip is installed and Python is globally accessible.

## Installation

1. **Install Dependencies**:
    - Navigate to the directory where `requirements.txt` is located.
    - Run the following command to install all necessary dependencies:

      ```bash
      pip install -r requirements.txt
      ```

## Running the Model

1. **Execute the Test Script**:
    - Run the `test_model.py` file by executing the following command:

      ```bash
      python -u test_model.py
      ```

## Camera Permissions

- **Permission Prompt**: Aridia ML may prompt for camera permissions. OpenCV requires access to your camera to start capturing video and performing translations.
- **Accept Permissions**: Ensure you accept the camera permission prompt.
  - **Note**: No data is saved or used for training beyond the development-specific dataset designated for development purposes.
