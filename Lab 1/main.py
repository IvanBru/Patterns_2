from places_ukraine import PlacesUkraine
from iterators import *

places_ukraine = ["Kharkiv", "Lviv", "Odesa", "Dnipro", "Kyiv"]
tourist_places = PlacesUkraine(places_ukraine)

tourist_preference_iterator = tourist_places.get_places_by_preference()
print("Tourist places based on the tourist's preference:")
for place in tourist_preference_iterator:
    print(place)

navigator_recommendation_iterator = tourist_places.get_places_by_navigator()
print("Tourist places based on navigator recommendations:")
for place in navigator_recommendation_iterator:
    print(place)

local_guide_iterator = tourist_places.get_places_by_local_guide()
print("Tourist places based on a local guide:")
for place in local_guide_iterator:
    print(place)