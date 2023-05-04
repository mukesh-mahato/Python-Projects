# Import the required libraries
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Obtain the historical stock price data
df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1262304000&period2=1619798400&interval=1d&events=history&includeAdjustedClose=true')

# Preprocess the data
df = df[['Date', 'Close']]
df = df.dropna()
df['Close'] = df['Close'] / df['Close'].max()
train_data = df.iloc[:-200, 1].values.reshape(-1, 1)
test_data = df.iloc[-200:, 1].values.reshape(-1, 1)

# Build the LSTM model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(1, 1)))
model.add(Dense(1))
model.compile(optimizer=Adam(), loss='mse')

# Train the model
train_data = train_data.reshape((train_data.shape[0], 1, 1))
history = model.fit(train_data, train_data, epochs=100, batch_size=32, validation_split=0.2)

# Make predictions on the test data
test_data = test_data.reshape((test_data.shape[0], 1, 1))
predictions = model.predict(test_data)

# Plot the actual and predicted stock prices
plt.plot(df['Close'][-200:].values, label='Actual Stock Price')
plt.plot(predictions.flatten(), label='Predicted Stock Price')
plt.legend()
plt.show()
