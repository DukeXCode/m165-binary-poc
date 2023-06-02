import pymongo
import gridfs
import connection

client = pymongo.MongoClient(connection.connection_string)
db = client.filedemo

fs = gridfs.GridFS(db)

# Read the content of the file
with open("song.flac", "rb") as file:
    content = file.read()

# Store the content in GridFS
key = fs.put(content)
file = fs.get(key)
print(file.read())
