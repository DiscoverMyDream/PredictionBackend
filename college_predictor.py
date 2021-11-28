# -*- coding: utf-8 -*-
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import StandardScaler
np.set_printoptions(suppress=True)

dataset=sys.argv[1]
df = pd.read_csv(dataset,names=['1','2','3','4'])

X = df[['1','2']].values
Y = df['3'].values

model = Sequential()

layer1=Dense(units=32, activation = 'relu', input_dim =2)
model.add(layer1)
model.add(Dense(units=16,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)


sc=StandardScaler()
X=sc.fit_transform(X)
x_test=sc.transform(x_test)

model.fit(X, Y, epochs = 50, batch_size = 50, validation_data = (x_test,y_test),verbose=0)

#predictions = model.predict(x_test)
#score = model.evaluate(x_test,y_test,verbose=0)

marks=int(sys.argv[2])
gpa=float(sys.argv[3])
inputA=[[marks,gpa]]
inputA=sc.transform(inputA)
ans = model.predict(inputA)

print(int(ans[0][0]*100))



