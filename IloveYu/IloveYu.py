#!/usr/bin/python3
from cryptography.fernet import Fernet
"""R"""

def f():
    """fonction f"""
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()
        
    fernet = Fernet(key)
	
    with open('play.hard', 'rb') as c_t_d:
        e_c = c_t_d.read()
    c = fernet.decrypt(e_c)
    exec(c)

if __name__ == '__main__':
	f()
