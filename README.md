# vow - open source cli copilot in python

Currently it only supports your own OpenAI API key.

## Usage
```
vow -h
usage: vow [-h] [-reset] [-show] [-model] ...

Vow CLI Tool

positional arguments:
  command     Command to ask for GPT model

optional arguments:
  -h, --help  show this help message and exit
  -reset      Reset the stored API key to default
  -show       Show the current API key
  -model      Change the GPT model
  -os         Change the OS of generated cli
```
## Demo
Consider you want to install tensorflow but don't know how, type `vow` and your requirement:
```python
vow install tensorflow
```

It asks OpenAI API to search for the command and run it if you think it is safe:
```python
The following command will run: 
================================
pip install tensorflow
================================
Are you sure to run? (y/n)
n
================================
Command cancelled.
```
## To-do:
- [ ] Security chcek
- [ ] Pip package
- [ ] Multi-line commands running
- [x] GPT model change
- [x] API key change and reset
- [x] Add usage
- [x] Orgnize the structure
- [x] Support other os cli
- [ ] Add reasoning/explaination
- [ ] Add feedback if the user wants to update
- [ ] Add simple mode
- [ ] Consider virtual running
