import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/sitka_weather_2018_simple.csv'


#plt.ylim((0, 150))

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)

	#for index, column_header in enumerate(header_row):
		#print(index, column_header)

	# Get high temperatures from this file.
	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)

#Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.set_ylim([0, 150])

#Format plot.
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (f)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()