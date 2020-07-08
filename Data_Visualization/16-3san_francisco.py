
import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'san_francisco.csv'


with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)

	#for index, column_header in enumerate(header_row):
	#	print(index, column_header)

	# Get dates, high and low temperatures from this file.
	highs, lows =[], []
	for row in reader:
		#current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = float(row[14])
		low = float(row[16])
		#dates.append(current_date)
		highs.append(high)
		lows.append(low)

#Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red', alpha=0.5)
ax.plot(lows, c='blue', alpha=0.5)
ax.fill_between(highs, lows, facecolor='blue', alpha=0.1)

#Format plot.
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (f)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

