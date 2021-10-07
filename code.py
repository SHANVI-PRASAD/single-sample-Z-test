import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    setOfMeans = random_set_of_mean(100)
    mean_list.append(setOfMeans)
standarddev = statistics.stdev(mean_list)

first_stdev_start, first_stdev_end = mean-standarddev, mean+standarddev
second_stdev_start, second_stdev_end = mean-(2*standarddev), mean+(2*standarddev)
third_stdev_start, third_stdev_end = mean-(3*standarddev), mean+(3*standarddev)

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
meanofSample = statistics.mean(data)
print("mean of the sample", meanofSample)
fig = ff.create_distplot([mean_list],["reading time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[meanofSample,meanofSample],y=[0,0.17],mode="lines", name="mean of reading time"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.17],mode="lines", name="second standard deviation"))
fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode="lines", name="third standard deviation"))

fig.show()

z_score = (mean-meanofSample)/standarddev
print("the z score is", z_score)