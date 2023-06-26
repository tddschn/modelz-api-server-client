from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.github_com_tensorchord_modelz_apiserver_api_types_user_state import (
    GithubComTensorchordModelzApiserverApiTypesUserState,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesUserStatus")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesUserStatus:
    """
    Attributes:
        state (Union[Unset, GithubComTensorchordModelzApiserverApiTypesUserState]):
        user_id (Union[Unset, str]):
    """

    state: Union[Unset, GithubComTensorchordModelzApiserverApiTypesUserState] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state is not UNSET:
            field_dict["state"] = state
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _state = d.pop("state", UNSET)
        state: Union[Unset, GithubComTensorchordModelzApiserverApiTypesUserState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = GithubComTensorchordModelzApiserverApiTypesUserState(_state)

        user_id = d.pop("user_id", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_user_status = cls(
            state=state,
            user_id=user_id,
        )

        github_com_tensorchord_modelz_apiserver_api_types_user_status.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_user_status

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
