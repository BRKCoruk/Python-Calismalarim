def borrow_book(lib_dict, book_title):
    if book_title not in lib_dict:
        print("Error: Book not found in catalog.")
        return False
    else:
        author, copies = lib_dict[book_title]
        if copies <= 0:
            print(f"Sorry, '{book_title}' is currently out of stock.")
            return False
        else:
            lib_dict[book_title] = (author, copies - 1)
            print(f"Successfully borrowed '{book_title}' by {author}")
            return True

def inventory_summary(lib_dict):
    total_copies = 0
    out_of_stock_list = []

    for books, values in lib_dict.items():
        if values[1] <= 0:
            out_of_stock_list.append(books)
        else:
            total_copies = total_copies + values[1]
    return total_copies, out_of_stock_list

borrowed_history = []
library = {
    "Clean Code": ("Robert C. Martin", 2),
    "Python Crash Course": ("Eric Matthes", 1),
    "The Pragmatic Programmer": ("Andrew Hunt", 0),
}

user_input = input("Enter book title to borrow (or 'done' to finish): ")

while user_input != "done":
    if borrow_book(library,user_input):
        borrowed_history.append(user_input)
    user_input = input("Enter book title to borrow (or 'done' to finish): ")

remaining_copies, out_of_stock = inventory_summary(library)

print("\n--- LIBRARY REPORT ---")
print(f"Books Borrowed ({len(borrowed_history)}): {borrowed_history})")
print(f"Total Remaining Copies: {remaining_copies}")

if len(out_of_stock) == 0:
    print("Out of Stock Books: None")
else:
    print(f"Out of Stock Books: {out_of_stock}")
