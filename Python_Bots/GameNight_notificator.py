# Calculates frequency table of players available for a certain day and sends them a personalized message.
# Send a message to those players unable to attend the first game and calculate availabiity for alternative day. 


gamers = []

def add_gamer(gamer={}, gamers_list=[]):
	try:
		if "name" in gamer.keys() and "availability" in gamer.keys():
			gamers_list.append(gamer)
	except:
		print("Incorrect dictionary provided")

add_gamer({"name":"Kimberly Warner", "availability": ["Mondays", "Tuesdays", "Fridays"]}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)


def build_freq_table():
	week = {"Monday":0,"Tuesday":0, "Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0, "Sunday":0}
	return week


def calculate_availability(gamers_list, freq_table):
	week_days = freq_table()
	for gamer in gamers_list:
		list_of_days = gamer.get("availability", 0)
		for i in list_of_days:
			for day in week_days:
				if i == day:
					week_days[day] += 1
	return week_days


calculate_availability = calculate_availability(gamers, build_freq_table)

def find_best_night(calculate_availability):
	game_night = max(calculate_availability, key=calculate_availability.get)
	return game_night


best_night = find_best_night(calculate_availability)
print(best_night)


def available_on_night(gamers_list, best_night):
	ppl = []
	for gamer in gamers_list:
		a = gamer.get('availability', 0)
		for i in a:
			if best_night in i:
				ppl.append(gamer.get('name'))

	return ppl


available_people = available_on_night(gamers, best_night)
print(available_people)

def send_email(available_people, best_night, game):
	for name in available_people:
		print("Hello {}! On {}, there is an {} game, hope you can drop by!".format(name, best_night, game))



send_email(available_people, best_night, "Abruptly Goblins")
print(send_email)


second_night = build_freq_table()


unavailable = []
for gamer in gamers:
	a = gamer.get("name")
	if a not in available_people:
		unavailable.append(gamer)


def calculate_availability_2(unavailable, second_night):
	days = second_night
	for gamer in unavailable:
		a = gamer.get("availability", 0)
		for i in a:
			for j in days:
				if i == j:
					days[j] += 1
	return days

second_game_night = calculate_availability_2(unavailable, second_night)



def find_best_night_2(second_game_night):
	day = max(second_game_night, key=second_game_night.get)
	return day

find_best_night_2 = find_best_night_2(second_game_night)


def second_email(unavailable, find_best_night_2, game):
	day = find_best_night_2
	for gamer in unavailable:
		gamer = gamer.get("name")
		print("Hello {} please come on {} for a second round of lulz in {}".format(gamer, day, game))


second_email(unavailable, find_best_night_2, "Abruptly Goblins")
