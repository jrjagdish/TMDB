import argparse

#get categoery 
def get_category_key():
        parser = argparse.ArgumentParser(description="add categories")
        parser.add_argument("category",choices=["playing","popular","top","upcoming"],help="add proper category")
        
        args = parser.parse_args()
        category=args.category

        return category

