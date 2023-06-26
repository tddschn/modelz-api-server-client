from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesSpendLimit")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesSpendLimit:
    """
    Attributes:
        limit (Union[Unset, float]):
    """

    limit: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_spend_limit = cls(
            limit=limit,
        )

        github_com_tensorchord_modelz_apiserver_api_types_spend_limit.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_spend_limit

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
