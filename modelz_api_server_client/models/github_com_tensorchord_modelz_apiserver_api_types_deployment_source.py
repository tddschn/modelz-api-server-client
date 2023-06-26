from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_docker_source import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentDockerSource,
    )
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_git_source import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentGitSource,
    )
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_huggingface_space_source import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentHuggingfaceSpaceSource,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesDeploymentSource")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesDeploymentSource:
    """
    Attributes:
        docker (Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentDockerSource]):
        git (Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentGitSource]):
        huggingface (Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentHuggingfaceSpaceSource]):
    """

    docker: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesDeploymentDockerSource"] = UNSET
    git: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesDeploymentGitSource"] = UNSET
    huggingface: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesDeploymentHuggingfaceSpaceSource"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        docker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.docker, Unset):
            docker = self.docker.to_dict()

        git: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.git, Unset):
            git = self.git.to_dict()

        huggingface: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.huggingface, Unset):
            huggingface = self.huggingface.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if docker is not UNSET:
            field_dict["docker"] = docker
        if git is not UNSET:
            field_dict["git"] = git
        if huggingface is not UNSET:
            field_dict["huggingface"] = huggingface

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_docker_source import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentDockerSource,
        )
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_git_source import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentGitSource,
        )
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_huggingface_space_source import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentHuggingfaceSpaceSource,
        )

        d = src_dict.copy()
        _docker = d.pop("docker", UNSET)
        docker: Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentDockerSource]
        if isinstance(_docker, Unset):
            docker = UNSET
        else:
            docker = GithubComTensorchordModelzApiserverApiTypesDeploymentDockerSource.from_dict(_docker)

        _git = d.pop("git", UNSET)
        git: Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentGitSource]
        if isinstance(_git, Unset):
            git = UNSET
        else:
            git = GithubComTensorchordModelzApiserverApiTypesDeploymentGitSource.from_dict(_git)

        _huggingface = d.pop("huggingface", UNSET)
        huggingface: Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentHuggingfaceSpaceSource]
        if isinstance(_huggingface, Unset):
            huggingface = UNSET
        else:
            huggingface = GithubComTensorchordModelzApiserverApiTypesDeploymentHuggingfaceSpaceSource.from_dict(
                _huggingface
            )

        github_com_tensorchord_modelz_apiserver_api_types_deployment_source = cls(
            docker=docker,
            git=git,
            huggingface=huggingface,
        )

        github_com_tensorchord_modelz_apiserver_api_types_deployment_source.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_deployment_source

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
