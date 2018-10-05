data = input()
city_capacity = {}

while data != "ready":
    list_data = data.split(":")
    city = list_data[0]
    list_transport = list_data[1].split(",")

    if city not in city_capacity:
        city_capacity[city] = {}

    for item in list_transport:
        transport = item.split("-")[0]
        capacity = item.split("-")[1]
        city_capacity[city][transport] = capacity
    data = input()

data = input()

while data != "travel time!":
    city = data.split()[0]
    people = data.split()[1]

    result = 0
    for item in city_capacity[city]:
        result += int(city_capacity[city][item])

    people = int(people)
    if result >= int(people):
        print(f"{city} -> all {people} accommodated")
    else:
        print(f"{city} -> all except {people - result} accommodated")

    data = input()



'''Write a program, which categorizes information about a travel company.
Companies have various vehicles planned for different cities. Every city has prepared several types of vehicles. Each vehicle type has a different capacity.
Until you receive the command “ready”, you will receive all the cities the company offers holiday packages for, and their respective vehicle types + capacities in the format:
•	“{city}:{type}-{capacity},{type}-{capacity}…”
An example city with its transportation options would look like this:
•	“Athens:bus-40,airplane-300,train-150”
If a city is entered a second time, add all transport which hasn’t already been added and replace existing transports’ capacities with the new ones.
After the “ready” command, you will start receiving groups for various cities in the format: “{city} {peopleCount}” until you receive “travel time!”.
After that, calculate whether the group will have enough seats to accommodate the passengers and print the status per these conditions:
If the group’s size is smaller than or equal to the combines seats in all the vehicles, print:
•	 “{city} -> all {peopleCount} accommodated”
If the group’s size is larger than the combines seats in all the vehicles, print:
•	“{city} -> all except {peopleCount - transportCapacities} accommodated”
Constraints
•	There will be no redundant whitespaces anywhere in the input.
•	The input will always be in the format specified.
•	The group cities will always be existing cities.
•	The group sizes will always be positive.
Examples
Input
	
Athens:bus-40,airplane-300,train-150
Athens:minibus-8,airplane-350
Warsaw:bus-30,train-150,airplane-120
ready
Athens 400
Warsaw 500
travel time!	

Output

Athens -> all 400 accommodated
Warsaw -> all except 200 accommodated

Input	
Sofia:bus-30,airplane-150,train-25
Istanbul:minibus-6,train-80
Sofia:bus-45
Sofia:bus-50
Berlin:airplane-120
ready
Berlin 115
Istanbul 200
Sofia 200
travel time!	

Output
Berlin -> all 115 accommodated
Istanbul -> all except 114 accommodated
Sofia -> all 200 accommodated
'''