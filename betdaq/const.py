# const.py
# James Mithen
# jamesmithen@gmail.com

"""
Some constants that are useful globally.
"""

import suds
import sys
import os

# version number for this software
VERSION = '0.1'

# print logging information to stdout while running code?  In the
# library itself, a logging message is printed each time an API
# function is called.
LOGGING = True

# maximum number of prices to get from API
NUMPRICES = 5

# send as 'user-agent' header for all SOAP requests
USERAGENT = 'pybetman/{0} python/{1} suds/{2}'.\
            format(VERSION, sys.version.split()[0], suds.__version__)

# path to local copy of WSDL file
_mypath = os.path.dirname(os.path.join(os.getcwd(), __file__))
_wsdlpath = os.path.join(_mypath, 'wsdl', 'API.wsdl')
WSDLLOCAL = 'file://{0}'.format(_wsdlpath)

# BDAQ API version sent in SOAP headers
BDAQAPIVERSION = '2'

# BDAQ username and password go here; alternatively, we can call
# betdaq.set_user.
BDAQUSER = 'username'
BDAQPASS = 'password'
