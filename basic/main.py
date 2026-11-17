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

