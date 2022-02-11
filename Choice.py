from random import choice
from numpy import loadtxt


with open("text.txt",  "r", errors='ignore') as tf:
    lines = tf.read().split(' ')

text = []    
for line in lines:
    text.append(line)

frase = []
for i in range(15):
    palavra = choice(text)
    frase.append(palavra)
    
print(frase) 