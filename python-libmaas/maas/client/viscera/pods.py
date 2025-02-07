"""Objects for pods."""

__all__ = [
    "Pod",
    "Pods",
]

import typing
from . import (
    check,
    Object,
    ObjectField,
    ObjectFieldRelated,
    ObjectSet,
    ObjectType,
)
from .zones import Zone
from ..utils import remove_None
from ..errors import OperationNotAllowed


class PodsType(ObjectType):
    """Metaclass for `Pods`."""

    async def read(cls):
        data = await cls._handler.read()
        return cls(map(cls._object, data))

    async def create(
            cls, *, type: str,
            power_address: str,
            power_user: str=None,
            power_pass: str=None,
            name: str=None,
            zone: typing.Union[str, Zone]=None,
            tags: typing.Sequence[str]=None):
        """Create a `Pod` in MAAS.

        :param type: Type of pod to create (rsd, virsh) (required).
        :type name: `str`
        :param power_address: Address for power control of the pod (required).
        :type power_address: `str`
        :param power_user: User for power control of the pod
            (required for rsd).
        :type power_user: `str`
        :param power_pass: Password for power control of the pod
            (required for rsd).
        :type power_pass: `str`
        :param name: Name for the pod (optional).
        :type name: `str`
        :param zone: Name of the zone for the pod (optional).
        :type zone: `str` or `Zone`
        :param tags: A tag or tags (separated by comma) for the pod.
        :type tags: `str`
        :returns: The created Pod.
        :rtype: `Pod`
        """
        params = remove_None({
            'type': type,
            'power_address': power_address,
            'power_user': power_user,
            'power_pass': power_pass,
            'name': name,
            'tags': tags,
        })
        if type == 'rsd' and power_user is None:
            message = "'power_user' is required for pod type `rsd`"
            raise OperationNotAllowed(message)
        if type == 'rsd' and power_pass is None:
            message = "'power_pass' is required for pod type `rsd`"
            raise OperationNotAllowed(message)
        if zone is not None:
            if isinstance(zone, Zone):
                params["zone"] = zone.name
            elif isinstance(zone, str):
                params["zone"] = zone
            else:
                raise TypeError(
                    "zone must be a str or Zone, not %s" % type(zone).__name__)
        return cls._object(await cls._handler.create(**params))


class Pods(ObjectSet, metaclass=PodsType):
    """The set of `Pods` stored in MAAS."""


class PodType(ObjectType):
    """Metaclass for a `Pod`."""

    async def read(cls, id: int):
        """Get `Pod` by `id`."""
        data = await cls._handler.read(id=id)
        return cls(data)


