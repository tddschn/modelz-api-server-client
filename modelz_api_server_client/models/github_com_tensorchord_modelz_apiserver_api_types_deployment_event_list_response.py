from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_event import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentEvent,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesDeploymentEventListResponse")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesDeploymentEventListResponse:
    """
    Attributes:
        events (Union[Unset, List['GithubComTensorchordModelzApiserverApiTypesDeploymentEvent']]):
    """

    events: Union[Unset, List["GithubComTensorchordModelzApiserverApiTypesDeploymentEvent"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()

                events.append(events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_event import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentEvent,
        )

        d = src_dict.copy()
        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = GithubComTensorchordModelzApiserverApiTypesDeploymentEvent.from_dict(events_item_data)

            events.append(events_item)

        github_com_tensorchord_modelz_apiserver_api_types_deployment_event_list_response = cls(
            events=events,
        )

        github_com_tensorchord_modelz_apiserver_api_types_deployment_event_list_response.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_deployment_event_list_response

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
