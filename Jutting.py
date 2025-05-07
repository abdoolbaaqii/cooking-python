# km = kilomneter
# min = minutes
# sec = seconds

given_distance = 10 # in km
one_mile = 1.61 # in km
miles_in_10_km = (given_distance/one_mile)
print(miles_in_10_km)

# total time given = 42 min 42 sec
total_time_in_sec = (42*60) + (42)
average_pace = (total_time_in_sec/miles_in_10_km)
print(average_pace)

average_speed = (miles_in_10_km/total_time_in_sec)
print(average_speed)
