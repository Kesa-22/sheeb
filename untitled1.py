# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XiVzxs2JNYyqBuZ8jI-HZX-IJsNWh8pw
"""

name=["keerthi", "kesa", "varthini", "kathir", "sheeba"]
father_name=["velmurugan", "ramesh", "tharun", "harshan", "dhurai"]
doy=[1999, 2000, 2001, 2002, 2003]
status=['daughter', 'daughter', 'daughter', 'son', 'daughter']
import pandas as pd
df=pd.DataFrame({'Name':name, 'father':father_name, 'yr of birth':doy, 'son/daughter': status})
print(df)

age=2022-df['yr of birth']
df['age']=(2022-df['yr of birth'])*2
df



