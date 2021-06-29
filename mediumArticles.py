import random
import pandas as p
import plotly.figure_factory as pff
import plotly.graph_objects as go
import statistics

df = p.read_csv(".\medium_data.csv")
readingTime = df["reading_time"].tolist()

meanList = []

mean = statistics.mean(readingTime)
print("Mean of the given data:",mean)

std = statistics.stdev(readingTime)
print("Standard Deviation of the given data:",std)

def sampleDataAnalysis():
    sampleData = []
    for i in range(0,100):
        index = random.randint(0,len(readingTime) - 1)
        value = readingTime[index]
        sampleData.append(value)
    
    sdMean = statistics.mean(sampleData)
    return sdMean

for i in range(0,1000):
    SdMean = sampleDataAnalysis()
    meanList.append(SdMean)

meanListStd = statistics.stdev(meanList)
print("Standard deviation of the mean list:",meanListStd)

meanListMean = statistics.mean(meanList)
print("Mean of the mean list:",meanListMean)

std1 = statistics.stdev(meanList)
print("Standard Deviation 1 of mean list:",std1)
std2 = statistics.stdev(meanList) * 2
print("Standard Deviation 2 of mean list:",std2)
std3 = statistics.stdev(meanList) * 3
print("Standard Deviation 3 of mean list:",std3)
figure = pff.create_distplot(meanList,"Mean list")
figure.add_trace(go.Scatter(x=[std1,std1],y=[0,1],name="STD 1",mode="lines"))
figure.add_trace(go.Scatter(x=[std2,std2],y=[0,1],name="STD 2",mode="lines"))
figure.add_trace(go.Scatter(x=[std3,std3],y=[0,1],name="STD 3",mode="lines"))