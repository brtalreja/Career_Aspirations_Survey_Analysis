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

#Country
country = data["Your Current Country."].value_counts()

label = country.index
counts = country.values

colors = ['Yellow', 'lime']

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Demographics: Current Country')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line=dict(color = 'black', width = 3)))
fig.show()

#COMMENT: The respondents belong to India, Germany, United Arab Emirates, and United States of America. Majority of them are from India (98.3%).

#Gender

gender = data["Your Gender"].value_counts()

label = gender.index
counts = gender.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Demographics: Gender')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors=colors, line=dict(color = 'black', width = 3)))
fig.show()

#COMMENT: Two thirds of the respondents are females and one-thrids of the respondents are males.

#Q1: Factors influencing the career aspirations of Genz:

question1 = data['Which of the below factors influence the most about your career aspirations ?'].value_counts()

label = question1.index
counts = question1.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q1: Factors Influencing Career Aspirations')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: Parents and Social idols play an important part in shaping an individual's career aspirations.
# Approximately 58% of the respondents choose what their parents want them to pursue or what their social idols do.
# Remaining 42% of GenZ are influenced by successful influencers, social media like LinkedIn, and known associations.

#Q2: Interest in pursuing self-sponsored Higher Education:

question2 = 'Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.'
question2 = data[question2].value_counts()

label = question2.index
counts = question2.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q2: Interest in pursuing self-sponsored Higher Education')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: Approximately 47% of the GenZ are interested in pursuing a higher education with their self-earned income.
# 27.7% said no to pursuing higher education outside India.
# While the remaining respondents said a conditional yes, i.e. they would not pursue it with their own expenses but if they get some scholarship or financial assistance, they will do it.

#Q3: Interested in working for an employer for 3 years or more:

question3 = 'How likely is that you will work for one employer for 3 years or more ?'
question3 = data[question3].value_counts()

label = question3.index
counts = question3.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q3: Interested in working for an employer for 3 years or more')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: 59.1% find it difficult to do so, but if the company is good, they might do it.
# 33.6% are willing to do it without any hesitations.
# Finally, 7.2% will not do it under any circumstances.

#Q4: 