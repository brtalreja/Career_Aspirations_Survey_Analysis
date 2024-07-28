#Importing Required Libraries.
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#Load the data.
data = pd.read_csv("../data/Your Career Aspirations of GenZ.csv")
print(data.head())

#Attributes in the data.
print(data.columns)

#Demographics Analysis.

country = data["Your Current Country."].value_counts()

label = country.index
counts = country.values

colors = ['gold', 'lightgreen']

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Demographics: Current Country')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size=30,
                  marker = dict(colors=colors, line=dict(color = 'black', width=3)))
fig.show()