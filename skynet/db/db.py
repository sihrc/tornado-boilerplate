"""
SkyNet User Database
"""
import motor

from skynet.config import MONGODB

client=motor.MotorClient(MONGODB)
mongodb = client.skynet
