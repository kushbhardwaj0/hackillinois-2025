#!/usr/bin/env python3
import pytest
import argparse
import google.generativeai as genai
import subprocess

def main():
    return
    
def file_extractor():
    parser = argparse.ArgumentParser(prog="driver", description="Process a file for testing")
    parser.add_argument("filename", help="Name of the file to process")
    args = parser.parse_args()
    text = ""
    with open(args.filename, 'r') as file:
        text = file.read()
    return text, args.filename


def create_test_file(content, module_name, filename="test_run.py"):
    module_name = module_name.replace('/', '.')[:-3]
    content = f"from {module_name} import *\n" + content
    #driver/factorial
    #factorial.py
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"File '{filename}' created successfully.")

        print(f"Running '{filename}'...")
        result = subprocess.run(["python3", filename], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Error running '{filename}': {result.stderr}")
        else:
            print(f"'{filename}' executed successfully.")

    except Exception as e:
        print(f"Error: {e}")


def testcase_generator(text):

    genai.configure(api_key=API_KEY)
    
    generation_config = genai.types.GenerationConfig(
        temperature=0.1,
    )
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction=["you are a minimal coder", "you are a pytest developer"],
    )
    
    response = model.generate_content(
        "create only pytest testcases, including edge cases for the following code - just give code for testcases and no further text/explanation/code comments. also include the main method that runs all the test cases. the only import you should put is 'pytest' - i will put the other imports in myself. DONT PUT COMMENTS IN THE CODE: " + text
    )
    
    outputText = response.text
    lines = outputText.split("\n")
    
    unwanted_last_line = "```"
    if lines and lines[-1] == unwanted_last_line:
        lines = lines[1:-1]
    else:
        lines = lines[1:]
    new_text = "\n".join(lines)
    
    return new_text


if __name__ == "__main__":
    text, filename = file_extractor()
    testcase_text = testcase_generator(text)
    create_test_file(testcase_text, filename)
