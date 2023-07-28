from rapid7.api import API


# STRUCTURES
from rapid7.endpoints.structures import (
    SearchObject,
    SortObject,
    Indicators,
    CommunityThreat,
    Assignee,
)


class Endpoint(API):
    def __init__(self, api_key : str, region : str) -> None:
        super().__init__(api_key, region)
        return
    

    # ACCOUNTS
    from rapid7.endpoints._accounts import search_accounts
    from rapid7.endpoints._accounts import get_account_by_rrn


    # ASSETS
    from rapid7.endpoints._assets import search_assets
    from rapid7.endpoints._assets import get_asset_by_rrn


    # ATTACHMENTS
    from rapid7.endpoints._attachments import list_attachments
    from rapid7.endpoints._attachments import upload_attachments
    from rapid7.endpoints._attachments import download_attachment
    from rapid7.endpoints._attachments import delete_attachment
    from rapid7.endpoints._attachments import get_attachment_information


    # COMMENTS
    from rapid7.endpoints._comments import list_comments
    from rapid7.endpoints._comments import create_comment
    from rapid7.endpoints._comments import delete_comment


    # COMMUNITY THREATS
    from rapid7.endpoints._community_threats import create_community_threat
    from rapid7.endpoints._community_threats import delete_community_threat
    from rapid7.endpoints._community_threats import add_indicators_to_community_threat
    from rapid7.endpoints._community_threats import replace_indicators_to_community_threat


    # INVESTIGATIONS
    from rapid7.endpoints._investigations import list_investigations_v1
    from rapid7.endpoints._investigations import list_investigations_v2
    from rapid7.endpoints._investigations import close_investigations_in_bulk_v1
    from rapid7.endpoints._investigations import close_investigations_in_bulk_v2
    from rapid7.endpoints._investigations import assign_user_to_investigation
    from rapid7.endpoints._investigations import set_investigation_status_v1
    from rapid7.endpoints._investigations import set_investigation_status_v2
    from rapid7.endpoints._investigations import create_investigation
    from rapid7.endpoints._investigations import search_investigations
    from rapid7.endpoints._investigations import list_alerts_associated_with_investigation
    from rapid7.endpoints._investigations import get_rapid7_product_alerts_associated_with_investigation
    from rapid7.endpoints._investigations import get_investigation
    from rapid7.endpoints._investigations import update_investigation
    from rapid7.endpoints._investigations import assign_user_to_investigation
    from rapid7.endpoints._investigations import set_investigation_disposition
    from rapid7.endpoints._investigations import set_investigation_priority

 
    # LOCAL ACCOUNTS
    from rapid7.endpoints._local_accounts import search_local_accounts
    from rapid7.endpoints._local_accounts import get_local_account_by_rrn

    
    # USERS
    from rapid7.endpoints._users import search_user
    from rapid7.endpoints._users import get_user_by_rrn
