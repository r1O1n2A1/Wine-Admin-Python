sudo mongod --port 27017 --dbpath /var/lib/mongodb --replSet rs0
sudo mongo-connector -m localhost:27017 -t localhost:9200 -d elastic2_doc_manager


