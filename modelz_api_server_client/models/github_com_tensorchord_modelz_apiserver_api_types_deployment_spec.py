from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.github_com_tensorchord_modelz_apiserver_api_types_framework_type import (
    GithubComTensorchordModelzApiserverApiTypesFrameworkType,
)
from ..models.github_com_tensorchord_modelz_apiserver_api_types_server_resource import (
    GithubComTensorchordModelzApiserverApiTypesServerResource,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_source import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentSource,
    )
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_spec_env_vars import (
        GithubComTensorchordModelzApiserverApiTypesDeploymentSpecEnvVars,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesDeploymentSpec")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesDeploymentSpec:
    """
    Attributes:
        command (Union[Unset, str]): Command is the command to run.
        deployment_source (Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentSource]):
        env_vars (Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentSpecEnvVars]): EnvVars is the
            environment variables of the deployment.
        framework (Union[Unset, GithubComTensorchordModelzApiserverApiTypesFrameworkType]):
        id (Union[Unset, str]): ID holds the unique identifier of the deployment.
        max_replicas (Union[Unset, int]): MaxReplicas is the maximum number of replicas of the deployment.
        min_replicas (Union[Unset, int]): MinReplicas is the minimum number of replicas of the deployment.
        name (Union[Unset, str]): Name is the name of the deployment. e.g. demo.
            [a-z0-9]([-a-z0-9]*[a-z0-9])?
        port (Union[Unset, int]): Port is the port of the deployment.
        secret (Union[Unset, List[str]]): Secret is the secret of the deployment.
        server_resource (Union[Unset, GithubComTensorchordModelzApiserverApiTypesServerResource]):
        spot_instance (Union[Unset, bool]):
        startup_duration (Union[Unset, int]): StartupDuration is the startup timeout.
        target_load (Union[Unset, int]): TargetLoad is the target load of the deployment. (inflight requests per
            replica)
        template_id (Union[Unset, str]): TemplateID is the template ID of the deployment.
        zero_duration (Union[Unset, int]): ZeroDuration is the idle timeout before scaling to zero.
    """

    command: Union[Unset, str] = UNSET
    deployment_source: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesDeploymentSource"] = UNSET
    env_vars: Union[Unset, "GithubComTensorchordModelzApiserverApiTypesDeploymentSpecEnvVars"] = UNSET
    framework: Union[Unset, GithubComTensorchordModelzApiserverApiTypesFrameworkType] = UNSET
    id: Union[Unset, str] = UNSET
    max_replicas: Union[Unset, int] = UNSET
    min_replicas: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    secret: Union[Unset, List[str]] = UNSET
    server_resource: Union[Unset, GithubComTensorchordModelzApiserverApiTypesServerResource] = UNSET
    spot_instance: Union[Unset, bool] = UNSET
    startup_duration: Union[Unset, int] = UNSET
    target_load: Union[Unset, int] = UNSET
    template_id: Union[Unset, str] = UNSET
    zero_duration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        command = self.command
        deployment_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deployment_source, Unset):
            deployment_source = self.deployment_source.to_dict()

        env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        framework: Union[Unset, str] = UNSET
        if not isinstance(self.framework, Unset):
            framework = self.framework.value

        id = self.id
        max_replicas = self.max_replicas
        min_replicas = self.min_replicas
        name = self.name
        port = self.port
        secret: Union[Unset, List[str]] = UNSET
        if not isinstance(self.secret, Unset):
            secret = self.secret

        server_resource: Union[Unset, str] = UNSET
        if not isinstance(self.server_resource, Unset):
            server_resource = self.server_resource.value

        spot_instance = self.spot_instance
        startup_duration = self.startup_duration
        target_load = self.target_load
        template_id = self.template_id
        zero_duration = self.zero_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if deployment_source is not UNSET:
            field_dict["deployment_source"] = deployment_source
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if framework is not UNSET:
            field_dict["framework"] = framework
        if id is not UNSET:
            field_dict["id"] = id
        if max_replicas is not UNSET:
            field_dict["max_replicas"] = max_replicas
        if min_replicas is not UNSET:
            field_dict["min_replicas"] = min_replicas
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if secret is not UNSET:
            field_dict["secret"] = secret
        if server_resource is not UNSET:
            field_dict["server_resource"] = server_resource
        if spot_instance is not UNSET:
            field_dict["spot_instance"] = spot_instance
        if startup_duration is not UNSET:
            field_dict["startup_duration"] = startup_duration
        if target_load is not UNSET:
            field_dict["target_load"] = target_load
        if template_id is not UNSET:
            field_dict["templateId"] = template_id
        if zero_duration is not UNSET:
            field_dict["zero_duration"] = zero_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_source import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentSource,
        )
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_deployment_spec_env_vars import (
            GithubComTensorchordModelzApiserverApiTypesDeploymentSpecEnvVars,
        )

        d = src_dict.copy()
        command = d.pop("command", UNSET)

        _deployment_source = d.pop("deployment_source", UNSET)
        deployment_source: Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentSource]
        if isinstance(_deployment_source, Unset):
            deployment_source = UNSET
        else:
            deployment_source = GithubComTensorchordModelzApiserverApiTypesDeploymentSource.from_dict(
                _deployment_source
            )

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, GithubComTensorchordModelzApiserverApiTypesDeploymentSpecEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = GithubComTensorchordModelzApiserverApiTypesDeploymentSpecEnvVars.from_dict(_env_vars)

        _framework = d.pop("framework", UNSET)
        framework: Union[Unset, GithubComTensorchordModelzApiserverApiTypesFrameworkType]
        if isinstance(_framework, Unset):
            framework = UNSET
        else:
            framework = GithubComTensorchordModelzApiserverApiTypesFrameworkType(_framework)

        id = d.pop("id", UNSET)

        max_replicas = d.pop("max_replicas", UNSET)

        min_replicas = d.pop("min_replicas", UNSET)

        name = d.pop("name", UNSET)

        port = d.pop("port", UNSET)

        secret = cast(List[str], d.pop("secret", UNSET))

        _server_resource = d.pop("server_resource", UNSET)
        server_resource: Union[Unset, GithubComTensorchordModelzApiserverApiTypesServerResource]
        if isinstance(_server_resource, Unset):
            server_resource = UNSET
        else:
            server_resource = GithubComTensorchordModelzApiserverApiTypesServerResource(_server_resource)

        spot_instance = d.pop("spot_instance", UNSET)

        startup_duration = d.pop("startup_duration", UNSET)

        target_load = d.pop("target_load", UNSET)

        template_id = d.pop("templateId", UNSET)

        zero_duration = d.pop("zero_duration", UNSET)

        github_com_tensorchord_modelz_apiserver_api_types_deployment_spec = cls(
            command=command,
            deployment_source=deployment_source,
            env_vars=env_vars,
            framework=framework,
            id=id,
            max_replicas=max_replicas,
            min_replicas=min_replicas,
            name=name,
            port=port,
            secret=secret,
            server_resource=server_resource,
            spot_instance=spot_instance,
            startup_duration=startup_duration,
            target_load=target_load,
            template_id=template_id,
            zero_duration=zero_duration,
        )

        github_com_tensorchord_modelz_apiserver_api_types_deployment_spec.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_deployment_spec

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
