from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Dropout

import numpy as np   

class SomeModel:
  def __init__(self):
    self.status = "I'm Alive"

  def fit_model(self):

    model = Sequential()
    model.add(Dense(16, input_shape=(1,), activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    
    X_train = np.linspace(0, 10, int(1e3))
    y_train = X_train*4.20

    model.compile(loss='mse', optimizer='adam', metrics=['mae'])
    history = model.fit(
      X_train, 
      y_train, 
      # batch_size="lol", # try invalid value
      batch_size=int(1e9), 
      epochs=100
    )
    return history