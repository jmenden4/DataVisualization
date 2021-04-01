import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#Load CSV file from Datasets folder
df = pd.read_csv("../Datasets/CoronavirusTotal.csv")

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating unrecovered column
df["Unrecovered"] = df["Confirmed"] - df["Deaths"] - df["Recovered"]

# Remove China from data frame
df = df[(df["Country"] != "China")]

# Creating sum of number of cases group by Country
new_df = df.groupby(["Country"]).agg(
    {
        "Confirmed": "sum",
        "Deaths": "sum",
        "Recovered": "sum",
        "Unrecovered": "sum",
    }
).reset_index()

# Sorting values and select 20 first values
new_df = new_df.sort_values(by=["Confirmed"], ascending=[False]).head(20).reset_index()

# Preparing data
trace1 = go.Bar(x=new_df["Country"], y=new_df["Unrecovered"], name="Unrecovered", marker={"color": "#CD7F32"})
trace2 = go.Bar(x=new_df["Country"], y=new_df["Recovered"], name="Recovered", marker={"color": "#9EA0A1"})
trace3 = go.Bar(x=new_df["Country"], y=new_df["Deaths"], name="Deaths", marker={"color": "#FFD700"})
data = [trace1, trace2, trace3]

# Preparing layout
layout = go.Layout(
    title="Corona Virus Cases in teh first 20 countries except China",
    xaxis_title="Country",
    yaxis_title="Number of cases",
    barmode="stack",
)

# Plot the figure and save html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="stackbarchart.html")