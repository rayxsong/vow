# usage.py
import argparse
import configparser
import os

model_list = ['gpt-3.5-turbo', 'gpt-3.5-turbo-instruct', 'gpt-4']

def menu():
    parser = argparse.ArgumentParser(description='Vow CLI Tool')
    parser.add_argument('-reset', action='store_true', help='Reset the stored API key to default')
    parser.add_argument('-show', action='store_true', help='Show the current API key')
    parser.add_argument('-model', action='store_true', help='Change the GPT model')
    parser.add_argument('-os', action='store_true', help='Change the cli OS')
    parser.add_argument('command', nargs=argparse.REMAINDER, help='Command to ask for GPT model')

    args = parser.parse_args()

    if args.reset:
        delete_api_key()
        print("API key reseted.")
        exit()
    
    if args.show:
        api_key = get_api_key()
        if len(api_key) == 0:
            print("No API key found.")
        else:
            print(api_key)
        exit()

    if args.model:
        model = get_model()
        switch_model()
        exit()

    if args.os:
        os_name = get_os()
        switch_os()
        exit()

def get_api_key():
    # First, try to get the API key from an environment variable
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        # If not found in environment, try to get it from a config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        if 'openai' in config and 'api_key' in config['openai']:
            api_key = config['openai']['api_key']
        else:
            # If not found in config, prompt the user to enter it
            api_key = input("Enter your OpenAI API key: ")

            # Optional: Save the entered API key to a config file for future use
            save = input("Do you want to save this API key for future use? (y/n): ").lower()
            if save == 'y':
                config['openai'] = {'api_key': api_key}
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)

    return api_key

def delete_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['openai'] = {'api_key': ""}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def print_model_list():
    # print the model list with index
    for i in range(len(model_list)):
        print(f"{i+1}. {model_list[i]}")

def get_model():
    # First, try to get the API key from an environment variable
    model = os.getenv('GPT_MODEL')

    if not model:
        # If not found in environment, try to get it from a config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        if 'openai' in config and 'model' in config['openai']:
            model = config['openai']['model']
        else:
            # If not the user to enter it
            print("Enter your OpenAI model found in config, prompt on the list: ")
            print_model_list()
            # limit input to the model list
            while True:
                model = input()
                if model in model_list:
                    break
                else:
                    print("Invalid model. Please choose from the list above.")

            # Optional: Save the entered API key to a config file for future use
            save = input("Do you want to save this model for future use? (y/n): ").lower()
            if save == 'y':
                config['openai'] = {'model': model}
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)

    return model

def switch_model():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # print the current model
    print("Current model is: " + config['openai']['model'])
    # check if the user wants to change the model
    print("Do you want to change the model? (y/n)")
    if input() == "y":
        # prompt the user to enter it
        model = input("Enter your OpenAI model(ex. gpt-3.5-turbo, gpt-4): ")
        # Optional: Save the entered API key to a config file for future use
        save = input("Do you want to save this model for future use? (y/n): ").lower()
        if save == 'y':
            config['openai'] = {'model': model}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        print("Model changed.")
    
def get_os():
    os_name = os.getenv('CLI_OS')

    if not os_name:
        # If not found in environment, try to get it from a config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        if 'openai' in config and 'os' in config['openai']:
            os_name = config['openai']['os']
        else:
            # If not found in config, prompt the user to enter it
            os_name = input("Enter your OS: ")

            # Optional: Save the entered API key to a config file for future use
            save = input("Do you want to save this OS for future use? (y/n): ").lower()
            if save == 'y':
                config['openai'] = {'os': os_name}
                with open('config.ini', 'w') as configfile:
                    config.write(configfile)
    return os_name

def switch_os():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # print the current model
    print("Current OS is: " + config['openai']['os'])
    # check if the user wants to change the model
    print("Do you want to change the OS? (y/n)")
    if input() == "y":
        # prompt the user to enter it
        os_name = input("Enter your OS: ")
        # Optional: Save the entered API key to a config file for future use
        save = input("Do you want to save this OS for future use? (y/n): ").lower()
        if save == 'y':
            config['openai'] = {'os': os_name}
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
        print("OS changed.")