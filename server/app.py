#!/usr/bin/env python3
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Create a manager instance for handling commands
manager = Manager(app)

# Add the 'db' command to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # Run the manager instead of the app
    manager.run()
