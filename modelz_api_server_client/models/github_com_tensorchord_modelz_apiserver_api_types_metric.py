from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesMetric")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesMetric:
    """
    Attributes:
        unix_seconds (Union[Unset, int]):
        value (Union[Unset, float]):
    """

    unix_seconds: Union[Unset, int] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unix_seconds = self.unix_seconds
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unix_seconds is not UNSET:
            field_dict["unix_seconds"] = unix_seconds
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unix_seconds = d.pop("unix_seconds", UNSET)

        value = d.pop("value", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_metric = cls(
            unix_seconds=unix_seconds,
            value=value,
        )

        github_com_tensorchord_modelz_apiserver_api_types_metric.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_metric

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
