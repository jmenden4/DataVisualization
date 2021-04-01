import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv("../Datasets/CoronaTimeSeries.csv")
df["Date"] = pd.to_datetime(df["Date"])


data = [
    go.Scatter(x=df["Date"], y=df["Confirmed"], mode="lines", name="Death"),
    go.Scatter(x=df["Date"], y=df["Recovered"], mode="lines", name="Recovered"),
    go.Scatter(x=df["Date"], y=df["Unrecovered"], mode="lines", name="Unrecovered"),
]

# Preparing layout
layout = go.Layout(
    title="Corona Virus Death and Recovered Cases from 2020-01-22 to 2020-03-17",
    xaxis_title="Date",
    yaxis_title="Number of cases",
)

# Plot the figure and save html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="multilinechart.html")