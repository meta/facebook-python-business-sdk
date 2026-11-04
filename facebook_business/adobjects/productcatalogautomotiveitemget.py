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

class ProductCatalogAutomotiveItemGet(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isProductCatalogAutomotiveItemGet = True
        super(ProductCatalogAutomotiveItemGet, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        address = 'address'
        amount_currency = 'amount_currency'
        amount_percentage = 'amount_percentage'
        amount_price = 'amount_price'
        amount_qualifier = 'amount_qualifier'
        applinks = 'applinks'
        automotive_model_id = 'automotive_model_id'
        availability = 'availability'
        availability_circle_radius = 'availability_circle_radius'
        availability_circle_radius_unit = 'availability_circle_radius_unit'
        body_style = 'body_style'
        capabilities = 'capabilities'
        capabilities_disabled_by_user = 'capabilities_disabled_by_user'
        capabilities_rendering_catalog_manager = 'capabilities_rendering_catalog_manager'
        carfax_dealership_id = 'carfax_dealership_id'
        channels_to_integrity_status = 'channels_to_integrity_status'
        comscore_market_codes = 'comscore_market_codes'
        condition = 'condition'
        currency = 'currency'
        custom_label_0 = 'custom_label_0'
        custom_label_1 = 'custom_label_1'
        custom_label_2 = 'custom_label_2'
        custom_label_3 = 'custom_label_3'
        custom_label_4 = 'custom_label_4'
        custom_number_0 = 'custom_number_0'
        custom_number_1 = 'custom_number_1'
        custom_number_2 = 'custom_number_2'
        custom_number_3 = 'custom_number_3'
        custom_number_4 = 'custom_number_4'
        date_first_on_lot = 'date_first_on_lot'
        days_on_lot = 'days_on_lot'
        dealer_communication_channel = 'dealer_communication_channel'
        dealer_email = 'dealer_email'
        dealer_id = 'dealer_id'
        dealer_name = 'dealer_name'
        dealer_phone = 'dealer_phone'
        dealer_privacy_policy_url = 'dealer_privacy_policy_url'
        dealer_url = 'dealer_url'
        default_country = 'default_country'
        default_language_locale = 'default_language_locale'
        description = 'description'
        downpayment_currency = 'downpayment_currency'
        downpayment_price = 'downpayment_price'
        downpayment_qualifier = 'downpayment_qualifier'
        drivetrain = 'drivetrain'
        enabled_capability_to_review_status = 'enabled_capability_to_review_status'
        end_date = 'end_date'
        engine_size = 'engine_size'
        exterior_color = 'exterior_color'
        fb_page_id = 'fb_page_id'
        features = 'features'
        finance_description = 'finance_description'
        finance_type = 'finance_type'
        fuel_type = 'fuel_type'
        generation = 'generation'
        horse_power = 'horse_power'
        id = 'id'
        image_fetch_status = 'image_fetch_status'
        images = 'images'
        interior_color = 'interior_color'
        interior_upholstery = 'interior_upholstery'
        is_blackholed = 'is_blackholed'
        legal_disclosure_impressum_url = 'legal_disclosure_impressum_url'
        make = 'make'
        mileage = 'mileage'
        model = 'model'
        offer_description = 'offer_description'
        offer_disclaimer = 'offer_disclaimer'
        offer_disclaimer_url = 'offer_disclaimer_url'
        offer_type = 'offer_type'
        previous_currency = 'previous_currency'
        previous_price = 'previous_price'
        price = 'price'
        product_feed = 'product_feed'
        product_priority_0 = 'product_priority_0'
        product_priority_1 = 'product_priority_1'
        product_priority_2 = 'product_priority_2'
        product_priority_3 = 'product_priority_3'
        product_priority_4 = 'product_priority_4'
        sale_currency = 'sale_currency'
        sale_price = 'sale_price'
        sanitized_images = 'sanitized_images'
        sanitized_previews = 'sanitized_previews'
        start_date = 'start_date'
        state_of_vehicle = 'state_of_vehicle'
        stock_number = 'stock_number'
        tags = 'tags'
        term_length = 'term_length'
        term_qualifier = 'term_qualifier'
        title = 'title'
        transmission = 'transmission'
        trim = 'trim'
        unit_price = 'unit_price'
        url = 'url'
        url_shimmed = 'url_shimmed'
        validation_errors = 'validation_errors'
        vehicle_id = 'vehicle_id'
        vehicle_offer_id = 'vehicle_offer_id'
        vehicle_registration_plate = 'vehicle_registration_plate'
        vehicle_specifications = 'vehicle_specifications'
        vehicle_type = 'vehicle_type'
        videos_metadata = 'videos_metadata'
        vin = 'vin'
        visibility = 'visibility'
        year = 'year'

    class Availability:
        available = 'AVAILABLE'
        not_available = 'NOT_AVAILABLE'
        pending = 'PENDING'
        unknown = 'UNKNOWN'

    class AvailabilityCircleRadiusUnit:
        km = 'KM'
        mi = 'MI'

    class BodyStyle:
        convertible = 'CONVERTIBLE'
        coupe = 'COUPE'
        crossover = 'CROSSOVER'
        estate = 'ESTATE'
        grandtourer = 'GRANDTOURER'
        hatchback = 'HATCHBACK'
        minibus = 'MINIBUS'
        minivan = 'MINIVAN'
        mpv = 'MPV'
        none = 'NONE'
        other = 'OTHER'
        pickup = 'PICKUP'
        roadster = 'ROADSTER'
        saloon = 'SALOON'
        sedan = 'SEDAN'
        small_car = 'SMALL_CAR'
        sportscar = 'SPORTSCAR'
        supercar = 'SUPERCAR'
        supermini = 'SUPERMINI'
        suv = 'SUV'
        truck = 'TRUCK'
        van = 'VAN'
        wagon = 'WAGON'

    class Capabilities:
        b2c_marketplace = 'B2C_MARKETPLACE'
        c2c_marketplace = 'C2C_MARKETPLACE'
        da = 'DA'
        daily_deals = 'DAILY_DEALS'
        daily_deals_legacy = 'DAILY_DEALS_LEGACY'
        ig_product_tagging = 'IG_PRODUCT_TAGGING'
        marketplace = 'MARKETPLACE'
        marketplace_ads_deprecated = 'MARKETPLACE_ADS_DEPRECATED'
        marketplace_shops = 'MARKETPLACE_SHOPS'
        mini_shops = 'MINI_SHOPS'
        offline_conversions = 'OFFLINE_CONVERSIONS'
        shops = 'SHOPS'
        universal_checkout = 'UNIVERSAL_CHECKOUT'
        whatsapp = 'WHATSAPP'

    class CapabilitiesDisabledByUser:
        b2c_marketplace = 'B2C_MARKETPLACE'
        biz_msg_ai_agent = 'BIZ_MSG_AI_AGENT'
        business_inbox_in_messenger = 'BUSINESS_INBOX_IN_MESSENGER'
        buy_on_facebook = 'BUY_ON_FACEBOOK'
        c2c_marketplace = 'C2C_MARKETPLACE'
        cpas_parent_catalog = 'CPAS_PARENT_CATALOG'
        da = 'DA'
        daily_deals = 'DAILY_DEALS'
        daily_deals_legacy = 'DAILY_DEALS_LEGACY'
        event = 'EVENT'
        event_deprecated = 'EVENT_DEPRECATED'
        groups = 'GROUPS'
        ig_onsite_shopping = 'IG_ONSITE_SHOPPING'
        ig_product_tagging = 'IG_PRODUCT_TAGGING'
        ldp = 'LDP'
        marketplace = 'MARKETPLACE'
        marketplace_ads_deprecated = 'MARKETPLACE_ADS_DEPRECATED'
        marketplace_home_rentals = 'MARKETPLACE_HOME_RENTALS'
        marketplace_home_sales = 'MARKETPLACE_HOME_SALES'
        marketplace_motors = 'MARKETPLACE_MOTORS'
        marketplace_shops = 'MARKETPLACE_SHOPS'
        mini_shops = 'MINI_SHOPS'
        neighborhoods = 'NEIGHBORHOODS'
        offline_conversions = 'OFFLINE_CONVERSIONS'
        organic_discovery = 'ORGANIC_DISCOVERY'
        profile = 'PROFILE'
        service = 'SERVICE'
        shops = 'SHOPS'
        test_capability = 'TEST_CAPABILITY'
        universal_checkout = 'UNIVERSAL_CHECKOUT'
        us_marketplace = 'US_MARKETPLACE'
        whatsapp = 'WHATSAPP'
        whatsapp_marketing_message = 'WHATSAPP_MARKETING_MESSAGE'

    class CapabilitiesRenderingCatalogManager:
        b2c_marketplace = 'B2C_MARKETPLACE'
        c2c_marketplace = 'C2C_MARKETPLACE'
        da = 'DA'
        daily_deals = 'DAILY_DEALS'
        daily_deals_legacy = 'DAILY_DEALS_LEGACY'
        ig_product_tagging = 'IG_PRODUCT_TAGGING'
        marketplace = 'MARKETPLACE'
        marketplace_ads_deprecated = 'MARKETPLACE_ADS_DEPRECATED'
        marketplace_shops = 'MARKETPLACE_SHOPS'
        mini_shops = 'MINI_SHOPS'
        offline_conversions = 'OFFLINE_CONVERSIONS'
        shops = 'SHOPS'
        universal_checkout = 'UNIVERSAL_CHECKOUT'
        whatsapp = 'WHATSAPP'

    class Condition:
        excellent = 'EXCELLENT'
        fair = 'FAIR'
        good = 'GOOD'
        none = 'NONE'
        other = 'OTHER'
        poor = 'POOR'
        very_good = 'VERY_GOOD'

    class DealerCommunicationChannel:
        chat = 'CHAT'
        email_chat_proxy = 'EMAIL_CHAT_PROXY'
        lead_form = 'LEAD_FORM'
        unknown = 'UNKNOWN'

    class DisplayFormat:
        carousel_ad = 'CAROUSEL_AD'
        shops_pdp = 'SHOPS_PDP'
        single_ad = 'SINGLE_AD'

    class Drivetrain:
        awd = 'AWD'
        four_wd = 'FOUR_WD'
        fwd = 'FWD'
        none = 'NONE'
        other = 'OTHER'
        rwd = 'RWD'
        two_wd = 'TWO_WD'

    class FinanceType:
        hire_purchase = 'HIRE_PURCHASE'
        lease = 'LEASE'
        none = 'NONE'
        no_finance = 'NO_FINANCE'
        personal_contract_purchase = 'PERSONAL_CONTRACT_PURCHASE'

    class FuelType:
        diesel = 'DIESEL'
        electric = 'ELECTRIC'
        flex = 'FLEX'
        gasoline = 'GASOLINE'
        hybrid = 'HYBRID'
        none = 'NONE'
        other = 'OTHER'
        petrol = 'PETROL'
        plugin_hybrid = 'PLUGIN_HYBRID'

    class ImageFetchStatus:
        direct_upload = 'DIRECT_UPLOAD'
        fetched = 'FETCHED'
        fetch_failed = 'FETCH_FAILED'
        no_status = 'NO_STATUS'
        outdated = 'OUTDATED'
        partial_fetch = 'PARTIAL_FETCH'

    class OfferType:
        cash = 'CASH'
        finance = 'FINANCE'
        lease = 'LEASE'
        none = 'NONE'

    class StateOfVehicle:
        cpo = 'CPO'
        new = 'NEW'
        used = 'USED'

    class Transmission:
        automatic = 'AUTOMATIC'
        manual = 'MANUAL'
        none = 'NONE'
        other = 'OTHER'

    class VehicleType:
        boat = 'BOAT'
        car_truck = 'CAR_TRUCK'
        commercial = 'COMMERCIAL'
        motorcycle = 'MOTORCYCLE'
        other = 'OTHER'
        powersport = 'POWERSPORT'
        rv_camper = 'RV_CAMPER'
        trailer = 'TRAILER'

    class Visibility:
        active = 'ACTIVE'
        archived = 'ARCHIVED'
        hidden = 'HIDDEN'
        legacy_public = 'LEGACY_PUBLIC'
        published = 'PUBLISHED'
        staging = 'STAGING'
        visible_only_with_overrides = 'VISIBLE_ONLY_WITH_OVERRIDES'
        whitelist_only = 'WHITELIST_ONLY'

    _field_types = {
        'address': 'object',
        'amount_currency': 'string',
        'amount_percentage': 'float',
        'amount_price': 'string',
        'amount_qualifier': 'string',
        'applinks': 'object',
        'automotive_model_id': 'string',
        'availability': 'Availability',
        'availability_circle_radius': 'float',
        'availability_circle_radius_unit': 'AvailabilityCircleRadiusUnit',
        'body_style': 'BodyStyle',
        'capabilities': 'list<Capabilities>',
        'capabilities_disabled_by_user': 'list<CapabilitiesDisabledByUser>',
        'capabilities_rendering_catalog_manager': 'list<CapabilitiesRenderingCatalogManager>',
        'carfax_dealership_id': 'string',
        'channels_to_integrity_status': 'object',
        'comscore_market_codes': 'list<string>',
        'condition': 'Condition',
        'currency': 'string',
        'custom_label_0': 'string',
        'custom_label_1': 'string',
        'custom_label_2': 'string',
        'custom_label_3': 'string',
        'custom_label_4': 'string',
        'custom_number_0': 'int',
        'custom_number_1': 'int',
        'custom_number_2': 'int',
        'custom_number_3': 'int',
        'custom_number_4': 'int',
        'date_first_on_lot': 'string',
        'days_on_lot': 'int',
        'dealer_communication_channel': 'DealerCommunicationChannel',
        'dealer_email': 'string',
        'dealer_id': 'string',
        'dealer_name': 'string',
        'dealer_phone': 'string',
        'dealer_privacy_policy_url': 'string',
        'dealer_url': 'string',
        'default_country': 'string',
        'default_language_locale': 'string',
        'description': 'string',
        'downpayment_currency': 'string',
        'downpayment_price': 'string',
        'downpayment_qualifier': 'string',
        'drivetrain': 'Drivetrain',
        'enabled_capability_to_review_status': 'list<object>',
        'end_date': 'string',
        'engine_size': 'float',
        'exterior_color': 'string',
        'fb_page_id': 'object',
        'features': 'list<object>',
        'finance_description': 'string',
        'finance_type': 'FinanceType',
        'fuel_type': 'FuelType',
        'generation': 'string',
        'horse_power': 'int',
        'id': 'int',
        'image_fetch_status': 'ImageFetchStatus',
        'images': 'list<string>',
        'interior_color': 'string',
        'interior_upholstery': 'string',
        'is_blackholed': 'bool',
        'legal_disclosure_impressum_url': 'string',
        'make': 'string',
        'mileage': 'object',
        'model': 'string',
        'offer_description': 'string',
        'offer_disclaimer': 'string',
        'offer_disclaimer_url': 'string',
        'offer_type': 'OfferType',
        'previous_currency': 'string',
        'previous_price': 'string',
        'price': 'string',
        'product_feed': 'object',
        'product_priority_0': 'float',
        'product_priority_1': 'float',
        'product_priority_2': 'float',
        'product_priority_3': 'float',
        'product_priority_4': 'float',
        'sale_currency': 'string',
        'sale_price': 'string',
        'sanitized_images': 'list<string>',
        'sanitized_previews': 'list<string>',
        'start_date': 'string',
        'state_of_vehicle': 'StateOfVehicle',
        'stock_number': 'string',
        'tags': 'list<string>',
        'term_length': 'int',
        'term_qualifier': 'string',
        'title': 'string',
        'transmission': 'Transmission',
        'trim': 'string',
        'unit_price': 'object',
        'url': 'string',
        'url_shimmed': 'string',
        'validation_errors': 'object',
        'vehicle_id': 'string',
        'vehicle_offer_id': 'string',
        'vehicle_registration_plate': 'string',
        'vehicle_specifications': 'list<object>',
        'vehicle_type': 'VehicleType',
        'videos_metadata': 'object',
        'vin': 'string',
        'visibility': 'Visibility',
        'year': 'int',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['Availability'] = ProductCatalogAutomotiveItemGet.Availability.__dict__.values()
        field_enum_info['AvailabilityCircleRadiusUnit'] = ProductCatalogAutomotiveItemGet.AvailabilityCircleRadiusUnit.__dict__.values()
        field_enum_info['BodyStyle'] = ProductCatalogAutomotiveItemGet.BodyStyle.__dict__.values()
        field_enum_info['Capabilities'] = ProductCatalogAutomotiveItemGet.Capabilities.__dict__.values()
        field_enum_info['CapabilitiesDisabledByUser'] = ProductCatalogAutomotiveItemGet.CapabilitiesDisabledByUser.__dict__.values()
        field_enum_info['CapabilitiesRenderingCatalogManager'] = ProductCatalogAutomotiveItemGet.CapabilitiesRenderingCatalogManager.__dict__.values()
        field_enum_info['Condition'] = ProductCatalogAutomotiveItemGet.Condition.__dict__.values()
        field_enum_info['DealerCommunicationChannel'] = ProductCatalogAutomotiveItemGet.DealerCommunicationChannel.__dict__.values()
        field_enum_info['DisplayFormat'] = ProductCatalogAutomotiveItemGet.DisplayFormat.__dict__.values()
        field_enum_info['Drivetrain'] = ProductCatalogAutomotiveItemGet.Drivetrain.__dict__.values()
        field_enum_info['FinanceType'] = ProductCatalogAutomotiveItemGet.FinanceType.__dict__.values()
        field_enum_info['FuelType'] = ProductCatalogAutomotiveItemGet.FuelType.__dict__.values()
        field_enum_info['ImageFetchStatus'] = ProductCatalogAutomotiveItemGet.ImageFetchStatus.__dict__.values()
        field_enum_info['OfferType'] = ProductCatalogAutomotiveItemGet.OfferType.__dict__.values()
        field_enum_info['StateOfVehicle'] = ProductCatalogAutomotiveItemGet.StateOfVehicle.__dict__.values()
        field_enum_info['Transmission'] = ProductCatalogAutomotiveItemGet.Transmission.__dict__.values()
        field_enum_info['VehicleType'] = ProductCatalogAutomotiveItemGet.VehicleType.__dict__.values()
        field_enum_info['Visibility'] = ProductCatalogAutomotiveItemGet.Visibility.__dict__.values()
        return field_enum_info


