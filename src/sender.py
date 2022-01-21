from generated import metric_pb2
from google.protobuf.internal.encoder import _VarintBytes
from random import random

with open('proto_dump/out.bin', 'wb') as f:
    my_tags = ("my_tag", "foo:bar")
    for i in range(128):
        my_metric = metric_pb2.Metric()
        my_metric.name = 'sys.cpu'
        my_metric.type = 'gauge'
        my_metric.value = round(random(), 2)
        my_metric.tags.extend(my_tags)
        size = my_metric.ByteSize()

        f.write(_VarintBytes(size))
        f.write(my_metric.SerializeToString())