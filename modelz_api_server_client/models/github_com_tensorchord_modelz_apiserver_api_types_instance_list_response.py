from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_instance import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentInstance,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesInstanceListResponse")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesInstanceListResponse:
    """
    Attributes:
        instances (Union[Unset, List['GithubComTensorchordModelzApiserverApiTypesDeploymentInstance']]):
    """

    instances: Union[Unset, List["GithubComTensorchordModelzApiserverApiTypesDeploymentInstance"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.instances, Unset):
            instances = []
            for instances_item_data in self.instances:
                instances_item = instances_item_data.to_dict()

                instances.append(instances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instances is not UNSET:
            field_dict["instances"] = instances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_instance import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentInstance,
        )

        d = src_dict.copy()
        instances = []
        _instances = d.pop("instances", UNSET)
        for instances_item_data in _instances or []:
            instances_item = GithubComTensorchordModelzApiserverApiTypesDeploymentInstance.from_dict(
                instances_item_data
            )

            instances.append(instances_item)

        github_com_tensorchord_modelz_apiserver_api_types_instance_list_response = cls(
            instances=instances,
        )

        github_com_tensorchord_modelz_apiserver_api_types_instance_list_response.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_instance_list_response

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
