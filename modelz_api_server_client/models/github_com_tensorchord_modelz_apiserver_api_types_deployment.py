from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_spec import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentSpec,
    )
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_status import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentStatus,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesDeployment")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesDeployment:
    """
    Attributes:
        spec (Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentSpec]):
        status (Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentStatus]):
    """

    spec: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesDeploymentSpec"] = UNSET
    status: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesDeploymentStatus"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spec is not UNSET:
            field_dict["spec"] = spec
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_spec import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentSpec,
        )
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_status import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentStatus,
        )

        d = src_dict.copy()
        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = GithubComTensorchordModelzApiserverApiTypesDeploymentSpec.from_dict(_spec)

        _status = d.pop("status", UNSET)
        status: Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GithubComTensorchordModelzApiserverApiTypesDeploymentStatus.from_dict(_status)

        github_com_tensorchord_modelz_apiserver_api_types_deployment = cls(
            spec=spec,
            status=status,
        )

        github_com_tensorchord_modelz_apiserver_api_types_deployment.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_deployment

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
