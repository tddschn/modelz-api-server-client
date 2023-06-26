from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_agent_version_info import (
        GithubComTensorchordModelzApiserverApiTypesAgentVersionInfo,
    )
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_version_info import (
        GithubComTensorchordModelzApiserverApiTypesVersionInfo,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesVersion")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesVersion:
    """
    Attributes:
        agents (Union[Unset, List['GithubComTensorchordModelzApiserverApiTypesAgentVersionInfo']]):
        version (Union[Unset, GithubComTensorchordModelzApiserverApiTypesVersionInfo]):
    """

    agents: Union[Unset, List["GithubComTensorchordModelzApiserverApiTypesAgentVersionInfo"]] = UNSET
    version: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesVersionInfo"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()

                agents.append(agents_item)

        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agents is not UNSET:
            field_dict["agents"] = agents
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_agent_version_info import (
            GithubComTensorchordModelzApiserverApiTypesAgentVersionInfo,
        )
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_version_info import (
            GithubComTensorchordModelzApiserverApiTypesVersionInfo,
        )

        d = src_dict.copy()
        agents = []
        _agents = d.pop("agents", UNSET)
        for agents_item_data in _agents or []:
            agents_item = GithubComTensorchordModelzApiserverApiTypesAgentVersionInfo.from_dict(agents_item_data)

            agents.append(agents_item)

        _version = d.pop("version", UNSET)
        version: Union[Unset, GithubComTensorchordModelzApiserverApiTypesVersionInfo]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = GithubComTensorchordModelzApiserverApiTypesVersionInfo.from_dict(_version)

        github_com_tensorchord_modelz_apiserver_api_types_version = cls(
            agents=agents,
            version=version,
        )

        github_com_tensorchord_modelz_apiserver_api_types_version.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_version

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
