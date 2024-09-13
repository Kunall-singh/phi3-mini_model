# Description: This script reads prompts from a file, sends them to the Ollama model, 
# and writes the responses to an output file.

import subprocess                                   ## we use the subprocess module to run the ollama command


# Function to read prompts from a file
def read_prompts(file_path):
    with open(file_path, 'r') as file:              ## open the file in read mode
        prompts = file.readlines()                  ## read the lines of the file
    return [prompt.strip() for prompt in prompts]   ## return the list of prompts(strings)


# Function to send the prompt to the Ollama model using the correct command
def get_model_response(prompt):
    process = subprocess.run(                       ## run the subprocess    
        ['ollama', 'run', 'phi3', prompt],          ## run the ollama command with the model and prompt
        capture_output=True, text=True, check=True  ## capture the output, text output, and check for errors
    )
    return process.stdout.strip()                   ## return the output of the process after stripping the whitespaces


# Function to write responses to a file
def write_responses(responses, file_path):
    
    with open(file_path, 'w') as file:              ## open the file in write mode
        for response in responses:                  ## iterate over the responses
            file.write(response + '\n')             ## write the response to the file and add a newline character

if __name__ == "__main__":
    # Step 1: Read prompts from the input file
    prompts = read_prompts('prompts.txt')

    # Step 2: Send prompts to the model and collect responses
    responses = [get_model_response(prompt) for prompt in prompts]

    # Step 3: Write the responses to an output file
    write_responses(responses, 'output_responses.txt')

    print("Model responses have been saved to output_responses.txt.")
