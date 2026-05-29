# Simple Travel Planner Program

class TravelPlanner:
    def __init__(self):
        self.places = {
            "Goa": ["Beach", 15000, ["Seafood", "Goan Curry"], 3],
            "Manali": ["Hill Station", 12000, ["Momos", "Thukpa"], 4],
            "Jaipur": ["Historical", 10000, ["Dal Baati", "Kachori"], 2]
        }

    def recommend_place(self, budget, interest):
        matched_places = []

        for place in self.places:
            place_type = self.places[place][0]
            place_cost = self.places[place][1]

            if place_cost <= budget and place_type.lower() == interest.lower():
                matched_places.append(place)

        return matched_places

    def show_details(self, place):
        if place not in self.places:
            print("Place not found")
            return

        details = self.places[place]

        print("\nPlace:", place)
        print("Type:", details[0])
        print("Estimated Cost: Rs.", details[1])
        print("Recommended Food:", ", ".join(details[2]))
        print("Suggested Days:", details[3])


planner = TravelPlanner()

budget = int(input("Enter your budget: "))
interest = input("Enter your interest (Beach/Hill Station/Historical): ")

places = planner.recommend_place(budget, interest)

print("\nRecommended Places:")
print(places)

if len(places) > 0:
    planner.show_details(places[0])
else:
    print("No place found for your budget and interest.")
