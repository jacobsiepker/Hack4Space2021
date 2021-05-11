Using monthly data from April 2015, which was recorded secondly. We applied resampling on variable ‘Dust Density’ by minutes to regroup the data, it improves model running time and model accuracy. 
ARIMA(3,0,4) was apply in this case, we were able to achieve 0.003 prediction errors, with an upward trending prediction of dusty density. 
Just by looking at April 2015, the Martian wind movements are stronger during the month, weaker at the beginning and the end of April. 

Library imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import *
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pandas.plotting import autocorrelation_plot
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARIMA # deprecated
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller 
from statsmodels.tsa.stattools import kpss
from statsmodels.tsa.arima_model import ARIMA
from pmdarima import auto_arima
import itertools