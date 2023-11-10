# Prototype of vow

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