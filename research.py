from mlProject.pipeline.prediction import PredictionPipeline
import numpy as np

state= 5
numcol = 22
yieldpercol = 22
totalprod =5
stocks =25
prodvalue=22
year=2022

data = [state, numcol, yieldpercol, totalprod, stocks, prodvalue, year]
data = np.array(data).reshape(1, 7)

obj = PredictionPipeline()
predict = obj.predict(data)

print(predict)