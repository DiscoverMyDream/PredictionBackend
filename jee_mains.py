# -*- coding: utf-8 -*-
import sys
import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

jee17CRL_1=pd.read_excel('JEE Mains 2017 P1.xlsx',skiprows=1,sheet_name=0)
jee17OBC_1=pd.read_excel('JEE Mains 2017 P1.xlsx',skiprows=1,sheet_name=1)
jee17SC_1=pd.read_excel('JEE Mains 2017 P1.xlsx',skiprows=1,sheet_name=2)
jee17ST_1=pd.read_excel('JEE Mains 2017 P1.xlsx',skiprows=1,sheet_name=3)
jee18CRL_1=pd.read_excel('JEE Mains 2018 P1.xlsx',skiprows=1,sheet_name=0)
jee18OBC_1=pd.read_excel('JEE Mains 2018 P1.xlsx',skiprows=1,sheet_name=1)
jee18SC_1=pd.read_excel('JEE Mains 2018 P1.xlsx',skiprows=1,sheet_name=2)
jee18ST_1=pd.read_excel('JEE Mains 2018 P1.xlsx',skiprows=1,sheet_name=3)

def trainData(dataset):
  X=dataset["Marks"]/360
  y=dataset["Rank"]
  X=pd.DataFrame(X)
  reg = RandomForestRegressor(n_estimators = 500, random_state = 0)
  reg.fit(X,y)
  return reg

def trainDataO(dataset):
  X=dataset["Marks"]/360
  y=dataset["Rank"]
  X=pd.DataFrame(X)
  reg = RandomForestClassifier(n_estimators = 400, criterion='entropy' ,random_state = 0)
  reg.fit(X,y)
  return reg



def estimation(marks,model1,model2):
  est1=math.ceil(model1.predict([[marks]])[0])
  est2=math.ceil(model2.predict([[marks]])[0])
  maxi=max(est1,est2)
  mini=min(est1,est2)
  if marks==1.0:
    mini=1
  if maxi==mini: 
    mini=max(mini-1,1)
    maxi=maxi+1 
  avg=(maxi+mini)//2  
  print(int(avg))
  print(int(mini))
  print(int(maxi) )
  

def prediction(marks,category):
  if category=="OPEN":
    CRLmodel1=trainData(jee17CRL_1)
    CRLmodel2=trainData(jee18CRL_1)
    return estimation(marks,CRLmodel1,CRLmodel2)
  elif category=="OBC-NCL":
    OBCmodel1=trainDataO(jee17OBC_1)
    OBCmodel2=trainDataO(jee18OBC_1)
    return estimation(marks,OBCmodel1,OBCmodel2)
  elif category=="SC":
    SCmodel1=trainDataO(jee17SC_1)
    SCmodel2=trainDataO(jee18SC_1)
    return estimation(marks,SCmodel1,SCmodel2)  
  elif category=="ST":
    STmodel1=trainDataO(jee17ST_1)
    STmodel2=trainDataO(jee18ST_1)
    return estimation(marks,STmodel1,STmodel2)
mark=int(sys.argv[1])/int(sys.argv[2])
prediction(mark,sys.argv[3])



