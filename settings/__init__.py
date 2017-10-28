# -*- coding: utf-8 -*-
from .base import *  # noqa
try:
    from .local import *  # noqa
except ImportError:
    print('User, fill in local.py, please!'
          '\nUse command: "cp settings/local.py.default settings/local.py"'
          '\nSet valid database connection data and other parameters in local.py')
    raise
