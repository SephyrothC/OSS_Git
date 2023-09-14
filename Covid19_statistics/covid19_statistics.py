import matplotlib.pyplot as plt

def normalize_data(n_cases, n_people, scale):
    # TODO) Calculate the number of cases per its population
    norm_cases = []
    for idx, n in enumerate(n_cases):        
        norm_cases.append( (n_cases[idx]/n_people[idx]) * scale )
    return norm_cases

regions  = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam', 'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227,  13530519, 3359527,     3322373,   2938429,     2630254, 2393626,    2118183,   1838353,   1792476,    1597179,   1536270,   1454679,   1441970, 1124459, 675883,   365309] # 2021-08
n_covid  = [    644,       529,      38,          29,       148,          28,      41,         62,        23,        27,         27,        33,        16,        40,      20,      5,        4] # 2021-09-21

sum_people = sum(n_people) # TODO) The total number of people
sum_covid  = sum(n_covid) # TODO) The total number of new cases
norm_covid = normalize_data(n_covid, n_people, 1000000) # The new cases per 1 million people

# Print population by region
print('### Korean Population by Region')
print('* Total population:', sum_people)
print() # Print an empty line
print('| Region | Population | Ratio (%) |')
print('| ------ | ---------- | --------- |')
for idx, pop in enumerate(n_people):
    ratio = (n_people[idx]*100/sum_people) # TODO) The ratio of new cases to the total
    print('| %s | %d | %.1f |' % (regions[idx], pop, ratio))
print()

# TODO) Print COVID-19 new cases by region
print('### COVID-19 cases by Region')
print('* Total cases:', sum_covid)
print()
print('| Region | New Cases | Ratio (%) | New cases / 1M |')
print('| ------ | ---------- | --------- | --------- |')
for idx, pop in enumerate(n_covid):
    ratio = (n_covid[idx]*100/sum_covid) # The ratio of new cases to the number of people in the region
    print('| %s | %d | %.1f | %0.1f |' % (regions[idx], pop, ratio , norm_covid[idx]))
print()


# Graphics about the COVID-19 new cases by region

# plt.bar(regions, n_covid ,label="COVID-19", width = 0.8, color = ['blue'])
# plt.xlabel('Region')
# plt.ylabel('Number of cases per region')
# plt.title('COVID-19 new cases by region')
# plt.legend()
# plt.show()


# Ratio of new cases per person by region

# ratio = []
# for idx, pop in enumerate(n_covid):
#     ratio.append(n_covid[idx]*100/n_people[idx])
# plt.pie(ratio, labels = regions, autopct = '%1.1f%%')
# plt.title("Ratio of new cases per person by region")
# plt.show()