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

#Q4: Willing to work for an employer without clearly defined mission:

question4 = 'Would you work for a company whose mission is not clearly defined and publicly posted.'
question4 = data[question4].value_counts()

label = question4.index
counts = question4.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q4: Willing to work for an employer without clearly defined mission')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: Majority of respondents feel the mission of a company is important and should be properly defined.
# So, if it is not clearly defined, 66.8% will not work for an employer whose mission is not clearly defined or publicly posted.
# And 33.2% would be open to work for such an employer.

#Q5: Willing to work for an employer whose mission misaligns wrt their public actions:

question5 = 'How likely would you work for a company whose mission is misaligned with their public actions or even their product ?'
question5 = data[question5].value_counts()

label = question5.index
counts = question5.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q5: Willing to work for an employer whose mission misaligns wrt their public actions')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: A similar trend like the last question can be seen for this question as well.
# Majority of respondents feel the mission of a company is important and should be properly defined which aligns with their public actions.
# So, if it is misaligned, 67.2% will not work for an employer and 32.8% would be open to work for such an employer.

#Q6: Willing to work for an employer whose mission is not bringing social impact:

question6 = 'How likely would you work for a company whose mission is not bringing social impact ?'
data['question6_cat'] = data[question6].map(lambda x: '9-10 Most Likely' if x >= 9 else ('7-8 Maybe' if x >= 7 else '1-6 Least Likely'))
question6 = data['question6_cat'].value_counts()

label = question6.index
counts = question6.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q6: Willing to work for an employer whose mission is not bringing social impact')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: A similar trend like the last two question can be seen for this question as well.
# Majority of respondents feel the mission of a company is important and should bring an impact to society.
# So, if it is misaligned, 65.2% will be least likely to work for such an employer, 27.7% might consider working for them, and 7.23% would be open to work for such an employer.

#Q7: Most Preferred Work Environment:

question7 = 'What is the most preferred working environment for you.'
question7 = data[question7].value_counts()

label = question7.index
counts = question7.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q7: Most Preferred Work Environment')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: 4.68% respondents choose that they want to work fully remotely with never visiting office.
# Another 25.5% also wish for a fully remote option but are open to visiting when needed.
# 48.6% wish to work in a hybrid environment where they don't have to visit office everyday.
# 21.3% prefer to work from office everyday.

#Q8: Preferred Values in Employers:

question8 = 'Which of the below Employers would you work with.'
question8 = data[question8].value_counts()

label = question8.index
counts = question8.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q8: Preferred Values in Employers')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: 48.1% prefer a challenging and learning environment, which rewards the efforts of employees.
# 31.9% prefer a learning and enabling environment. 15.3% prefer a rewarding and enabling environment.
# 2.98% prefer a challenging environment but doesn't have a learning and rewarding component.
# 1.7% prefer learning but are open to an environment which does not enable a learning environment.

#Q9: Preferred type of learning environment:

question9 = 'Which type of learning environment that you are most likely to work in ?'
question9 = data[question9].value_counts()

label = question9.index
counts = question9.values

fig = go.Figure(data=[go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = 'Q9: Preferred type of learning environment')
fig.update_traces(hoverinfo = 'label+value', textinfo = 'percent', textfont_size = 30,
                  marker = dict(colors = colors, line = dict(color = 'black', width = 3)))

fig.show()

#COMMENT: 51.09% prefer a self-paced learning option with different choices of either learning by observing others or trial and error with hands-on experience.
# 36.5% prefer a instructor or expert learning programs with a hands-on trial and error experience.
# Finally, 12.3% choose to learn by observing others, and get hands-on practice with trial and error.