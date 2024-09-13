# Phi-3 Mini Prompt Response Script

## Overview

This project demonstrates how to interact with the Phi-3 Mini model (a lightweight, state-of-the-art open model) using Ollama, a desktop application that lets you download and run models locally. The script reads prompts from a text file, sends them to the Phi-3 Mini model running on Ollama, and stores the model's responses in an output text file.


## Prerequisites

- Python 3
- Ollama installed and running locally.
- Phi-3 Mini model (`phi3`) pulled via Ollama.

## Installation

### Step 1: Set Up Python Environment

1. Clone this repository and navigate to the project directory:
    ```bash
    git clone https://github.com/Kunall-singh/phi3-mini_model.git
    cd phi3-mini_model
    ```

2. Create and activate a virtual environment:

    - **For Linux/macOS:**
      ```bash
      python3 -m venv phi3-env
      source phi3-env/bin/activate
      ```

    - **For Windows:**
      ```bash
      python -m venv phi3-env
      .\phi3-env\Scripts\activate
      ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.yaml
    ```

### Step 2: Install and Set Up Ollama

1. Download and install Ollama from the [official website](https://ollama.com).

2. Start the Ollama server on an separate terminal:
    ```bash
    ollama serve
    ```

3. Pull the Phi-3 Mini model to ensure it's available locally:
    ```bash
    ollama pull phi3
    ```

4. You can check list of all installed models on your system using the following command:
    ```bash
    ollama list
    ```
5. TO get help related ollama use:
    ```bash
    ollama --help
    ```
    
### Step 3 : Run the script

1. Make sure you have ollama running in separate teminal by using the command :
    ```bash
    ollama serve
    ```

2. Open a new terminal and use the command:
    ```bash
    python3 script.py
    ```
3. It will take a few seconds and a new output_response.txt file will be created with responses in it.

## How It Works

- The script first reads the prompts from `input_prompts.txt`.
- It then uses the `ollama run` command to send each prompt to the Phi-3 Mini model, which is served by Ollama.
- The model generates a response for each prompt, and the script writes these responses to `output_responses.txt`.

## Dependencies

All required Python dependencies are listed in `requirements.txt`.

