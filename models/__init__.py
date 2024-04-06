#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv

# Determine the storage type
storage_t = getenv("HBNB_TYPE_STORAGE")

# Import the appropriate storage class based on the storage type
if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()

# Import all models
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

# Optionally, you can also import the base model if you have one
# from models.base_model import BaseModel
