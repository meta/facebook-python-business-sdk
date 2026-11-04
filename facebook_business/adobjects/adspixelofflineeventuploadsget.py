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

class AdsPixelOfflineEventUploadsGet(
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdsPixelOfflineEventUploadsGet, self).__init__()
        self._isAdsPixelOfflineEventUploadsGet = True
        self._api = api

    class Field(AbstractObject.Field):
        data = 'data'
        paging = 'paging'

    class Order:
        ascending = 'ASCENDING'
        descending = 'DESCENDING'

    class SortBy:
        api_calls = 'API_CALLS'
        creation_time = 'CREATION_TIME'
        event_time_max = 'EVENT_TIME_MAX'
        event_time_min = 'EVENT_TIME_MIN'
        first_upload_time = 'FIRST_UPLOAD_TIME'
        is_excluded_for_lift = 'IS_EXCLUDED_FOR_LIFT'
        last_upload_time = 'LAST_UPLOAD_TIME'

    _field_types = {
        'data': 'list<object>',
        'paging': 'object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Order'] = AdsPixelOfflineEventUploadsGet.Order.__dict__.values()
        field_enum_info['SortBy'] = AdsPixelOfflineEventUploadsGet.SortBy.__dict__.values()
        return field_enum_info


