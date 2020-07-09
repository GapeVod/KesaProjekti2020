import csv
from datetime import datetime

import matplotlib.pyplot as plt


death_valley = 'death_valley_2018_simple.csv'
sitka = 'sitka_weather_2018_simple.csv'

with open(death_valley) as df:
	reader_death = csv.reader(df)
	header_row = next(reader_death)

	dates, highs_death = [], []
	for row in reader_death:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high_death = int(row[4])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs_death.append(high_death)

with open(sitka) as sf:
	reader_sitka = csv.reader(sf)
	header_row = next(reader_sitka)

	dates, highs_sitka = [], []
	for row in reader_sitka:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high_sitka = int(row[5])
		dates.append(current_date)
		highs_sitka.append(high_sitka)

#Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs_death, c='red', alpha=0.5)
ax.plot(dates, highs_sitka, c='blue', alpha=0.5)
ax.fill_between(dates, highs_death, facecolor='blue', alpha=0.1)
ax.set_ylim([0, 150])

#Format plot.
title ="comparison between sitka and death valley"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (f)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()