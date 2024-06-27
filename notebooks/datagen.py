import os
import random
import string
import uuid

from faker import Faker
from schemas import protobuf_all_datatypes_pb2

fake = Faker()


def generate_key():
    return str(uuid.uuid4())


def generate_headers():
    return {
        "foo": fake.word(),
        "bar": str(fake.random_int()),
        "baz": str(fake.random_number()),
        "schema_id": str(100001),
        "schema_version": str(1),
    }


def generate_avro_all_datatypes():
    return {
        "nullField": None,
        "booleanField": fake.boolean(),
        "intField": fake.random_int(),
        "floatField": fake.random_number(),
        "doubleField": fake.random_number(),
        "bytesField": fake.binary(length=10),
        "stringField": fake.sentence(),
        "arrayField": [fake.word() for _ in range(5)],
        "mapField": {fake.word(): fake.random_int() for _ in range(5)},
        "enumField": fake.random_element(elements=("A", "B", "C")),
        "fixedField": os.urandom(16),
        "unionField": fake.random_element(elements=(None, fake.sentence())),
        "recordField": {"nestedField": fake.word()},
    }


def generate_jsonschema_all_datatypes():
    # key1 is required
    object = (
        {"key1": fake.word(), "key2": fake.random_int()}
        if random.choice([True, False])
        else {"key1": fake.word()}
    )
    return {
        "nullField": None,
        "booleanField": fake.boolean(),
        "integerField": fake.random_int(),
        "numberField": fake.random_number(),
        "stringField": fake.sentence(),
        "arrayField": [fake.word() for _ in range(5)],
        "objectField": object,
        "enumField": fake.random_element(elements=("A", "B", "C")),
        "constField": "sampleConst",
        "oneOfField": fake.random_element(
            elements=(fake.random_int(), fake.sentence())
        ),
        "allOfField": fake.pystr(min_chars=3, max_chars=5),
        "notField": fake.random_digit(),
    }


def generate_protobuf_all_datatypes():
    sample_message = protobuf_all_datatypes_pb2.SampleMessage()

    sample_message.boolean_field = fake.boolean()
    sample_message.int32_field = fake.random_int(min=-(2**31), max=2**31 - 1)
    sample_message.int64_field = fake.random_int(min=-(2**63), max=2**63 - 1)
    sample_message.uint32_field = fake.random_int(min=0, max=2**31 - 1)
    sample_message.uint64_field = fake.random_int(min=0, max=2**63 - 1)
    sample_message.sint32_field = fake.random_int(min=-(2**31), max=2**31 - 1)
    sample_message.sint64_field = fake.random_int(min=-(2**63), max=2**63 - 1)
    sample_message.fixed32_field = fake.random_int(min=0, max=2**32 - 1)
    sample_message.fixed64_field = fake.random_int(min=0, max=2**64 - 1)
    sample_message.sfixed32_field = fake.random_int(min=-(2**31), max=2**31 - 1)
    sample_message.sfixed64_field = fake.random_int(min=-(2**63), max=2**63 - 1)
    sample_message.float_field = fake.random_number()
    sample_message.double_field = fake.random_number()
    sample_message.bytes_field = fake.binary(length=10)
    sample_message.string_field = fake.sentence()

    sample_message.enum_field = fake.random_element(
        [
            protobuf_all_datatypes_pb2.SampleMessage.ENUM_TYPE1,
            protobuf_all_datatypes_pb2.SampleMessage.ENUM_TYPE2,
            protobuf_all_datatypes_pb2.SampleMessage.ENUM_TYPE3,
        ]
    )

    nested_message = sample_message.nested_message_field
    nested_message.nested_int32_field = fake.random_int()

    for _ in range(3):
        sample_message.repeated_boolean_field.append(fake.boolean())

    sample_message.map_field["key1"] = fake.random_int()

    if fake.boolean():
        sample_message.oneof_string_field = fake.sentence()
    else:
        sample_message.oneof_int32_field = fake.random_int()

    return sample_message


def generate_large_string(size: int = 256 * 1024):
    return "".join(random.choices(string.ascii_letters + string.digits, k=size))


def generate_large_bytes(size: int = 256 * 1024):
    return str(os.urandom(size))


def generate_large_array(size: int = 256 * 1024, item_size: int = 1024):
    num_elements = size // item_size
    return [generate_large_string(item_size) for _ in range(num_elements)]


def generate_large_map(
    size: int = 256 * 1024, key_size: int = 16, value_size: int = 1024
):
    num_entries = size // (key_size + value_size)
    return {
        generate_large_string(key_size): generate_large_string(value_size)
        for _ in range(num_entries)
    }


def generate_large_datatypes(size: int = 256 * 1024):
    return {
        "largeString": generate_large_string(size),
        "largeBytes": generate_large_bytes(size),
        "largeArray": generate_large_array(size),
        "largeMap": generate_large_map(size),
    }
