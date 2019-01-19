# Elasticsearch
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

