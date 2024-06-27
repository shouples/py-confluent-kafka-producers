# py-confluent-kafka-producers

Uses [faker](https://faker.readthedocs.io/en/master/) and [confluent_kafka](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html#) inside notebooks to generate data and produce it to Kafka topics.

## Installation

This project uses [poetry](https://python-poetry.org/) for dependency management. To install the dependencies, run the following command:
```bash
poetry install
```

> [!NOTE]
> To compile protobuf schemas, you'll need `protoc` via [protobuf](https://grpc.io/docs/protoc-installation/). Once that's installed, run the following command:
> ```bash
> protoc --python_out=. ./notebooks/schemas/*.proto
> ```
> And then import them in the notebooks with:
> ```python
> from schemas import name_of_generated_protobuf_python_file_pb2
> ```

## Related VSCode Extensions
- [Avro Tools](https://marketplace.visualstudio.com/items?itemName=tomaszbartoszewski.avro-tools)
- [Protobuf support](https://marketplace.visualstudio.com/items?itemName=peterj.proto)
