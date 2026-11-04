# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class ProductFeedScheduleGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductFeedScheduleGet = True
        super(ProductFeedScheduleGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        day_of_month = 'day_of_month'
        day_of_week = 'day_of_week'
        feed_schedule_mode = 'feed_schedule_mode'
        hour = 'hour'
        id = 'id'
        interval = 'interval'
        interval_count = 'interval_count'
        minute = 'minute'
        next_scheduled_upload_time = 'next_scheduled_upload_time'
        status = 'status'
        timezone = 'timezone'
        url = 'url'
        username = 'username'

    class FeedScheduleMode:
        automatic = 'AUTOMATIC'
        fixed = 'FIXED'

    class Status:
        active = 'ACTIVE'
        suspended = 'SUSPENDED'
        waiting_on_other_feed = 'WAITING_ON_OTHER_FEED'

    _field_types = {
        'day_of_month': 'int',
        'day_of_week': 'string',
        'feed_schedule_mode': 'FeedScheduleMode',
        'hour': 'int',
        'id': 'int',
        'interval': 'string',
        'interval_count': 'int',
        'minute': 'int',
        'next_scheduled_upload_time': 'string',
        'status': 'Status',
        'timezone': 'string',
        'url': 'string',
        'username': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['FeedScheduleMode'] = ProductFeedScheduleGet.FeedScheduleMode.__dict__.values()
        field_enum_info['Status'] = ProductFeedScheduleGet.Status.__dict__.values()
        return field_enum_info


