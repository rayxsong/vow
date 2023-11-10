#!/usr/bin/env python3
import subprocess
import sys
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def run_command(command):
    try:
        # Run the command and capture output
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def get_input():
    command = ""
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            command += sys.argv[i] + " "
        return command
    else:
        print("No command provided.")
        return None

def main():

    client = OpenAI(
        api_key= os.getenv("OPENAI_API_KEY"),
    )

    user_input = get_input()
    if user_input == "exit":
        exit()
    raw_input = "Give me the command to run:" + user_input + "in MacOS terminal, give me the output directly without any explaination in one line."

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": raw_input,
            }
        ],
        model="gpt-3.5-turbo",
    )
    raw_output = completion.choices[0].message.content
    print("The following command will run: ")
    print("================================")
    print(raw_output)
    print("================================")
    print("Are you sure to run? (y/n)")
    if input() == "y":
        run_command(raw_output)
    else:
        print("Command cancelled.")

if __name__ == "__main__":
    main()