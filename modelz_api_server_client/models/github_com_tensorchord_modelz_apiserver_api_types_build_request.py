from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesBuildRequest")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesBuildRequest:
    """
    Attributes:
        branch (Union[Unset, str]):
        image (Union[Unset, str]):
        repo (Union[Unset, str]):
        tag (Union[Unset, str]):
    """

    branch: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    repo: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        branch = self.branch
        image = self.image
        repo = self.repo
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if branch is not UNSET:
            field_dict["branch"] = branch
        if image is not UNSET:
            field_dict["image"] = image
        if repo is not UNSET:
            field_dict["repo"] = repo
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        branch = d.pop("branch", UNSET)

        image = d.pop("image", UNSET)

        repo = d.pop("repo", UNSET)

        tag = d.pop("tag", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_build_request = cls(
            branch=branch,
            image=image,
            repo=repo,
            tag=tag,
        )

        github_com_tensorchord_modelz_apiserver_api_types_build_request.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_build_request

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
