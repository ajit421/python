import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from io import StringIO  

from google.colab import files
uploaded = files.upload()

file_name = next(iter(uploaded))
df = pd.read_csv(StringIO(uploaded[file_name].decode('utf-8'))) 
plt.scatter(df['Time on Website'], df['Avg. Session Length'])
plt.xlabel('Time on Website')
plt.ylabel('Avg. Session Length')
plt.title('Time on Website vs Avg. Session Length')
plt.show()

from google.colab import files
uploaded = files.upload()
file = open('comand.txt','r')
print(file.read())
file.close()

file = open('result.txt','w')
file.write("Welcome to AI training program")
file.close()

file=open('result.txt','r')
print(file.read())
file.close()