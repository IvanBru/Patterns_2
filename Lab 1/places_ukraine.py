class PlacesUkraine:
    def __init__(self, places):
        self.places = places

    def get_places_by_preference(self):
        return TouristPreferenceIterator(self.places)

    def get_places_by_navigator(self):
        return NavigatorRecommendationIterator(self.places)

    def get_places_by_local_guide(self):
        return LocalGuideIterator(self.places)