#
# =================================
# Daily Challenge: Air Management
# =================================
# Your goal is to build an airplanes traffic management system.

from datetime import date, datetime


class Airline:
    def __init__(self, id_code, name):
        self.id = id_code
        self.name = name
        self.planes = []


class Airplane:
    def __init__(self, id_num, current_location, company):
        self.id = id_num
        self.current_location = current_location
        self.company = company
        self.next_flights = []

    def fly(self, destination):
        """Executes the next scheduled flight if the destination matches."""
        for flight in self.next_flights:
            if flight.destination == destination:
                flight.take_off()
                flight.land()
                self.next_flights.remove(flight)
                return True
        return False

    def location_on_date(self, target_date):
        """Predicts where the plane will be on a specific date."""
        current_loc = self.current_location
        for flight in self.next_flights:
            if flight.date <= target_date:
                current_loc = flight.destination
            else:
                break
        return current_loc

    def available_on_date(self, target_date, location):
        """Checks if the plane is at the location and has no flight that day."""
        for flight in self.next_flights:
            if flight.date == target_date:
                return False

        return self.location_on_date(target_date) == location


class Flight:
    def __init__(self, date_obj, origin, destination, plane):
        self.date = date_obj
        self.origin = origin
        self.destination = destination
        self.plane = plane
        self.id = f"{destination.city}-{plane.company.id}-{date_obj}"

    def take_off(self):
        print(f"Flight {self.id} is taking off from {self.origin.city}!")
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)

    def land(self):
        print(f"Flight {self.id} has landed in {self.destination.city}.")
        self.plane.current_location = self.destination
        self.destination.planes.append(self.plane)


class Airport:
    def __init__(self, city_code):
        self.city = city_code
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination_airport, flight_date):
        """Finds an available plane and schedules a flight."""
        for plane in self.planes:
            if plane.available_on_date(flight_date, self):
                new_flight = Flight(flight_date, self,
                                    destination_airport, plane)

                plane.next_flights.append(new_flight)
                plane.next_flights.sort(key=lambda x: x.date)

                self.scheduled_departures.append(new_flight)
                destination_airport.scheduled_arrivals.append(new_flight)
                return new_flight
        return None

    def info(self, start_date, end_date):
        print(f"--- Flights from {self.city} ({start_date} to {end_date}) ---")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(
                    f"Flight: {flight.id} | To: {flight.destination.city} | Plane: {flight.plane.id}")
