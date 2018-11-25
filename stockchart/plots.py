import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
import twstock
import datetime


def plotChandleStick():
    stock_6207 = twstock.Stock('6207')
    stock_6207_2016 = stock_6207.fetch_from(2016,1)
    stock_6207_2016_pd=pd.DataFrame(stock_6207_2016)

    trace = go.Candlestick(x=stock_6207_2016_pd.date,
                       open=stock_6207_2016_pd.open,
                       high=stock_6207_2016_pd.high,
                       low=stock_6207_2016_pd.low,
                       close=stock_6207_2016_pd.close)

    data = [trace]
    layout = go.Layout(
         autosize=True,
        # width=900,
        # height=500,

        xaxis=dict(
            autorange=True
        ),
        yaxis=dict(
            autorange=True
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    logger.info("Plotting number of points {}.".format(len(x_data)))
    return plot_div
