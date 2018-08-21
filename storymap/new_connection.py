import sys
import os
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

# get settings module
settings = sys.modules[os.environ['FLASK_SETTINGS_MODULE']]

if settings.TEST_MODE: 
	# something
else:
	# connect to sql database
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'