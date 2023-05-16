class TouristPreferenceIterator:
    def __init__(self, places):
        self.places = places
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.places):
            place = self.places[self.current_index]
            self.current_index += 1
            return place
        else:
            raise StopIteration()


class NavigatorRecommendationIterator:
    def __init__(self, places):
        self.places = places
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.places):
            place = self.places[self.current_index]
            self.current_index += 1
            return place
        else:
            raise StopIteration()


class LocalGuideIterator:
    def __init__(self, places):
        self.places = places
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.places):
            place = self.places[self.current_index]
            self.current_index += 1
            return place
        else:
            raise StopIteration()