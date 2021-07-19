import requests
from datetime import date
import os
from sshelper import SSHelper
import ast

DEBUG = ast.literal_eval(os.environ['DEBUG'])

countries = SSHelper(os.environ['API_KEY']).getCountries(DEBUG)
