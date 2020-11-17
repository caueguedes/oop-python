class Database:
    # the database implementation
    pass


database = None

def initialize_database():
    global database
    database = Database()

# From ecommerce.database import database
