from django_mongo.settings import DATABASES
import pymongo


CLUSTER = DATABASES['default']['CLIENT']['host']

client = pymongo.MongoClient(CLUSTER)

db = client[DATABASES['default']['NAME']]