from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.types_builder_type import TypesBuilderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesBuildSpec")


@attr.s(auto_attribs=True)
class TypesBuildSpec:
    """
    Attributes:
        branch (Union[Unset, str]):
        builder (Union[Unset, TypesBuilderType]):
        directory (Union[Unset, str]): directory is the target directory name.
            Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the
            git repository.  Otherwise, if specified, the volume will contain the git repository in
            the subdirectory with the given name.
            +optional
        duration (Union[Unset, str]):
        image (Union[Unset, str]):
        image_tag (Union[Unset, str]):
        name (Union[Unset, str]):
        namespace (Union[Unset, str]):
        project_id (Union[Unset, str]):
        repository (Union[Unset, str]): repository is the URL
        revision (Union[Unset, str]): revision is the commit hash for the specified revision.
            +optional
    """

    branch: Union[Unset, str] = UNSET
    builder: Union[Unset, TypesBuilderType] = UNSET
    directory: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    image_tag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    repository: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branch = self.branch
        builder: Union[Unset, str] = UNSET
        if not isinstance(self.builder, Unset):
            builder = self.builder.value

        directory = self.directory
        duration = self.duration
        image = self.image
        image_tag = self.image_tag
        name = self.name
        namespace = self.namespace
        project_id = self.project_id
        repository = self.repository
        revision = self.revision

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if builder is not UNSET:
            field_dict["builder"] = builder
        if directory is not UNSET:
            field_dict["directory"] = directory
        if duration is not UNSET:
            field_dict["duration"] = duration
        if image is not UNSET:
            field_dict["image"] = image
        if image_tag is not UNSET:
            field_dict["image_tag"] = image_tag
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if repository is not UNSET:
            field_dict["repository"] = repository
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch = d.pop("branch", UNSET)

        _builder = d.pop("builder", UNSET)
        builder: Union[Unset, TypesBuilderType]
        if isinstance(_builder, Unset):
            builder = UNSET
        else:
            builder = TypesBuilderType(_builder)

        directory = d.pop("directory", UNSET)

        duration = d.pop("duration", UNSET)

        image = d.pop("image", UNSET)

        image_tag = d.pop("image_tag", UNSET)

        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        project_id = d.pop("project_id", UNSET)

        repository = d.pop("repository", UNSET)

        revision = d.pop("revision", UNSET)

        types_build_spec = cls(
            branch=branch,
            builder=builder,
            directory=directory,
            duration=duration,
            image=image,
            image_tag=image_tag,
            name=name,
            namespace=namespace,
            project_id=project_id,
            repository=repository,
            revision=revision,
        )

        types_build_spec.additional_properties = d
        return types_build_spec

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
