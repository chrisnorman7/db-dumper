from attr import attrs, attrib, asdict
from db_dumper import load, dump


@attrs
class DummyObject:
    name = attrib()
    age = attrib()


def test_dump():
    o = DummyObject('Chris Norman', 28)
    l = dump([o])
    assert len(l) is 1
    assert list(l.keys()) == [DummyObject.__name__]
    assert list(l.values())[0][0] == asdict(o)


def test_load():
    me = DummyObject('Chris Norman', 28)
    dog = DummyObject('Fliss', 10)
    d = dump([me, dog])
    objects = load(d, [DummyObject])
    assert len(objects) is 2
    loaded_me, loaded_dog = objects
    assert loaded_me == me
    assert loaded_dog == dog
