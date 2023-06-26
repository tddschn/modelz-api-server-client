from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesCreditWallet")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesCreditWallet:
    """
    Attributes:
        left (Union[Unset, float]):
        total (Union[Unset, float]):
        used (Union[Unset, float]):
    """

    left: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    used: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        left = self.left
        total = self.total
        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left is not UNSET:
            field_dict["left"] = left
        if total is not UNSET:
            field_dict["total"] = total
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        left = d.pop("left", UNSET)

        total = d.pop("total", UNSET)

        used = d.pop("used", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_credit_wallet = cls(
            left=left,
            total=total,
            used=used,
        )

        github_com_tensorchord_modelz_apiserver_api_types_credit_wallet.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_credit_wallet

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
