"""
grey User Database
"""
import motor

from grey.config import MONGODB

client = motor.MotorClient(MONGODB)
mongodb = client.grey
