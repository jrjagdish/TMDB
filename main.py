from getkey import get_category_key
from request_api import get_by_key
from display_movie import display_data

def main():
    category=get_category_key()
    store = get_by_key(category)
    display_data(store)

if __name__ == "__main__":
    main()    




