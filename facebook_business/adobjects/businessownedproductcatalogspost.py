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

class BusinessOwnedProductCatalogsPost(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isBusinessOwnedProductCatalogsPost = True
        super(BusinessOwnedProductCatalogsPost, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        ad_account_to_collaborative_ads_share_settings = 'ad_account_to_collaborative_ads_share_settings'
        agencies = 'agencies'
        agency_collaborative_ads_share_settings = 'agency_collaborative_ads_share_settings'
        assigned_users = 'assigned_users'
        business = 'business'
        can_advertise = 'can_advertise'
        can_catalog_segment_create_campaign = 'can_catalog_segment_create_campaign'
        can_create_catalog_segments = 'can_create_catalog_segments'
        can_manage = 'can_manage'
        capabilities = 'capabilities'
        capability_features = 'capability_features'
        catalog_duplicate_data = 'catalog_duplicate_data'
        catalog_item_type = 'catalog_item_type'
        catalog_segment_filter = 'catalog_segment_filter'
        catalog_segment_type = 'catalog_segment_type'
        catalog_segments = 'catalog_segments'
        catalog_store = 'catalog_store'
        check_external_event_source_association = 'check_external_event_source_association'
        checkout_urls = 'checkout_urls'
        collaborative_ads_share_settings = 'collaborative_ads_share_settings'
        commerce_merchant_settings = 'commerce_merchant_settings'
        cpas_catalog_compliance_status = 'cpas_catalog_compliance_status'
        cpas_customization_enabled_fields = 'cpas_customization_enabled_fields'
        cpas_is_mpa_lite_omni_enabled_catalog_segment = 'cpas_is_mpa_lite_omni_enabled_catalog_segment'
        cpas_parent_catalog_settings = 'cpas_parent_catalog_settings'
        creation_source = 'creation_source'
        creator_user = 'creator_user'
        da_display_settings = 'da_display_settings'
        da_pe_spend_28d = 'da_pe_spend_28d'
        da_spend_28d = 'da_spend_28d'
        data_sources = 'data_sources'
        default_image_url = 'default_image_url'
        destinations = 'destinations'
        diagnostics = 'diagnostics'
        dominant_pixel = 'dominant_pixel'
        dpa_eligible_ad_accounts = 'dpa_eligible_ad_accounts'
        event_stats = 'event_stats'
        external_event_sources = 'external_event_sources'
        fallback_image_url = 'fallback_image_url'
        feed_count = 'feed_count'
        has_external_event_source_associated_skip_privacy = 'has_external_event_source_associated_skip_privacy'
        has_issues = 'has_issues'
        has_localized_overrides = 'has_localized_overrides'
        has_multiple_partner_integrations_for_platform = 'has_multiple_partner_integrations_for_platform'
        home_listings = 'home_listings'
        hotels = 'hotels'
        hpi_count = 'hpi_count'
        id = 'id'
        is_catalog_segment = 'is_catalog_segment'
        is_eligible_for_category_targeting = 'is_eligible_for_category_targeting'
        is_eligible_for_checkout = 'is_eligible_for_checkout'
        is_eligible_for_value_optimization = 'is_eligible_for_value_optimization'
        is_local_catalog = 'is_local_catalog'
        localization_settings = 'localization_settings'
        name = 'name'
        owner_business = 'owner_business'
        page = 'page'
        parent_catalog_id = 'parent_catalog_id'
        product_count = 'product_count'
        product_feeds = 'product_feeds'
        product_groups = 'product_groups'
        product_sets = 'product_sets'
        products = 'products'
        smart_pixel_settings = 'smart_pixel_settings'
        source_app = 'source_app'
        store_catalog_settings = 'store_catalog_settings'
        sub_vertical = 'sub_vertical'
        suggested_conversion_event = 'suggested_conversion_event'
        user_tasks = 'user_tasks'
        vehicles = 'vehicles'
        vertical = 'vertical'
        website_onboarding_settings = 'website_onboarding_settings'

    class CatalogItemType:
        activity = 'ACTIVITY'
        app_and_software = 'APP_AND_SOFTWARE'
        article_and_publication = 'ARTICLE_AND_PUBLICATION'
        automotive = 'AUTOMOTIVE'
        destination = 'DESTINATION'
        flight = 'FLIGHT'
        home_listing = 'HOME_LISTING'
        hotel = 'HOTEL'
        media_title = 'MEDIA_TITLE'
        other = 'OTHER'
        product = 'PRODUCT'
        service = 'SERVICE'
        test_item = 'TEST_ITEM'

    class SuggestedConversionEvent:
        achievement_unlocked = 'ACHIEVEMENT_UNLOCKED'
        activate_app = 'ACTIVATE_APP'
        add_payment_info = 'ADD_PAYMENT_INFO'
        add_to_cart = 'ADD_TO_CART'
        add_to_wishlist = 'ADD_TO_WISHLIST'
        ad_impression = 'AD_IMPRESSION'
        complete_registration = 'COMPLETE_REGISTRATION'
        contact = 'CONTACT'
        content_view = 'CONTENT_VIEW'
        customize_product = 'CUSTOMIZE_PRODUCT'
        d2_retention = 'D2_RETENTION'
        d7_retention = 'D7_RETENTION'
        donate = 'DONATE'
        find_location = 'FIND_LOCATION'
        flow_complete = 'FLOW_COMPLETE'
        initiated_checkout = 'INITIATED_CHECKOUT'
        lead = 'LEAD'
        level_achieved = 'LEVEL_ACHIEVED'
        listing_interaction = 'LISTING_INTERACTION'
        messaging_accept = 'MESSAGING_ACCEPT'
        messaging_block = 'MESSAGING_BLOCK'
        messaging_conversation_started_7d = 'MESSAGING_CONVERSATION_STARTED_7D'
        messaging_delete_message = 'MESSAGING_DELETE_MESSAGE'
        messaging_delete_thread = 'MESSAGING_DELETE_THREAD'
        messaging_delivery_receipt = 'MESSAGING_DELIVERY_RECEIPT'
        messaging_first_reply = 'MESSAGING_FIRST_REPLY'
        messaging_ignore_request = 'MESSAGING_IGNORE_REQUEST'
        messaging_mark_spam = 'MESSAGING_MARK_SPAM'
        messaging_open_thread = 'MESSAGING_OPEN_THREAD'
        messaging_promotional_off = 'MESSAGING_PROMOTIONAL_OFF'
        messaging_read_receipt = 'MESSAGING_READ_RECEIPT'
        messaging_reply = 'MESSAGING_REPLY'
        other = 'OTHER'
        purchase = 'PURCHASE'
        rate = 'RATE'
        schedule = 'SCHEDULE'
        search = 'SEARCH'
        service_booking_request = 'SERVICE_BOOKING_REQUEST'
        spent_credits = 'SPENT_CREDITS'
        start_trial = 'START_TRIAL'
        submit_application = 'SUBMIT_APPLICATION'
        subscribe = 'SUBSCRIBE'
        tutorial_completion = 'TUTORIAL_COMPLETION'

    _field_types = {
        'ad_account_to_collaborative_ads_share_settings': 'object',
        'agencies': 'object',
        'agency_collaborative_ads_share_settings': 'object',
        'assigned_users': 'object',
        'business': 'object',
        'can_advertise': 'bool',
        'can_catalog_segment_create_campaign': 'bool',
        'can_create_catalog_segments': 'bool',
        'can_manage': 'bool',
        'capabilities': 'list<object>',
        'capability_features': 'list<string>',
        'catalog_duplicate_data': 'object',
        'catalog_item_type': 'CatalogItemType',
        'catalog_segment_filter': 'string',
        'catalog_segment_type': 'string',
        'catalog_segments': 'object',
        'catalog_store': 'object',
        'check_external_event_source_association': 'string',
        'checkout_urls': 'list<object>',
        'collaborative_ads_share_settings': 'object',
        'commerce_merchant_settings': 'object',
        'cpas_catalog_compliance_status': 'string',
        'cpas_customization_enabled_fields': 'list<string>',
        'cpas_is_mpa_lite_omni_enabled_catalog_segment': 'bool',
        'cpas_parent_catalog_settings': 'object',
        'creation_source': 'string',
        'creator_user': 'object',
        'da_display_settings': 'object',
        'da_pe_spend_28d': 'float',
        'da_spend_28d': 'float',
        'data_sources': 'object',
        'default_image_url': 'string',
        'destinations': 'object',
        'diagnostics': 'object',
        'dominant_pixel': 'string',
        'dpa_eligible_ad_accounts': 'object',
        'event_stats': 'object',
        'external_event_sources': 'object',
        'fallback_image_url': 'list<string>',
        'feed_count': 'int',
        'has_external_event_source_associated_skip_privacy': 'bool',
        'has_issues': 'bool',
        'has_localized_overrides': 'bool',
        'has_multiple_partner_integrations_for_platform': 'bool',
        'home_listings': 'object',
        'hotels': 'object',
        'hpi_count': 'int',
        'id': 'int',
        'is_catalog_segment': 'bool',
        'is_eligible_for_category_targeting': 'bool',
        'is_eligible_for_checkout': 'bool',
        'is_eligible_for_value_optimization': 'bool',
        'is_local_catalog': 'bool',
        'localization_settings': 'object',
        'name': 'string',
        'owner_business': 'object',
        'page': 'object',
        'parent_catalog_id': 'int',
        'product_count': 'int',
        'product_feeds': 'object',
        'product_groups': 'object',
        'product_sets': 'object',
        'products': 'object',
        'smart_pixel_settings': 'object',
        'source_app': 'object',
        'store_catalog_settings': 'object',
        'sub_vertical': 'string',
        'suggested_conversion_event': 'SuggestedConversionEvent',
        'user_tasks': 'object',
        'vehicles': 'object',
        'vertical': 'string',
        'website_onboarding_settings': 'object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['CatalogItemType'] = BusinessOwnedProductCatalogsPost.CatalogItemType.__dict__.values()
        field_enum_info['SuggestedConversionEvent'] = BusinessOwnedProductCatalogsPost.SuggestedConversionEvent.__dict__.values()
        return field_enum_info


