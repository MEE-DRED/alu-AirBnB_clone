from uuid import uuid4
from datetime import datetime

"""
Base Model Class
"""
class BaseModel:
    """
    Model that defines all common attributes for other objects

    id: (str) unique id of each object
    created_at: (datetime) time of creation
    updated_at: (datetime) time of last update
    
    updated_at and created_at are automatically set to the current date
    and time when an instance is created or updated

    updated time will be updated whenever an instance is changed

    """

    def __init__(self):
        """
        Initialize the BaseModel class
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
        
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        
        """
        class_name = self.__class__.__name__
        serial_dict = self.__dict__.copy()
        serial_dict["created_at"] = self.created_at.isoformat()
        serial_dict["updated_at"] = self.updated_at.isoformat()

        serial_dict["__class__"] = class_name
        return serial_dict
        