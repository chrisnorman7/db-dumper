"""Load and dump databases to disk."""

from attr import asdict


def load(source, classes):
    """Load 0 or more objects from source and instantiate them with the classes
    found in the classes iterable. They will be returned as a list which can be
    passed to session.add_all for example. No saving will be performed. Pass a
    dictionary as source with name: list-of-dictionaries as pairs."""
    objects = []  # All the created objects.
    classes = {x.__name__: x for x in classes}
    for name, data in source.items():
        cls = classes[name]
        for datum in data:
            # Let's load.
            objects.append(cls(**datum))
    return objects


def dump(objects, dump_object=None):
    """Return a dictionary suitable for loading with the load function. Objects
    will be dumped with attr.asdict if dump_object is None."""
    d = {}
    if dump_object is None:
        dump_object = asdict
    for obj in objects:
        name = obj.__class__.__name__
        d[name] = d.get(name, [])
        d[name].append(dump_object(obj))
    return d


__all__ = ['load', 'dump']
