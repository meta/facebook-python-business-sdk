# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdsPixelActivitiesHead(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdsPixelActivitiesHead, self).__init__()
        self._isAdsPixelActivitiesHead = True
        self._api = api

    class Field(AbstractObject.Field):
        pass

    class EventType:
        add_dataset_to_business = 'ADD_DATASET_TO_BUSINESS'
        add_user_to_dataset = 'ADD_USER_TO_DATASET'
        create_custom_audience = 'CREATE_CUSTOM_AUDIENCE'
        create_custom_conversion = 'CREATE_CUSTOM_CONVERSION'
        dataset_assign_to_adacct = 'DATASET_ASSIGN_TO_ADACCT'
        dataset_autotrack_on_adacct = 'DATASET_AUTOTRACK_ON_ADACCT'
        dataset_disable_autotrack_on_adacct = 'DATASET_DISABLE_AUTOTRACK_ON_ADACCT'
        dataset_unassign_from_adacct = 'DATASET_UNASSIGN_FROM_ADACCT'
        remove_user_from_dataset = 'REMOVE_USER_FROM_DATASET'
        share_custom_audience = 'SHARE_CUSTOM_AUDIENCE'
        unshare_custom_audience = 'UNSHARE_CUSTOM_AUDIENCE'
        update_custom_conversion = 'UPDATE_CUSTOM_CONVERSION'
        update_user_role_on_dataset = 'UPDATE_USER_ROLE_ON_DATASET'

    _field_types = {
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['EventType'] = AdsPixelActivitiesHead.EventType.__dict__.values()
        return field_enum_info


