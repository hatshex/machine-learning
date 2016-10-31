
# coding: utf-8

# In[112]:

import pandas as pd
import numpy as np
import scipy.stats as st
import math as mth
from random import random, randint
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression
from scipy.stats import norm 
import matplotlib.pyplot as plt

#Carga archivos
get_ipython().magic('matplotlib inline')
df1=pd.read_csv('regLin.csv')
df2=pd.read_csv('regLin2.csv')
df3=pd.read_csv('regLin3.csv')


# In[113]:

#Separo mis datos en Train y Test
X1_tr, X1_t, Y1_tr, Y1_t = train_test_split(df1[df1.columns[0:-1]],df1[df1.columns[-1]], train_size=0.75)
X2_tr, X2_t, Y2_tr, Y2_t = train_test_split(df2[df2.columns[0:-1]],df2[df2.columns[-1]], train_size=0.75)
X3_tr, X3_t, Y3_tr, Y3_t = train_test_split(df3[df3.columns[0:-1]],df3[df3.columns[-1]], train_size=0.75)


# In[114]:

plt.scatter(X1_tr,Y1_tr)


# In[115]:

plt.scatter(X2_tr,Y2_tr)


# In[86]:

plt.scatter(X3_tr,Y3_tr)


# In[123]:

regr1 = LinearRegression()
regr1.fit(X1_tr, Y1_tr)


# In[175]:

# Graficar los datos y el resultado del modelo lineal
# Coeficientes
regr1 = LinearRegression()
regr1.fit(X1_tr, Y1_tr)print('Coeficientes: \n', regr1.coef_)
# Suma errores al cuadrado
print("Suma de los errores al cuadrado: %.2f"
      % np.mean((regr1.predict(X1_t) - Y1_t) ** 2))

plt.scatter(X1_t, Y1_t,  color='blue')
plt.plot(X1_t, regr1.predict(X1_t), color='red',linewidth=3)


# In[176]:

w1=regr1.coef_
w0=regr1.intercept_


# In[177]:

W=np.arange(-10,10,.1)
error =[]
for i in W:
    Y_estimada = (regr1.predict(X1_tr))+i
    C= np.subtract(Y_estimada, Y1_tr)
    C= C**2
    error.append(np.mean(C))

plt.plot(W,error)
plt.scatter(w1,np.mean(((w1*df['X'] + w0 )-df['y'])**2),color="red")
#plt.scatter(w1,np.mean(((w1* X_train['X'] + w0 )-Y_train['y'])**2),color="red")


# In[183]:

regr2 = LinearRegression()
X2_trans=[[i+i**2] for i in X2_tr['X']]
regr2.fit(X2_trans, Y2_tr)
plt.scatter(X2_t, Y2_t,  color='black')
x=np.linspace(0,100,100)
xt=[[i+i**2] for i in x]
plt.plot(x, regr2.predict(xt), color='red', linewidth=1)


# In[181]:

w1=regr2.coef_
w0=regr2.intercept_
W=np.arange(-10,10,.1)
error =[]
X2_trans=[[i+i**2] for i in X2_tr['X']]
for i in W:
    Y_estimada = (regr2.predict(X2_trans))+i
    C= np.subtract(Y_estimada, Y2_tr)
    C= C**2
    error.append(np.mean(C))

plt.plot(W,error)
plt.scatter(w1,np.mean(((w1*df2['X'] + w0 )-df2['y'])**2),color="red")


# In[129]:

regr3 = LinearRegression()

regr3.fit([[mth.sin(i)] for i in X3_tr['X']], Y3_tr)
plt.scatter(X3_t, Y3_t,  color='blue')
x=np.linspace(0,100,100)
xt=[[mth.sin(i)] for i in x]
plt.plot(x, regr3.predict(xt), color='red', linewidth=1)


# In[ ]:



