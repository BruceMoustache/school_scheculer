import random
from config import classes_per_week, classes_per_day


standard_day_reference = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sturday']

def get_day_name(index, reference = standard_day_reference):
	return reference[index]


single_schedule = []
for counter in range(len(standard_day_reference)):
	single_schedule.append([None] * classes_per_day)
print(single_schedule)

