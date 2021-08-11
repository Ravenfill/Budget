# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR + '/app/database/', 'app.db')
#SQLALCHEMY_DATABASE_URI = 'postgresql://admin:mysecretpassword@172.21.0.2:5432/postgres'
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
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
CSRF_SESSION_KEY = "\xed\xc2\xc2\x8bC9\x93\x9e)}\xac\x0f;\xc8\xa9a\x8e\x03\xdbr\xbf\x0blQ\x7f\xb8f\x08\xb3U\n\xc8"

# Secret key for signing cookies
SECRET_KEY = "\xed\xc2\xc2\x8bC9\x93\x9e)}\xac\x0f;\xc8\xa9a\x8e\x03\xdbr\xbf\x0blQ\x7f\xb8f\x08\xb3U\n\xc8"
