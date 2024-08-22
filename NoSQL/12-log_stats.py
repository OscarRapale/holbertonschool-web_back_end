#!/usr/bin/env python3

"""This script provides stats about Nginx"""


from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.logs
collection = db.nginx

# Get total number of logs
log_count = collection.count_documents({})

# Get count for each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method})
                 for method in methods}

# Get count for GET requests with path '/status'
status_check_count = collection.count_documents
({"method": "GET", "path": "/status"})

# Display the results
print(f"{log_count} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
