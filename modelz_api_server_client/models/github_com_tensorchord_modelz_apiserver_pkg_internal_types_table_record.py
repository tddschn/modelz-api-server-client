from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_tensorchord_modelz_apiserver_pkg_internal_types_record import (
        GithubComTensorchordModelzApiserverPkgInternalTypesRecord,
    )


T = TypeVar("T", bound="GithubComTensorchordModelzApiserverPkgInternalTypesTableRecord")


@attr.s(auto_attribs=True)
class GithubComTensorchordModelzApiserverPkgInternalTypesTableRecord:
    """
    Attributes:
        record (Union[Unset, GithubComTensorchordModelzApiserverPkgInternalTypesRecord]):
        schema (Union[Unset, str]):
        table (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    record: Union[Unset, "GithubComTensorchordModelzApiserverPkgInternalTypesRecord"] = UNSET
    schema: Union[Unset, str] = UNSET
    table: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record, Unset):
            record = self.record.to_dict()

        schema = self.schema
        table = self.table
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record is not UNSET:
            field_dict["record"] = record
        if schema is not UNSET:
            field_dict["schema"] = schema
        if table is not UNSET:
            field_dict["table"] = table
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.github_com_tensorchord_modelz_apiserver_pkg_internal_types_record import (
            GithubComTensorchordModelzApiserverPkgInternalTypesRecord,
        )

        d = src_dict.copy()
        _record = d.pop("record", UNSET)
        record: Union[Unset, GithubComTensorchordModelzApiserverPkgInternalTypesRecord]
        if isinstance(_record, Unset):
            record = UNSET
        else:
            record = GithubComTensorchordModelzApiserverPkgInternalTypesRecord.from_dict(_record)

        schema = d.pop("schema", UNSET)

        table = d.pop("table", UNSET)

        type = d.pop("type", UNSET)

        github_com_tensorchord_modelz_apiserver_pkg_internal_types_table_record = cls(
            record=record,
            schema=schema,
            table=table,
            type=type,
        )

        github_com_tensorchord_modelz_apiserver_pkg_internal_types_table_record.additional_properties = d
        return github_com_tensorchord_modelz_apiserver_pkg_internal_types_table_record

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
