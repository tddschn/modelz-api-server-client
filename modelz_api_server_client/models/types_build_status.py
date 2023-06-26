from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.types_build_phase import TypesBuildPhase
from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesBuildStatus")


@attr.s(auto_attribs=True)
class TypesBuildStatus:
    """
    Attributes:
        image (Union[Unset, str]):
        phase (Union[Unset, TypesBuildPhase]):
    """

    image: Union[Unset, str] = UNSET
    phase: Union[Unset, TypesBuildPhase] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image = self.image
        phase: Union[Unset, str] = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if phase is not UNSET:
            field_dict["phase"] = phase

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image = d.pop("image", UNSET)

        _phase = d.pop("phase", UNSET)
        phase: Union[Unset, TypesBuildPhase]
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = TypesBuildPhase(_phase)

        types_build_status = cls(
            image=image,
            phase=phase,
        )

        types_build_status.additional_properties = d
        return types_build_status

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
