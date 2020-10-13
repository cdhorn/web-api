"""Family API resource."""

from typing import Dict

from gramps.gen.lib import Family

from .base import (
    GrampsObjectProtectedResource,
    GrampsObjectResourceHelper,
    GrampsObjectsProtectedResource,
)
from .util import (
    get_extended_attributes,
    get_family_profile_for_object,
    get_person_by_handle,
)


class FamilyResourceHelper(GrampsObjectResourceHelper):
    """Family resource helper."""

    gramps_class_name = "Family"

    def object_extend(self, obj: Family, args: Dict) -> Family:
        """Extend family attributes as needed."""
        db_handle = self.db_handle
        if args["profile"]:
            obj.profile = get_family_profile_for_object(
                db_handle, obj, with_events=True
            )
        if args["extend"]:
            obj.extended = get_extended_attributes(db_handle, obj)
            obj.extended["father"] = get_person_by_handle(db_handle, obj.father_handle)
            obj.extended["mother"] = get_person_by_handle(db_handle, obj.mother_handle)
        return obj


class FamilyResource(GrampsObjectProtectedResource, FamilyResourceHelper):
    """Family resource."""


class FamiliesResource(GrampsObjectsProtectedResource, FamilyResourceHelper):
    """Families resource."""