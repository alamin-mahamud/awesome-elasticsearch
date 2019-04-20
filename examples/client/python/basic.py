from datetime import datetime
from elasticsearch import Elasticsearch

# By Default localhost:9200
es = Elasticsearch()

# Datetime will be serialized
es.index(
    index='my-index',
    doc_type='test-type',
    id=42,
    body={
        "any": "data",
        "timestamp": datetime.now()
    }
)

# but not deserialized
es.get(
    index="my-index",
    doc_type="test-type",
    id=42)['_source']
