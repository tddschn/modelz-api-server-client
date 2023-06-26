from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesInstanceSpec")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesInstanceSpec:
    """
    Attributes:
        name (Union[Unset, str]):
        owner_reference (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    owner_reference: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        owner_reference = self.owner_reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if owner_reference is not UNSET:
            field_dict["owner_reference"] = owner_reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        owner_reference = d.pop("owner_reference", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_instance_spec = cls(
            name=name,
            owner_reference=owner_reference,
        )

        github_com_tensorchord_modelz_apiserver_api_types_instance_spec.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_instance_spec

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
