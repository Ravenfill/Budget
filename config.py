# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'postgresql://testing:test123@16.170.36.92:5432/testing'
#DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

BABEL_DEFAULT_LOCALE = 'en'

LANGUAGES = ['ru', 'en', 'uk', 'de']

# Session
#USE_SESSION_FOR_NEXT = True

# Coockies setup
REMEMBER_COOKIE_NAME = 'budget'
REMEMBER_COOKIE_SECURE = False