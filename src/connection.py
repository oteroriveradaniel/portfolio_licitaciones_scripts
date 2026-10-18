from pymongo import MongoClient
import os

def get_connection():
   CONNECTION_STRING = os.getenv("MONGODB_URI")
   client = MongoClient(CONNECTION_STRING)
   return client

def load_data(data, connection, collection):
    try: 
        database = connection.get_database(os.getenv("MONGODB_DATABASE"))
        db_collection = database.get_collection(collection)

        num_items = db_collection.estimated_document_count()

        print("Cargando datos en", collection, "...")

        if num_items > 0:
            print("Omitida", "/", num_items, "documentos.")
        else:
            items = db_collection.insert_many(data)
            print(len(items.inserted_ids), "nuevos documentos.")

    except Exception as e:
        raise Exception(e)