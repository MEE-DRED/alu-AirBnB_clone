#!/usr/bin/python3
"""
Test Module for BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Testing BaseModel Class
    """
    def setUp(self):
        """
        Set up for testing
        """
        self.base = BaseModel()

    def tearDown(self):
        """
        Tear down for testing
        """
        del self.base

    def test_init(self):
        """
        Test for init method
        """
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_uuid(self):
        """
        Test for uuid
        """
        self.assertTrue(hasattr(self.base, "id"))

    def test_created_at(self):
        """
        Test for created_at
        """
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(isinstance(self.base.created_at, datetime))

    def test_updated_at(self):
        """
        Test for updated_at
        """
        self.assertTrue(hasattr(self.base, "updated_at"))
        self.assertTrue(isinstance(self.base.updated_at, datetime))

    def test_save(self):
        """
        Test for save method
        """
        self.base.save()
        self.assertTrue(isinstance(self.base.updated_at, datetime))

    def test_to_dict(self):
        """
        Test for to_dict method
        """
        self.assertTrue(hasattr(self.base, "to_dict"))
        self.assertTrue(type(self.base.to_dict()) is dict)

    def test_str(self):
        """
        Test for __str__ method
        """
        self.assertTrue(hasattr(self.base, "__str__"))
        self.assertTrue(type(self.base.__str__()) is str)


if __name__ == "__main__":
    unittest.main()