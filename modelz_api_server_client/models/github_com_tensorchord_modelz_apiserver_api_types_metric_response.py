from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_api_types_metric import (
        GithubComTensorchordModelzApiserverApiTypesMetric,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverApiTypesMetricResponse")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverApiTypesMetricResponse:
    """
    Attributes:
        metrics (Union[Unset, List['GithubComTensorchordModelzApiserverApiTypesMetric']]):
    """

    metrics: Union[Unset, List["GithubComTensorchordModelzApiserverApiTypesMetric"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metrics: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()

                metrics.append(metrics_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_api_types_metric import (
            GithubComTensorchordModelzApiserverApiTypesMetric,
        )

        d = src_dict.copy()
        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = GithubComTensorchordModelzApiserverApiTypesMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        github_com_tensorchord_modelz_apiserver_api_types_metric_response = cls(
            metrics=metrics,
        )

        github_com_tensorchord_modelz_apiserver_api_types_metric_response.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_api_types_metric_response

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
