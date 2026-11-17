mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print(mission_route[0])
print(mission_route[5])
len(mission_route)
print("Total destinations:", (len(mission_route)))

for i in range(len(mission_route)):
    destination = mission_route[i]
    print(destination)

if "Europa" in mission_route:
    print("Europa is part of the mission route.")
else:
    print("Europa is not part of the mission route.")

search_destination = input("Enter a destination: ")
if search_destination in mission_route:
    print(search_destination, "is part of the mission route.")
    position = mission_route.index(search_destination)
    print("Stops away from the start:", position)
    stops_away_from_end = (len(mission_route) - position - 1)
    print("Stops away from the end:", stops_away_from_end)
    if stops_away_from_end > 0:
        print("Next stop:", mission_route[position + 1])
    else:
        print("This is the final destination.")
else:
    print(search_destination, "is not part of the mission route.")