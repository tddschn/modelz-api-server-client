from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesDeploymentGuide")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesDeploymentGuide:
    """
    Attributes:
        markdown (Union[Unset, str]):
    """

    markdown: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        markdown = self.markdown

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markdown is not UNSET:
            field_dict["markdown"] = markdown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        markdown = d.pop("markdown", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_deployment_guide = cls(
            markdown=markdown,
        )

        github_com_tensorchord_modelz_apiserver_api_types_deployment_guide.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_deployment_guide

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
