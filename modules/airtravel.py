"""Model for aircraff flights"""
from pprint import pprint as pp

class Flight:
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")      

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating =  [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def route(self):
        return self._number[2:]

    def aircraft(self):
        return self._aircraft

    def allocate_seat(self, seat, passenger):
        rows, seat_letters = self._aircraft.seating_plan()
        letter  = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid set row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")    

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")
                
        self._seating[row][letter] = passenger


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows+1), 
                "ABCDEFGHJK"[:self._num_seats_per_row])


if __name__ == "__main__":
    f = Flight("SN1234", Aircraft("A1", "AIRBUS-121", 10, 6))
    print(f.number())
    print(f.airline())
    print(f.route())
    print(f.aircraft().seating_plan())
    f.allocate_seat("1B", "Nicola Tesla")
    f.allocate_seat("2A", "Other guy")
    pp(f._seating)

# from airtravel import Flight