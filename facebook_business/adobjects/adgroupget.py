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

class AdgroupGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdgroupGet = True
        super(AdgroupGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        account_id = 'account_id'
        ad_active_time = 'ad_active_time'
        ad_schedule_end_time = 'ad_schedule_end_time'
        ad_schedule_start_time = 'ad_schedule_start_time'
        adcreatives = 'adcreatives'
        adlabels = 'adlabels'
        adrules_governed = 'adrules_governed'
        adset = 'adset'
        adset_id = 'adset_id'
        bid_amount = 'bid_amount'
        bid_info = 'bid_info'
        bid_type = 'bid_type'
        campaign = 'campaign'
        campaign_id = 'campaign_id'
        can_aggregate_social_feedback_on_edit = 'can_aggregate_social_feedback_on_edit'
        clicks = 'clicks'
        configured_status = 'configured_status'
        conversion_domain = 'conversion_domain'
        conversion_specs = 'conversion_specs'
        created_time = 'created_time'
        creative = 'creative'
        creative_asset_groups_spec = 'creative_asset_groups_spec'
        creative_audience_pairing_persona = 'creative_audience_pairing_persona'
        creative_body = 'creative_body'
        creative_history = 'creative_history'
        creative_id = 'creative_id'
        creative_link_url = 'creative_link_url'
        creative_title = 'creative_title'
        delivery_info = 'delivery_info'
        delivery_status = 'delivery_status'
        demolink_hash = 'demolink_hash'
        display_sequence = 'display_sequence'
        effective_status = 'effective_status'
        engagement_audience = 'engagement_audience'
        frequency = 'frequency'
        id = 'id'
        impressions = 'impressions'
        is_autobid = 'is_autobid'
        last_updated_by_app_id = 'last_updated_by_app_id'
        meta_reward_adgroup_status = 'meta_reward_adgroup_status'
        special_ad_categories = 'special_ad_categories'
        spent = 'spent'
        status = 'status'
        updated_time = 'updated_time'
        view_tags = 'view_tags'
        yesterday_spent = 'yesterday_spent'

    class DatePreset:
        data_maximum = 'DATA_MAXIMUM'
        last_12m = 'LAST_12M'
        last_14d = 'LAST_14D'
        last_14_days = 'LAST_14_DAYS'
        last_180d = 'LAST_180D'
        last_180_days = 'LAST_180_DAYS'
        last_24m = 'LAST_24M'
        last_28d = 'LAST_28D'
        last_28_days = 'LAST_28_DAYS'
        last_2d = 'LAST_2D'
        last_2_days = 'LAST_2_DAYS'
        last_30d = 'LAST_30D'
        last_30_days = 'LAST_30_DAYS'
        last_3d = 'LAST_3D'
        last_3_days = 'LAST_3_DAYS'
        last_3_months = 'LAST_3_MONTHS'
        last_40d = 'LAST_40D'
        last_60d = 'LAST_60D'
        last_7d = 'LAST_7D'
        last_7_days = 'LAST_7_DAYS'
        last_8_days = 'LAST_8_DAYS'
        last_90d = 'LAST_90D'
        last_90_days = 'LAST_90_DAYS'
        last_month = 'LAST_MONTH'
        last_nd_3_2 = 'LAST_ND_3_2'
        last_nd_4_3 = 'LAST_ND_4_3'
        last_nd_5_4 = 'LAST_ND_5_4'
        last_nd_6_5 = 'LAST_ND_6_5'
        last_nd_7_6 = 'LAST_ND_7_6'
        last_nd_8_7 = 'LAST_ND_8_7'
        last_nm_1_0 = 'LAST_NM_1_0'
        last_nm_2_0 = 'LAST_NM_2_0'
        last_nm_3_0 = 'LAST_NM_3_0'
        last_nm_3_2 = 'LAST_NM_3_2'
        last_nm_4_3 = 'LAST_NM_4_3'
        last_nm_5_4 = 'LAST_NM_5_4'
        last_nq_2_0 = 'LAST_NQ_2_0'
        last_nq_2_1 = 'LAST_NQ_2_1'
        last_nq_3_0 = 'LAST_NQ_3_0'
        last_nq_3_1 = 'LAST_NQ_3_1'
        last_quarter = 'LAST_QUARTER'
        last_week = 'LAST_WEEK'
        last_week_mon_sun = 'LAST_WEEK_MON_SUN'
        last_week_sun_sat = 'LAST_WEEK_SUN_SAT'
        last_year = 'LAST_YEAR'
        lifetime = 'LIFETIME'
        maximum = 'MAXIMUM'
        none = 'NONE'
        this_month = 'THIS_MONTH'
        this_month_no_today = 'THIS_MONTH_NO_TODAY'
        this_quarter = 'THIS_QUARTER'
        this_week = 'THIS_WEEK'
        this_week_mon_no_today = 'THIS_WEEK_MON_NO_TODAY'
        this_week_mon_today = 'THIS_WEEK_MON_TODAY'
        this_week_sun_no_today = 'THIS_WEEK_SUN_NO_TODAY'
        this_week_sun_today = 'THIS_WEEK_SUN_TODAY'
        this_year = 'THIS_YEAR'
        today = 'TODAY'
        yesterday = 'YESTERDAY'

    _field_types = {
        'account_id': 'string',
        'ad_active_time': 'string',
        'ad_schedule_end_time': 'mixed',
        'ad_schedule_start_time': 'mixed',
        'adcreatives': 'object',
        'adlabels': 'list<object>',
        'adrules_governed': 'object',
        'adset': 'object',
        'adset_id': 'int',
        'bid_amount': 'int',
        'bid_info': 'map<int, int>',
        'bid_type': 'string',
        'campaign': 'object',
        'campaign_id': 'int',
        'can_aggregate_social_feedback_on_edit': 'bool',
        'clicks': 'int',
        'configured_status': 'string',
        'conversion_domain': 'string',
        'conversion_specs': 'list<object>',
        'created_time': 'mixed',
        'creative': 'object',
        'creative_asset_groups_spec': 'object',
        'creative_audience_pairing_persona': 'object',
        'creative_body': 'string',
        'creative_history': 'list<object>',
        'creative_id': 'int',
        'creative_link_url': 'string',
        'creative_title': 'string',
        'delivery_info': 'object',
        'delivery_status': 'object',
        'demolink_hash': 'string',
        'display_sequence': 'int',
        'effective_status': 'string',
        'engagement_audience': 'bool',
        'frequency': 'float',
        'id': 'int',
        'impressions': 'int',
        'is_autobid': 'bool',
        'last_updated_by_app_id': 'string',
        'meta_reward_adgroup_status': 'string',
        'special_ad_categories': 'list<string>',
        'spent': 'string',
        'status': 'string',
        'updated_time': 'mixed',
        'view_tags': 'list<string>',
        'yesterday_spent': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['DatePreset'] = AdgroupGet.DatePreset.__dict__.values()
        return field_enum_info


