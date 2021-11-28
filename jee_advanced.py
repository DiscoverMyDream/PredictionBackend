import sys
import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

jee19CRL=pd.read_excel('JEE Advanced 2019.xlsx',skiprows=1,sheet_name=0)
jee19OBC=pd.read_excel('JEE Advanced 2019.xlsx',skiprows=1,sheet_name=1)
jee19SC=pd.read_excel('JEE Advanced 2019.xlsx',skiprows=1,sheet_name=2)
jee19ST=pd.read_excel('JEE Advanced 2019.xlsx',skiprows=1,sheet_name=3)
jee20CRL=pd.read_excel('JEE Advanced 2020.xlsx',skiprows=1,sheet_name=0)
jee20OBC=pd.read_excel('JEE Advanced 2020.xlsx',skiprows=1,sheet_name=1)
jee20SC=pd.read_excel('JEE Advanced 2020.xlsx',skiprows=1,sheet_name=2)
jee20ST=pd.read_excel('JEE Advanced 2020.xlsx',skiprows=1,sheet_name=3)

def trainData(dataset,totalMarks):
  X=dataset["Marks"]/totalMarks
  y=dataset["Rank"]
  X=pd.DataFrame(X)
  reg = RandomForestRegressor(n_estimators = 100, max_depth=8)
  reg.fit(X.values,y.values)
  return reg

def trainDataO(dataset,totalMarks):
  X=dataset["Marks"]/totalMarks
  y=dataset["Rank"]
  X=pd.DataFrame(X)
  reg = RandomForestClassifier(n_estimators = 400, criterion='entropy' ,random_state = 0)
  reg.fit(X.values,y.values)
  return reg

def estimation(marks,model4,model5):
  est4=math.ceil(model4.predict([[marks]])[0])
  est5=math.ceil(model5.predict([[marks]])[0])
  maxi=max(est4,est5)
  mini=min(est4,est5)
  if marks==1.0:
    mini=1
  if maxi==mini: 
    mini=max(mini-1,1)
    maxi=maxi+1 
  avg=(est4+est5)//2
  print(int(avg))
  print(int(mini))
  print(int(maxi) )
  return avg,mini,maxi

def prediction(marks,category):
  if category=="OPEN":
    CRLmodel4=trainData(jee19CRL,372)
    CRLmodel5=trainData(jee20CRL,396)
    return estimation(marks,CRLmodel4,CRLmodel5)
  elif category=="OBC-NCL":
    OBCmodel4=trainDataO(jee19OBC,372)
    OBCmodel5=trainDataO(jee20OBC,396)
    return estimation(marks,OBCmodel4,OBCmodel5)
  elif category=="SC":
    SCmodel4=trainDataO(jee19SC,372)
    SCmodel5=trainDataO(jee20SC,396)
    return estimation(marks,SCmodel4,SCmodel5)  
  elif category=="ST":
    STmodel4=trainDataO(jee19ST,372)
    STmodel5=trainDataO(jee20ST,396)
    return estimation(marks,STmodel4,STmodel5)

mark=int(sys.argv[1])/int(sys.argv[2])
prediction(mark,sys.argv[3])

