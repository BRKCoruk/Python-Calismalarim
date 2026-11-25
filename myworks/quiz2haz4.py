def buy_ticket(movie_dict, title, quantity):
    if title not in movie_dict:
        print("Movie not found.")
        return False
    else:
        price, seats = movie_dict[title]
        if seats < quantity:
            print("Not enough seats!")
            return False
        else:
            movie_dict[title] = (price, seats - quantity)
            total_price = price * quantity
            print(f"Total price: {total_price} TL")
            return True

movies = {
    "Inception": (150.0, 5),
    "Interstellar": (180.0, 0),
    "Dune": (160.0, 12)
}

buy_ticket(movies, "Avatar", 2)
buy_ticket(movies, "Interstellar", 1)
buy_ticket(movies, "Inception", 3)
