from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesMeterSessionKeyResponse")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesMeterSessionKeyResponse:
    """
    Attributes:
        session_token (Union[Unset, str]):
    """

    session_token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        session_token = self.session_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_token is not UNSET:
            field_dict["session_token"] = session_token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        session_token = d.pop("session_token", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_meter_session_key_response = cls(
            session_token=session_token,
        )

        github_com_tensorchord_modelz_apiserver_api_types_meter_session_key_response.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_meter_session_key_response

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
