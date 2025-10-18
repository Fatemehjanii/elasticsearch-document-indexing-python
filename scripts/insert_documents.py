from elasticsearch import Elasticsearch ,helpers
import random



client = Elasticsearch("http://localhost:9200")          #connect local elastic or docker
print(client.info())                         #check connection
index_name = "users"
#client.indices.create(index=index_name)/create empty index


if not client.indices.exists(index=index_name):
    mapping = {
        "mappings": {
            "properties": {
                "name": {"type": "keyword"},
                "username": {"type": "keyword"},
                "email": {"type": "keyword"},
                "password": {"type": "keyword"},
            }
        }
    }
    client.indices.create(index=index_name, body=mapping)
    print(f"Index '{index_name}' created successfully.")
else:
    print(f"Index '{index_name}' already exists.")

document = []
names = ["Ali", "Ahmad", "Mehdi", "Fatemeh", "Sara", "Niloofar", "Hassan", "Reza"]

for i in range (1,101):
    doc = {
        "_index": index_name,
        "_source": {
            "name": random.choice(names),
            "username": f"user{i}",
            "email": f"user{i}@example.com",
            "password": f"pass{i:03d}"
        }
    }
    document.append(doc)


helpers.bulk(client, document)
print(f"Successfully inserted {len(document)} documents into '{index_name}' index.")


count = client.count(index=index_name)["count"]
print(f"Total documents in '{index_name}': {count}")