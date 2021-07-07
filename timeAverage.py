#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pickle as pk
import numpy as np
import math as mt
from os import walk
import statistics as st
from matplotlib import pyplot
import scipy.stats as stats


# In[52]:


poblacion=100
archivo='high1e6final'
nbins=1000


# In[53]:


##Homogenously distributed 100'000 points 
totmeans=np.zeros(100000)
nfiles=0
mypath='D:\\datos_tesis\\'+archivo+'\\n'+str(poblacion)+'\\'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break
for filename in f:
    values=[]
    counter=0
    ndato=100000
    with open(mypath+filename,'rb') as openfile:
        nfiles+=1
        while (True):
            try:
                dato=pk.load(openfile)
                counter+=(len(dato)/poblacion)
                
                contin=0
                for i in dato:
                    if(counter>=100000 and contin%poblacion==0):
                        values.append(i)
                    contin+=1
            except EOFError:
                break
    values=values[0:100000]
    totmeans=np.add(values,totmeans)
totmeans=totmeans/nfiles


# In[7]:


## In order to generate averages, a variables to store the values for each file must be created independently, averaged and named (timeline#)


# In[63]:


#Graph means
times=[100000,110000,120000,130000,140000,150000,160000,170000,180000,190000]
pyplot.plot(times,timeline100,label='n100')
pyplot.plot(times,timeline1000,label='n1000')
pyplot.legend(loc='upper right')
pyplot.xlabel("Average number of plasmids")
pyplot.ylabel("Generations")
pyplot.title("Number of plasmids across generations")
pyplot.show()


# In[57]:


#Graph independent
times=[100000,110000,120000,130000,140000,150000,160000,170000,180000,190000]
pyplot.plot(times,allmeanshigh1000,label='high1000')
pyplot.plot(times,allmeanslow1000,label='low1000')
pyplot.plot(times,allmeanshigh100,label='high100')
pyplot.plot(times,allmeanslow100,label='low100')
pyplot.legend(loc='upper right')
pyplot.xlabel("Average number of plasmids")
pyplot.ylabel("Generations")
pyplot.title("Number of plasmids across generations")
pyplot.show()

