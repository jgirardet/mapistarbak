# -*- coding: utf-8 -*-
import os
from config.get_env import env

# from .base import *

try:
    os.environ['PYTEST_VER']  #given by pytest-env-info
except KeyError:
    if env['DEBUG'] == True:
        print("\n ## Mapistar LOCAL config loaded ###  \n")
        from .local import *
    else:
        print("\n ## Mapistar PRODUCTION config loaded ###  \n")
        from .prod import *
else:
    print("\n ## Mapistar TESTING config loaded ###  \n")
    from .testing import *

if env['DEBUG']:
    print("""
##################################
#     DEBUG MODE IS ACTIVE       #
##################################
""")
