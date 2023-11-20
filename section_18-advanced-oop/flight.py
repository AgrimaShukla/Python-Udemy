from typing import List
class Segment:
    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination

class Flight:
    def __init__(self, segments: List[Segment]):
        self.segments = segments

    def __repr__(self):
        stops = [self.segments[0].departure, self.segments[0].destination]
        for seg in self.segments[1:]:
            stops.append(seg.destination)

        return '->'.join(stops)
    
    @property
    def departure_point(self)->str:
        return self.segments[0].departure
    
    @departure_point.setter
    def departure_point(self, val):
        dest = self.segments[0].destination
        self.segments[0] = Segment(departure=val, destination=dest)

seg1_obj = Segment('GLA', 'LHR')
seg2_obj = Segment('lhr', 'mum')
seg3_obj = Segment('mum', 'udai')

flight = Flight([seg1_obj, seg2_obj, seg3_obj])
print(flight)

flight.departure_point = 'EDI'
print(flight)