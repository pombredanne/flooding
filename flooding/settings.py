# Base Django settings, suitable for production.
# Imported (and partly overridden) by developmentsettings.py which also
# imports localsettings.py (which isn't stored in svn).  Buildout takes care
# of using the correct one.
# So: "DEBUG = TRUE" goes into developmentsettings.py and per-developer
# database ports go into localsettings.py.  May your hear turn purple if you
# ever put personal settings into this file or into developmentsettings.py!

import os
import tempfile

# SETTINGS_DIR allows media paths and so to be relative to this settings file
# instead of hardcoded to c:\only\on\my\computer.
SETTINGS_DIR = os.path.dirname(os.path.realpath(__file__))

# BUILDOUT_DIR is for access to the "surrounding" buildout, for instance for
# BUILDOUT_DIR/var/media files to give django-staticfiles a proper place
# to place all collected static files.
BUILDOUT_DIR = os.path.abspath(os.path.join(SETTINGS_DIR, '..'))

# Triple blast.  Needed to get matplotlib from barfing on the server: it needs
# to be able to write to some directory.
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.gettempdir()

# Production, so DEBUG is False. developmentsettings.py sets it to True.
DEBUG = False
# Show template debug information for faulty templates.  Only used when DEBUG
# is set to True.
TEMPLATE_DEBUG = True

# ADMINS get internal error mails, MANAGERS get 404 mails.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'
# ^^^ 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = os.path.join(BUILDOUT_DIR, 'var', 'sqlite', 'test.db')
DATABASE_NAME = 'flooding20_new'
DATABASE_USER = 'postgres'
DATABASE_PASSWORD = 'lizard123'
#DATABASE_HOST = 'nens-webontw-01'
DATABASE_HOST = '194.105.129.235'
DATABASE_PORT = '' # empty string for default.

# Almost always set to 1.  Django allows multiple sites in one database.
SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems.  If running in a Windows
# environment this must be set to the same as your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl-NL'
# For at-runtime language switching.  Note: they're shown in reverse order in
# the interface!
LANGUAGES = (
    ('en', 'English'),
    ('nl', 'Nederlands'),
)
# If you set this to False, Django will make some optimizations so as not to
# load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds user-uploaded media.
MEDIA_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'media')
# Absolute path to the directory where django-staticfiles'
# "bin/django build_static" places all collected static files from all
# applications' /media directory.
STATIC_ROOT = os.path.join(BUILDOUT_DIR, 'var', 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
MEDIA_URL = '/media/'
# URL for the per-application /media static files collected by
# django-staticfiles.  Use it in templates like
# "{{ MEDIA_URL }}mypackage/my.css".
STATIC_URL = '/static_media/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.  Uses STATIC_URL as django-staticfiles nicely collects
# admin's static media into STATIC_ROOT/admin.
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

# django-staticfiles needs an extra context processor to allow you to use {{
# STATIC_URL }}myapp/my.css in your templates.
TEMPLATE_CONTEXT_PROCESSORS = (
    # Default items.
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    # Extra for django-staticfiles.
    'staticfiles.context_processors.static_url',
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b8cdceb3-4879-4dcc-96ef-5030c2493fa0'

ROOT_URLCONF = 'flooding.urls'

CACHE_BACKEND = 'locmem:///'
# Note: for development only, check django website for caching solutions for
# production environments
# ^^^ TODO

INSTALLED_APPS = (
    'flooding',
    'lizard_flooding',
    'lizard_presentation',
    'lizard_visualization',
    'lizard_flooding.tools.importtool',
    'lizard_flooding.tools.exporttool',
    'lizard_flooding.tools.approvaltool',
    'lizard_base',
    'staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    # 'django.contrib.gis.db',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
)


EXTERNAL_MOUNTED_DIR = os.path.join(BUILDOUT_DIR, 'var', 'external_data')