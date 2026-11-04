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

class CreativeReadiness(
    AbstractObject,
):

    def __init__(self, api=None):
        super(CreativeReadiness, self).__init__()
        self._isCreativeReadiness = True
        self._api = api

    class Field(AbstractObject.Field):
        ad_ids = 'ad_ids'
        analysis_status = 'analysis_status'
        asset_type = 'asset_type'
        checks = 'checks'
        creative_id = 'creative_id'

    _field_types = {
        'ad_ids': 'list<string>',
        'analysis_status': 'string',
        'asset_type': 'string',
        'checks': 'list<Object>',
        'creative_id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


