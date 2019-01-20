# Elasticsearch

* Run ElasticSearch using Docker Compose

``` shell
docker-compose up --build
```

* Monitor Health check
``` shell
curl -X GET "localhost:9200/_cat/health?v"
```

```
epoch      timestamp cluster        status node.total node.data shards pri relo init unassign pending_tasks max_task_wait_time active_shards_percent
1547898883 11:54:43  docker-cluster green           1         1      1   1    0    0        0             0                  -                100.0%
```

* Nodes Details
``` shell
curl -X GET "localhost:9200/_cat/nodes?v"
```

``` shell
ip         heap.percent ram.percent cpu load_1m load_5m load_15m node.role master name
172.30.0.2           11          93  13    1.18    1.96     1.58 mdi       *      u0eQjEH
```

* List Indices
``` shell
curl -X GET "localhost:9200/_cat/indices?v"
```

``` shell
PUT /customer?pretty
GET /_cat/indices?v
```

* Insert a document
``` shell
curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'
{
  "name": "John Doe"
}
'

```
* Get a Document
``` shell
curl -X GET "localhost:9200/customer/_doc/1?pretty"
```

* Loading the sample dataset

``` shell	 
curl -H "Content-Type: application/json" \
     -X POST "localhost:9200/bank/_doc/_bulk?pretty&refresh" \
	 --data-binary "@data/bank-account.json"
```

* Searching

``` shell
curl -X GET "localhost:9200/bank/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "must": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}
'

curl -X GET "localhost:9200/bank/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "should": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}
'
curl -X GET "localhost:9200/bank/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "must_not": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}
'

curl -X GET "localhost:9200/bank/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "must": [
        { "match": { "age": "40" } }
      ],
      "must_not": [
        { "match": { "state": "ID" } }
      ]
    }
  }
}
'

```
