from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment import (
        GithubComTensorchordModelzApiserverApiTypesDeployment,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesDeploymentListResponse")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesDeploymentListResponse:
    """
    Attributes:
        deployments (Union[Unset, List['GithubComTensorchordModelzApiserverApiTypesDeployment']]):
    """

    deployments: Union[Unset, List["GithubComTensorchordModelzApiserverApiTypesDeployment"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        deployments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deployments, Unset):
            deployments = []
            for deployments_item_data in self.deployments:
                deployments_item = deployments_item_data.to_dict()

                deployments.append(deployments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deployments is not UNSET:
            field_dict["deployments"] = deployments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment import (
            GithubComTensorchordModelzApiserverApiTypesDeployment,
        )

        d = src_dict.copy()
        deployments = []
        _deployments = d.pop("deployments", UNSET)
        for deployments_item_data in _deployments or []:
            deployments_item = GithubComTensorchordModelzApiserverApiTypesDeployment.from_dict(deployments_item_data)

            deployments.append(deployments_item)

        github_com_tensorchord_modelz_apiserver_api_types_deployment_list_response = cls(
            deployments=deployments,
        )

        github_com_tensorchord_modelz_apiserver_api_types_deployment_list_response.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_deployment_list_response

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
