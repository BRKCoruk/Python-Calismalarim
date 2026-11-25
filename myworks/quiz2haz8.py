def assign_seat(seats_dict, row, col, passenger):
    if not (1 <= row <= 10) or col not in ("A", "B", "C", "D"):
        print("Invalid seat position!")
        return False
    elif (row, col) in seats_dict:
        print("Seat is already occupied!")
        return False
    else:
        seats_dict[(row, col)] = passenger
        print(f"Seat {row},{col} reserved for {passenger}.")
        return True

def get_priority_passengers(seats_dict, limit=3):
    all_seats = []

    for seat, passenger in seats_dict.items():
        all_seats.append((seat, passenger))

    ordered = sorted(all_seats)
    top_seats = ordered[:limit]

    name_list = []
    for seat, passenger in top_seats:
        name_list.append(passenger)
       
    return name_list

seat_map = {
    (1, "A"): "Zeynep",
    (1, "B"): "Kerem",
    (3, "C"): "Mert",
    (2, "A"): "Selin"
}

user_input = input("Enter a passenger name (or 'done' to finish): ")

while user_input != "done":
    row_input = int(input("Enter row: "))
    col_input = input("Enter column: ").upper()
    assign_seat(seat_map, row_input, col_input, user_input)
    user_input = input("Enter a passenger name (or 'done' to finish): ")

print(get_priority_passengers(seat_map,5))