class Pod(Object, metaclass=PodType):
    """A `Pod` stored in MAAS."""

    id = ObjectField.Checked(
        "id", check(int), readonly=True, pk=True)
    type = ObjectField.Checked(
        "type", check(str), check(str))
    name = ObjectField.Checked(
        "name", check(str), check(str))
    architectures = ObjectField.Checked(
        "architectures", check(list), check(list))
    capabilities = ObjectField.Checked(
        "capabilities", check(list), check(list))
    zone = ObjectFieldRelated("zone", "Zone", readonly=True)
    tags = ObjectField.Checked(
        "tags", check(list), check(list))
    cpu_over_commit_ratio = ObjectField.Checked(
        "cpu_over_commit_ratio", check(float), check(float))
    memory_over_commit_ratio = ObjectField.Checked(
        "memory_over_commit_ratio", check(float), check(float))
    available = ObjectField.Checked(
        "available", check(dict), check(dict))
    used = ObjectField.Checked(
        "used", check(dict), check(dict))
    total = ObjectField.Checked(
        "total", check(dict), check(dict))

    async def save(self):
        """Save the `Pod`."""
        old_tags = list(self._orig_data['tags'])
        new_tags = list(self.tags)
        self._changed_data.pop('tags', None)
        await super(Pod, self).save()
        for tag_name in new_tags:
            if tag_name not in old_tags:
                await self._handler.add_tag(id=self.id, tag=tag_name)
            else:
                old_tags.remove(tag_name)
        for tag_name in old_tags:
            await self._handler.remove_tag(id=self.id, tag=tag_name)
        self._orig_data['tags'] = new_tags
        self._data['tags'] = list(new_tags)

    async def refresh(self):
        """Refresh the `Pod`."""
        return await self._handler.refresh(id=self.id)

    async def parameters(self):
        """Get the power parameters for the `Pod`."""
        return await self._handler.parameters(id=self.id)

    async def compose(
            self, *, cores: int=None, memory: int=None,
            cpu_speed: int=None, architecture: str=None,
            storage: typing.Sequence[str]=None, hostname: str=None,
            domain: typing.Union[int, str]=None,
            zone: typing.Union[int, str, Zone]=None):
        """Compose a machine from `Pod`.

        All fields below are optional:

        :param cores: Minimum number of CPU cores.
        :type cores: `int`
        :param memory: Minimum amount of memory (MiB).
        :type memory: `int`
        :param cpu_speed: Minimum amount of CPU speed (MHz).
        :type cpu_speed: `int`
        :param architecture: Architecture for the machine. Must be an
            architecture that the pod supports.
        :type architecture: `str`
        :param storage: A list of storage constraint identifiers, in the form:
            <label>:<size>(<tag>[,<tag>[,...])][,<label>:...]
        :type storage: `str`
        :param hostname: Hostname for the newly composed machine.
        :type hostname: `str`
        :param domain: The domain ID for the machine (optional).
        :type domain: `int` or `str`
        :param zone: The zone ID for the machine (optional).
        :type zone: `int` or 'str' or `Zone`
        :returns: The created Machine
        :rtype: `Machine`
        """
        params = remove_None({
            'cores': str(cores) if cores else None,
            'memory': str(memory) if memory else None,
            'cpu_speed': str(cpu_speed) if cpu_speed else None,
            'architecture': architecture,
            'storage': storage,
            'hostname': hostname,
            'domain': str(domain) if domain else None,
        })
        if zone is not None:
            if isinstance(zone, Zone):
                params["zone"] = str(zone.id)
            elif isinstance(zone, int):
                params["zone"] = str(zone)
            elif isinstance(zone, str):
                params["zone"] = zone
            else:
                raise TypeError(
                    "zone must be an int, str or Zone, not %s" %
                    type(zone).__name__)
        return await self._handler.compose(**params, id=self.id)

    async def update(
            self, *, name: str=None,
            default_storage_pool: str=None,
            cpu_over_commit_ratio: float=None,
            memory_over_commit_ratio: float=None):
        """Update the `Pod`.

        :param name: Name for the pod (optional).
        :type name: `str`
        :param default_storage_pool: Default storage pool for Virsh pod
            (optional).
        :type default_storage_pool: `str`
        :param cpu_over_commit_ratio: CPU over commit ratio (optional).
        :type cpu_over_commit_ratio: `float`
        :param memory_over_commit_ratio: Memory over commit ratio (optional).
        :type memory_over_commit_ratio: `float`

        Note: 'type' cannot be updated on a Pod. The Pod must be deleted and
        re-added to change the type.
        """
        params = remove_None({
            'name': name,
            'default_storage_pool': default_storage_pool,
            'cpu_over_commit_ratio': (
                str(cpu_over_commit_ratio)
                if cpu_over_commit_ratio else None),
            'memory_over_commit_ratio': (
                str(memory_over_commit_ratio)
                if memory_over_commit_ratio else None),
        })
        if self.type != 'virsh' and default_storage_pool is not None:
            message = (
                "'default_storage_pool' only compatiable for pod type `virsh`")
            raise OperationNotAllowed(message)
        return await self._handler.update(**params, id=self.id)

    async def delete(self):
        """Delete the `Pod`."""
        return await self._handler.delete(id=self.id)
