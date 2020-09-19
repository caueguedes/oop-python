""" Project Structure
parent_directory/
    main.py
    ecommerce/
        __init__.py
        database.py
        products.py
        payments/
            __init__.py
            square.py
            stripe.py
            paypal.py
        /contact
            email/
                send_mail
"""

# From inside products
from .database import Database

# From Paypal inside ecommerce.payments
from ..database import Database
from ..contact.email import send_mail

# Add "from .database import db" to __init__.py
# Them you can import files like:
from ecommerce import db
