# China_Commercial_Bank_LSTM_Prediction

This is a LSTM model that predicts the 5-day price of a few selected commercial banks in China. The model arises from that developed by Yufeng Chen, Jinwang Wu, and Zhongrui Wu. From their research, a group of 4 commercial banks are identified as highly correlated. The daily closing price of these 4 banks are trained with a multi-step output static prediction method to project the daily closing price of the next five days. The trained model have a mean absolute error of 0.084.

<br>Use LSTM_Data_Acquire.py to acquire data in xlsx form

<br>Use LSTM.ipynb to train the model the see the result

<br>"python images" folder contain the visualized result of the prediction
