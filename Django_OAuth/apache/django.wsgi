import os
import sys

home_path = '/home/celestia/Dropbox/GitHub/Django-OAuth/Django_OAuth'
if home_path not in sys.path:
    sys.path.insert(0, home_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Django_OAuth.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()