# Prototype of vow

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
- [ ] GPT model change
- [ ] API key change 