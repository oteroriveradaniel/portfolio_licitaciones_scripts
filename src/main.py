from dotenv import load_dotenv, find_dotenv
from connection import get_connection, load_data
from utils import read_csv
from pathlib import Path

if __name__ == "__main__":
    load_dotenv(find_dotenv())

    connection = get_connection()

    try:
        collections = [
            {"collection": "contratos", "filename": "ckan_contratos"}, 
            {"collection": "adjudicatarios", "filename": "ckan_contratos_adjudicatario"}, 
            {"collection": "lotes", "filename": "ckan_contratos_lot"}, 
            {"collection": "organizaciones", "filename": "ckan_contratos_organizacion"}, 
        ]
        for collection in collections:
            path = Path(__file__).parent.resolve() / "CSV" / f"{collection['filename']}.csv"
            data = read_csv(path)
            load_data(data, connection, collection["collection"])
    except Exception as e:
        print(e)

    connection.close()