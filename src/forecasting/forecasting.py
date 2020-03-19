import itertools
import warnings

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from pylab import rcParams


def setup():
    warnings.filterwarnings("ignore")

    plt.style.use('fivethirtyeight')

    matplotlib.use('tkagg')
    matplotlib.rcParams['axes.labelsize'] = 14
    matplotlib.rcParams['xtick.labelsize'] = 12
    matplotlib.rcParams['ytick.labelsize'] = 12
    matplotlib.rcParams['text.color'] = 'k'

    rcParams['figure.figsize'] = 18, 8


def load_data_frame(path: str):
    return pd.read_excel(path)


def data_setup(data_frame):
    cols = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country',
            'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name',
            'Quantity', 'Discount', 'Profit']
    data_frame = data_frame.drop(cols, axis=1)
    data_frame = data_frame.sort_values('Order Date')
    data_frame = data_frame.groupby('Order Date')['Sales'].sum().reset_index()
    data_frame = data_frame.set_index('Order Date')
    return data_frame


def print_info(furniture, furniture_month_mean):
    print("innull sum:")
    print(furniture.isnull().sum())

    print("index:")
    print(furniture.index)

    print("furniture_month_mean")
    print(furniture_month_mean['2017':])


def plot(data):
    data.plot(figsize=(15, 6))
    plt.show()


def setup_arima_parameters():
    p = d = q = range(0, 2)
    pdq = list(itertools.product(p, d, q))
    seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

    print('Examples of parameter combinations for Seasonal ARIMA...')
    print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
    print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
    print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
    print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))
    return pdq, seasonal_pdq


def arima_optimization(data, pdq, seasonal_pdq):
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(data,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False)
                results = mod.fit()
                print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
            except:
                continue


def main():
    file_path = "../../data/Superstore.xls"

    dataframe = load_data_frame(file_path)

    furniture = dataframe.loc[dataframe['Category'] == 'Furniture']
    furniture_min, furniture_max = furniture['Order Date'].min(), furniture['Order Date'].max()
    print("furniture date range: ", furniture_min, furniture_max)

    furniture = data_setup(furniture)
    furniture_month_mean = furniture['Sales'].resample('MS').mean()

    print_info(furniture, furniture_month_mean)
    # plot(furniture_month_mean)

    # decomposition_plot(furniture_month_mean)

    pdq, seasonal_pdq = setup_arima_parameters()

    arima_optimization(furniture_month_mean, pdq, seasonal_pdq)


def decomposition_plot(furniture_month_mean):
    decomposition = sm.tsa.seasonal_decompose(furniture_month_mean, model='additive')
    fig = decomposition.plot()
    plt.show()


if __name__ == "__main__":
    main()
