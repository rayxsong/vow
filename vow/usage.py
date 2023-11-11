# usage.py
import argparse
import configparser
import os


def menu():
    parser = argparse.ArgumentParser(description='Vow CLI Tool')
    parser.add_argument('-reset', action='store_true', help='Reset the stored API key to default')
    parser.add_argument('-show', action='store_true', help='Show the current API key')
    parser.add_argument('-model', action='store_true', help='Change the GPT model')
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
            # If not found in config, prompt the user to enter it
            model = input("Enter your OpenAI model(ex. gpt-3.5-turbo, gpt-4): ")

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