__author__ = 'teo'

from pymongo import MongoClient
from juniper import settings

def check_passphrase(provided):
    try:
        mc = MongoClient(settings.MONGO_DB_IP, settings.MONGO_DB_PORT)
        if settings.MONGO_DB_AUTH == True:
            mc[settings.MONGO_DB_NAME].authenticate(settings.MONGO_DB_USER, settings.MONGO_DB_PWD)
        db = mc[settings.MONGO_DB_NAME]
        settings_col = db.settings
        obj_from_db = settings_col.find_one({'key':'passphrase'})
        if provided == obj_from_db['value']:
            return True
        else:
            return False
    except Exception as ex:
        print (ex.message)
    finally:
        mc.close()

def change_passphrase(provided):
    try:
        mc = MongoClient(settings.MONGO_DB_IP, settings.MONGO_DB_PORT)
        db = mc.linksdb
        settings_col = db.settings
        obj_from_db = settings_col.find_one({'key':'passphrase'})
        obj_from_db['value'] = provided
        settings_col.save(obj_from_db)
    except Exception as ex:
        print (ex.message)
    finally:
        mc.close()


if __name__ == '__main__':
    #check_passphrase('alfa')

    change_passphrase('gamma')
    check_passphrase('beta')