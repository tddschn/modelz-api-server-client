from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_spec import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentSpec,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesDeploymentCreateRequest")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesDeploymentCreateRequest:
    """
    Attributes:
        spec (Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentSpec]):
    """

    spec: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesDeploymentSpec"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_spec import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentSpec,
        )

        d = src_dict.copy()
        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = GithubComTensorchordModelzApiserverApiTypesDeploymentSpec.from_dict(_spec)

        github_com_tensorchord_modelz_apiserver_api_types_deployment_create_request = cls(
            spec=spec,
        )

        github_com_tensorchord_modelz_apiserver_api_types_deployment_create_request.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_deployment_create_request

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
