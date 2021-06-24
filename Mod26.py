#Lukas Robin
#23.06.2021
#Module 2.6 Assignment
from Vacation import Vacation

def main()->object:
	gender = input("What is your sex? (Male/Female) ")
	timeOfYear = input("Are you going in Winter, Spring, Summer, or Autumn? ")
	location = input("Are you going to Miami, New York, Los Angeles, or Paris? ")
	vacation = Vacation(gender, timeOfYear, location)
	return vacation
def vacation()->str:
	location = ["miami", "new york", "los angeles","paris"]
	vacation = main()
	vacationtime = vacation.time
	if vacation.time.lower() == "spring":
		if vacation.place.lower() == location[0]:
			if vacation.gender.lower() == "male":
				return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 20's. during " + vacation.time + "."
			elif vacation.gender.lower() == "female":
				return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 20's. during " + vacation.time + "."
			else:
				return "Error"
				exit()
			if vacation.place.lower() == location[1]:
				if vacation.gender.lower() == "male":
					return "Wear light jeans, a t-shirt and maybe closed shoes because the weather will most likely around 10º during"  + vacation.time + "."
				elif vacation.gender.lower() == "female":
					return "Wear light jeans, a t-shirt and maybe closed shoes because the weather will most likely around 10º during" + vacation.time + "."
				else:
					return "Error"
					exit()
			if vacation.place.lower() == location[2]:
				if vacation.gender.lower() == "male":
					return "Wear light jeans or shorts, a t-shirt and maybe closed shoes because the weather will most likely around 15º during"  + vacation.time + "."
				elif vacation.gender.lower() == "female":
					return "Wear light jeans or shorts, a tank top and maybe closed shoes because the weather will most likely around 15º during"  + vacation.time + "."
				else:
					return "Error"
					exit()
				if vacation.place.lower() == location[3]:
					if vacation.gender.lower() == "male":
						return "Wear hoodie and jeans, the weather is likely to be in the mid teens during "+ vacation.time + "."					
					elif vacation.gender.lower() == "female":
						return "Wear hoodie and jeans, the weather is likely to be in the mid teens.  during "+ vacation.time + "."
					else:
						return "Error"
						exit()
	if vacation.time.lower() == "summer":
		if vacation.place.lower() == location[0]:
			if vacation.gender.lower() == "male":
				return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 30's in Miami  during "+ vacation.time + "."
			elif vacation.gender.lower() == "female":
				return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 30's in Miami  during "+ vacation.time + "."
			else:
				return "Error"
				exit()
			if vacation.place.lower() == location[1]:
				if vacation.gender.lower() == "male":
					return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 20's in New York  during "+ vacation.time + "."
				elif vacation.gender.lower() == "female":
					return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 20's in New York  during "+ vacation.time + "."
				else:
					return "Error"
					exit()
			if vacation.place.lower() == location[2]:
				if vacation.gender.lower() == "male":
					return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 20's in Los Angeles  during "+ vacation.time + "."
				elif vacation.gender.lower() == "female":
					return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 20's in Los Angeles  during "+ vacation.time + "."
				else:
					return "Error"
					exit()
				if vacation.place.lower() == location[3]:
					if vacation.gender.lower() == "male":
						return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 20's in Paris.  during "+ vacation.time + "."
					elif vacation.gender.lower() == "female":
						return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 20's in Paris  during "+ vacation.time + "."
					else:
						return "Error"
						exit()
	if (vacation.time.lower() == "autumn") or (vacation.time.lower() == "fall"):
		if vacation.place.lower() == location[0]:
			if vacation.gender.lower() == "male":
				return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 20's  during "+ vacation.time + "."
			elif vacation.gender.lower() == "female":
				return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 20's  during "+ vacation.time + "."
			else:
				return "Error"
				exit()
			if vacation.place.lower() == location[1]:
				if vacation.gender.lower() == "male":
					return "Wear light jeans, a t-shirt and maybe closed shoes because the weather will most likely around 10º.  during "+ vacation.time + "."
				elif vacation.gender.lower() == "female":
					return "Wear light jeans, a t-shirt and maybe closed shoes because the weather will most likely around 10º  during "+ vacation.time + "."
				else:
					return "Error"
					exit()
			if vacation.place.lower() == location[2]:
				if vacation.gender.lower() == "male":
					return "Wear light jeans or shorts, a t-shirt and maybe closed shoes because the weather will most likely around 15º.  during "+ vacation.time + "."
				elif vacation.gender.lower() == "female":
					return "Wear light jeans or shorts, a tank top and maybe closed shoes because the weather will most likely around 15º  during "+ vacation.time + "."
				else:
					return "Error"
					exit()
				if vacation.place.lower() == location[3]:
					if vacation.gender.lower() == "male":
						return "Wear hoodie and jeans, the weather is likely to be in the mid teens during "+ vacation.time + "."					
					elif vacation.gender.lower() == "female":
						return "Wear hoodie and jeans, the weather is likely to be in the mid teens  during "+ vacation.time + "."
					else:
						return "Error"
						exit()
	if vacation.time.lower() == "winter":
		if vacation.place.lower() == location[0]:
			if vacation.gender.lower() == "male":
				return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 30's in Miami  during "+ vacation.time + "."
			elif vacation.gender.lower() == "female":
				return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 30's in Miami  during "+ vacation.time + "."
			else:
				return "Error"
				exit()
			if vacation.place.lower() == location[1]:
				if vacation.gender.lower() == "male":
					return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 20's in New York  during "+ vacation.time + "."
				elif vacation.gender.lower() == "female":
					return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 20's in New York  during "+ vacation.time + "."
				else:
					return "Error"
					exit()
			if vacation.place.lower() == location[2]:
				if vacation.gender.lower() == "male":
					return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 20's in Los Angeles  during "+ vacation.time + "."
				elif vacation.gender.lower() == "female":
					return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 20's in Los Angeles during    "
				else:
					return "Error"
					exit()
				if vacation.place.lower() == location[3]:
					if vacation.gender.lower() == "male":
						return "Wear shorts, a light t-shirt and maybe open shoes because the weather will most likely be in the mid 20's in Paris during"  + vacation.time + "."
					elif vacation.gender.lower() == "female":
						return "Wear a summer dress and flip flops, or perhaps a tank top with shorts, the weather is likely to be in the mid 20's in Paris during"  + vacation.time + "."
					else:
						return "Error"
						exit()
print(vacation())