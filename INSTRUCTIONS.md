# Instructions for Using Aridia ML

## Prerequisites

1. **Python**: Ensure that Python 3.12 or a later version is installed on your system.
2. **UV**: Make sure the UV package manager is installed and Python is accessible from your shell.

## Installation

1. **Install Dependencies**:
    - Navigate to the project directory.
    - Run the following command to install dependencies and set up the Python virtual environment:

      ```bash
      uv sync
      ```

## Running the Model

Aridia ML includes a built-in CLI (powered by Typer) to automate tasks such as running the sample playground, training the model, collecting data, and creating datasets.

1. **Run the Sample Playground**:
    - Execute the following command:

      ```bash
      python aridia_ml/main.py run
      ```
2. **Run the Data Collection Playground**:
    - Execute the following command:

      ```bash
      python aridia_ml/main.py collect-data
      ```
3. **Run the Dataset Creation Playground**:
    - Execute the following command:

      ```bash
      python aridia_ml/main.py create-dataset
      ```

4. **Run the Model Training Playground**:
    - Execute the following command:

      ```bash
      python aridia_ml/main.py train
      ```

You can view all the available commands by running:
```bash
python aridia_ml/main.py --help
```

## Camera Permissions

- **Permission Prompt**: Aridia ML may prompt you to grant camera permissions. OpenCV requires access to your camera to capture video and perform translations.
- **Grant Permissions**: Ensure that you allow the camera permission prompt.
  - **Note**: No data is saved or used for training beyond the dataset designated for development purposes.
