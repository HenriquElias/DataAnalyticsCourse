import random
## -------------------------------------Part 1--------------------------------------------------
daily_temperatures = [random.randint(0, 35) for _ in range(30)] 

# initial conditions
lowest_temp = daily_temperatures[0]
highest_temp = daily_temperatures[0]
lowest_days = [0]
highest_days = [0]
above20 = []
below10 = []
increased_temp = []
hotter_than = daily_temperatures[0]
hotter_than_days = [0]

# 1) Find the day with the lowest temperature.
for day, temperature in enumerate(daily_temperatures):
    if temperature == lowest_temp:
        lowest_days.append(day)
    if temperature < lowest_temp:
          lowest_days = [day]
          lowest_temp = temperature

# 2) Find the day with the highest temperature.
for day, temperature in enumerate(daily_temperatures):
    if temperature == highest_temp:
        highest_days.append(day)
    if temperature > highest_temp:
          highest_days = [day]
          highest_temp = temperature

# 3) Find the days where the temperature rises above 20°C.
for day,temperature in enumerate(daily_temperatures):
     if temperature > 20:
        above20.append(day)

# 4) Find the days where the temperature drops below 10°C.
for day,temperature in enumerate(daily_temperatures):
     if temperature < 10:
        below10.append(day)

# 5) Find the days where the temperature increased from the day before
diff = [daily_temperatures[i+1]-daily_temperatures[i] for i in range(len(daily_temperatures)-1)]
for i in range(len(diff)):
    if diff[i] > 0:
        increased_temp.append(i+1)

# 6) Find the days where the temperature was hotter than any of the days previous in the month.
for day,temperature in enumerate(daily_temperatures):
    if temperature > hotter_than:
        hotter_than = temperature
        hotter_than_days.append(day)

print('\n')
print('-----PART 1-----')
print('\n')
print('Daily Temps: ',daily_temperatures)
print('\n')
print('The lowest temperature of the month was {}°C, occurring on day(s) {}'.format(lowest_temp,lowest_days))
print('The highest temperature of the month was {}°C, occurring on day(s) {}'.format(highest_temp,highest_days))
print('days w/ temperature above 20°C: ', above20)
print('days w/ temperature below 10°C: ', below10)
print('days the temperature increased from the day before', increased_temp)
print('days hotter than any previous: ', hotter_than_days)
print('\n')

## -------------------------------------Part 2--------------------------------------------------

daily_rainfall = [random.randint(0, 10) for _ in range(30)]

#initial conditions for part 2
count_bw = 0
count_aw = 0 
count_gw = 0
day_bw = []
day_aw = []
day_gw = []

for day,(temp,rain) in enumerate(zip(daily_temperatures,daily_rainfall)):
    if (temp < 10) and (rain > 3): # Bad Weather
        count_bw += 1
        day_bw.append((day,temp,rain))
    if (temp > 10 and temp < 18) and (rain > 1 and rain < 5): # Average Weather
        count_aw += 1
        day_aw.append((day,temp,rain))
    if (temp > 18) and (rain < 2): # Good Weather
        count_gw += 1
        day_gw.append((day,temp,rain))

print('-----PART 2-----')
print('\n')
print('Daily Rainfall: ', daily_rainfall)
print('\n')
print('amount of "bad weather" days: ', count_bw)
print('amount of "average weather" days: ', count_aw)
print('amount of "good weather" days: ', count_gw)
print('\n')
print('list of tuples w day index, temperature and rainfall information, just to make it easier to compare')
print('\n')
print('tuples w bad weather info(day, temp, rain): ', day_bw)
print('tuples w average weather info(day, temp, rain): ', day_aw)
print('tuples w good weather info(day, temp, rain): ', day_gw)