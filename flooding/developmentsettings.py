from flooding.settings import *

DEBUG = True

DATABASE_ENGINE = 'sqlite3'
# ^^^ 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(BUILDOUT_DIR, 'var', 'sqlite', 'test.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = '' # empty string for localhost.
DATABASE_PORT = '' # empty string for default.


try:
    from flooding.localsettings import *
    # For local dev overrides.
except ImportError:
    pass