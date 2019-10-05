import random
from config import map_classes_per_week, counter_classes_per_day, available_days_interval


standard_day_reference = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sturday']
indexes_of_available_days_interval = standard_day_reference.index(available_days_interval[0]), standard_day_reference.index(available_days_interval[1])

def get_day_name(index, reference = standard_day_reference):
	return reference[index]

def show_schedule(schedule):
	for day_index, day_list in enumerate(schedule):
		print(get_day_name(day_index))
		for subject in day_list:
			print('\t', subject)


schedule = []
for counter in range(len(standard_day_reference)):
	schedule.append([None] * counter_classes_per_day)

for subject in map_classes_per_week:
	remaining_sheduling = map_classes_per_week[subject]
	while remaining_sheduling > 0:
		while True:
			subject_day_index = random.randint(*indexes_of_available_days_interval)
			subject_time_index = random.randint(0, counter_classes_per_day - 1)
			if schedule[subject_day_index][subject_time_index] == None:
				schedule[subject_day_index][subject_time_index] = subject
				remaining_sheduling -= 1
				break

show_schedule(schedule)

