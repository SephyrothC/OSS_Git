# COVID-19 Statestics

## To do 
* [x] Calculate the number of cases per its population
* [x] Calculate the total number of people  
* [x] Calculate the total number of new cases
* [x] The ratio of new cases to the total
* [x] Print COVID-19 new cases by region

## Results
### Korean Population by Region
* Total population: 51669716

| Region | Population | Ratio (%) |
| ------ | ---------- | --------- |
| Seoul | 9550227 | 18.5 |
| Gyeongi | 13530519 | 26.2 |
| Busan | 3359527 | 6.5 |
| Gyeongnam | 3322373 | 6.4 |
| Incheon | 2938429 | 5.7 |
| Gyeongbuk | 2630254 | 5.1 |
| Daegu | 2393626 | 4.6 |
| Chungnam | 2118183 | 4.1 |
| Jeonnam | 1838353 | 3.6 |
| Jeonbuk | 1792476 | 3.5 |
| Chungbuk | 1597179 | 3.1 |
| Gangwon | 1536270 | 3.0 |
| Daejeon | 1454679 | 2.8 |
| Gwangju | 1441970 | 2.8 |
| Ulsan | 1124459 | 2.2 |
| Jeju | 675883 | 1.3 |
| Sejong | 365309 | 0.7 |
### COVID-19 cases by Region
* Total cases: 1714

| Region | New Cases | Ratio (%) | New cases / 1M |
| ------ | ---------- | --------- | --------- |
| Seoul | 644 | 37.6 | 67.4 |
| Gyeongi | 529 | 30.9 | 39.1 |
| Busan | 38 | 2.2 | 11.3 |
| Gyeongnam | 29 | 1.7 | 8.7 |
| Incheon | 148 | 8.6 | 50.4 |
| Gyeongbuk | 28 | 1.6 | 10.6 |
| Daegu | 41 | 2.4 | 17.1 |
| Chungnam | 62 | 3.6 | 29.3 |
| Jeonnam | 23 | 1.3 | 12.5 |
| Jeonbuk | 27 | 1.6 | 15.1 |
| Chungbuk | 27 | 1.6 | 16.9 |
| Gangwon | 33 | 1.9 | 21.5 |
| Daejeon | 16 | 0.9 | 11.0 |
| Gwangju | 40 | 2.3 | 27.7 |
| Ulsan | 20 | 1.2 | 17.8 |
| Jeju | 5 | 0.3 | 7.4 |
| Sejong | 4 | 0.2 | 10.9 |

## What I added

### I have added a graph of COVID-19 new cases by region
  
![](./Figure_1.png)

#### code :

```py
plt.bar(regions, n_covid ,label="COVID-19", width = 0.8, color = ['blue']) # view of the bar
plt.xlabel('Region') # x label
plt.ylabel('Number of cases per region') # y label
plt.title('COVID-19 new cases by region') # title of the graph
plt.legend() # add legend

plt.show() # show the graph
```

### I have added a graph of the ratio of new cases per person by region

![](./Figure_2.png)

### code :

```py
ratio = []
for idx, pop in enumerate(n_covid):
    ratio.append(n_covid[idx]*100/n_people[idx]) # Calculate ratio
plt.pie(ratio, labels = regions, autopct = '%1.1f%%') # view of the pie
plt.title("Ratio of new cases per person by region") # title of the graph
plt.show() # show the graph
```
