import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima_model import ARIMA



# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return numpy.array(diff)

def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]

from pandas import Series
from statsmodels.tsa.arima_model import ARIMA
import numpy

# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return numpy.array(diff)


def predict(dataSeries):
    # load dataset
    # series = Series.from_csv('dataset.csv', header=None)
    #series = dataSeries
    # seasonal difference
    X = dataSeries
    days_in_year = 365
    differenced = difference(X, days_in_year)
    # fit model
    model = ARIMA(differenced, order=(7,1,5))
    model_fit = model.fit(disp=0)
    # print summary of fit model
    print(model_fit.summary())
    forecast = model_fit.predict(len(differenced), len(differenced)+120)
    print(forecast)

    forecast = model_fit.forecast(steps=120)[0]
    history = [x for x in X]
    predict = [history[-1]]
    day = 1
    for yhat in forecast:
        inverted = inverse_difference(history, yhat, days_in_year)
        print('Day %d: %f' % (day, inverted))
        history.append(inverted)
        predict.append(inverted)
        day += 1
    print(predict)

    return predict
    # def objfunc(order, exog, endog):
    #     from statsmodels.tsa.arima_model import ARIMA
    #     fit = ARIMA(endog, order, exog=exog).fit()
    #     ARIMA.predict()
    #     return fit.aic()
    #
    # class prediction:
    #     data = None
    #     output = None
    #     sd = None
    #     variance = None
    #     mean = None
    #
    #     def __init__(self, data):
    #         self.data = data
    #
    #     def process(self):
    #         from scipy.optimize import brute
    #         exog = tuple(float(x) for x in range(0, 534))
    #         print(exog)
    #         print(callable(exog))
    #         endog = self.data
    #         print(endog)
    #         objfunc(endog=endog, order=(1,2,1), exog=exog)
    #         # print(callable(endog))
    #         # grid = (slice(1, 3, 1), slice(1, 3, 1), slice(1, 3, 1))
    #         # params = brute(objfunc, grid, args=(exog,
    #         #                                     endog), finish=None)
    #         # print(params)
    #
    #
    # predict = prediction(tuple(pd.read_csv("emissions_by_source_73_17.csv").get("Total Energy")))
    # predict.process()
