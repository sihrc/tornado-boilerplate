"""
SkyNet User Database
"""
import motor

from skynet.config import MONGODB

mongodb = motor.MotorClient(MONGODB).skynet
