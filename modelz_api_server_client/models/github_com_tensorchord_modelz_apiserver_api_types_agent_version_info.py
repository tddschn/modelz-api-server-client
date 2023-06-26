from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_version_info import (
        GithubComTensorchordModelzApiserverApiTypesVersionInfo,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesAgentVersionInfo")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesAgentVersionInfo:
    """
    Attributes:
        orchestration (Union[Unset, str]):
        provider (Union[Unset, str]):
        version (Union[Unset, GithubComTensorchordModelzApiserverApiTypesVersionInfo]):
    """

    orchestration: Union[Unset, str] = UNSET
    provider: Union[Unset, str] = UNSET
    version: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesVersionInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        orchestration = self.orchestration
        provider = self.provider
        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orchestration is not UNSET:
            field_dict["orchestration"] = orchestration
        if provider is not UNSET:
            field_dict["provider"] = provider
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_version_info import (
            GithubComTensorchordModelzApiserverApiTypesVersionInfo,
        )

        d = src_dict.copy()
        orchestration = d.pop("orchestration", UNSET)

        provider = d.pop("provider", UNSET)

        _version = d.pop("version", UNSET)
        version: Union[Unset, GithubComTensorchordModelzApiserverApiTypesVersionInfo]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = GithubComTensorchordModelzApiserverApiTypesVersionInfo.from_dict(_version)

        github_com_tensorchord_modelz_apiserver_api_types_agent_version_info = cls(
            orchestration=orchestration,
            provider=provider,
            version=version,
        )

        github_com_tensorchord_modelz_apiserver_api_types_agent_version_info.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_agent_version_info

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
