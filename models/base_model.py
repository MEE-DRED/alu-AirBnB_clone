import uuid
from datetime import datetime

"""

"""
class BaseModel():
    """
    Model that defines all common attributes for other classes
    """
    def __init__(self, id, created_at, updated_at):
        """
        Initialize the BaseModel class
        """
        self.id = str(uuid.uuid4())
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
        