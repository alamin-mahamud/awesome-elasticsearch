# Elasticsearch - Study

## Table of Contents

- [What Problem it Solves](#what-problem-it-solves)
- [Previous Solutions to this problem](#previous-solutions-to-this-problem)
- [How elasticsearch is better than them](#how-elasticsearch-is-better-than-them)
- [Is there new problems](#is-there-new-problems)
- [How to guides](#how-to-guides)
- [Resources](#resources)

### What Problem it Solves

### Previous Solutions to this problem

What about systems like Postgres, that come with full-text search and ACID-transactions? (Other examples are the full-text capabilities of MySQL, MongoDB, Riak, etc.) While you can implement basic search with Postgres, there’s a huge gap both in possible performance, and in the features. As mentioned in the section on transactions, Elasticsearch can “cheat” and do a lot of caching, with no concern for multi version concurrency control and other complicating things. Search is also more than finding a keyword in a piece of text: it’s about applying domain specific knowledge to implement good relevancy models, giving an overview of the entire result space, and doing things like spell checking and autocompletion. All while being fast.

Elasticsearch is commonly used in addition to another database. A database system with stronger focus on constraints, correctness and robustness, and on being readily and transactionally updatable, has the master record - which is then asynchronously pushed to Elasticsearch. (Or pulled, if you use one of Elasticsearch’s “rivers”.)

Elasticsearch is great when you need text based information quickly indexed and later queried. It is an extremely fast database where data is queried in almost >10ms

### How elasticsearch is better than them

### Is there New Problems

Elasticsearch – Not great as a primary database
ES can handle large data sets, flexibility during single object storage and fast search queries at the cost of latency, transactions and joins
ES is not an ACID compliant database system like most SQL systems. This means it cannot block transactions, which is very important for financial actions(such as buying an item or updating a cart) where multiple tables need to be updated in sync.
ES does not come with security features such as built-in authentication or authorization.

Basically, ES is great as long as it used for its intended usage ie, distributed full-text search & aggregation. In practice, you would use Elasticsearch as a secondary database to store text-based information that needs to be quickly indexed and searched.

## How To Guides

#### RUN ELK

```shell
cd examples/elk/docker-elk
export ELK_VERSION=7.0.0; docker-compose up
```

#### Kibana console

- in browser goto - `http://localhost:5601/app/kibana`

#### CheatSheet

- REST API Syntax

```shell
<HTTP Verb> /<Index>/<Endpoint>/<ID>
```

- Create Index, Get Index, Create and Get Documents 

```shell
# create an index
PUT /customer?pretty

# get all indices
GET /_cat/indices?v

# index a document
PUT /customer/_doc/1?pretty
{
  "name": "John Doe"
}

# query a document
GET /customer/_doc/1?pretty

# Outputs
{
  "_index" : "customer",
  "_type" : "_doc",
  "_id" : "1",
  "_version" : 1,
  "_seq_no" : 25,
  "_primary_term" : 1,
  "found" : true,                       # Here found tells us that elasticsearch found the document
  "_source" : { "name": "John Doe" }    # this is the origin JSON Document
}

# Delete an Index
DELETE /customer?pretty
```

- BATCH Processing

```shell
POST /customer/_bulk?pretty
{"index":{"_id":"1"}}
{"name": "John Doe" }
{"index":{"_id":"2"}}
{"name": "Jane Doe" }
```

```shell
POST /customer/_bulk?pretty
{"update": {"_id": "1"}}
{"doc": {"name": "Alamin Mahamud Rocks"}}
{"delete": {"_id":"2"}}
```

The Bulk API does not fail due to failures in one of the actions. If a single action fails for whatever reason, it will continue to process the remainder of the actions after it. When the bulk API returns, it will provide a status for each action (in the same order it was sent in) so that you can check if a specific action failed or not.



## Resources
