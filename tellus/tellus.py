# -*- coding: utf-8 -*-
"""
Tellus
"""

import datetime
import json

import requests


class Tellus:
    """
    Tellus
    """

    api_token = ""
    market_token = ""

    def __init__(self, api_token):
        self.api_token = api_token

    def _get(self, url, payload={}):  # pylint: disable=dangerous-default-value
        headers = {"Authorization": "Bearer " + self.market_token}
        response = requests.get(url, headers=headers, params=payload)
        if response.status_code != 200:
            print(response.content)
            return None
        return response.content

    def _auth(self, url, payload={}):  # pylint: disable=dangerous-default-value
        headers = {
            "Authorization": "Bearer " + self.api_token,
            "Content-type": "application/json",
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code != 200:
            print(response.content)
            return
        res = json.loads(response.content)
        self.market_token = res["token"]

    def auth_v2(self, product_id):
        """
        Authenticate for API Version 2
        Args:
            product_id: str : Product ID
        """
        url = "https://www.tellusxdp.com/api/manager/v2/auth/token/"
        payload = {"product_id": product_id}
        self._auth(url, payload)

    def auth_v1(self, provider_id, tool_label, expiration=5):
        """
        Authenticate for API Version 1
        Args:
            provider_id: str : Provider ID
            tool_label: str : Tool label
            expiration: str : expiration minutes
        """
        url = "https://sdk.tellusxdp.com/api/manager/v1/auth/api_access_token/token"
        expires_at = (
            datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9)))
            + datetime.timedelta(minutes=expiration)
        ).isoformat()
        payload = {
            "provider_id": provider_id,
            "tool_label": tool_label,
            "expires_at": expires_at,
        }
        self._auth(url, payload)

    def get(self, url, payload={}):  # pylint: disable=dangerous-default-value
        """
        Request GET
        Args:
            url: str : API URL
            payload: dict : Request payload
        """
        return json.loads(self._get(url, payload))

    def get_file(self, url, payload={}):  # pylint: disable=dangerous-default-value
        """
        Request GET for file
        Args:
            url: str : API URL
            payload: dict : Request payload
        """
        return self._get(url, payload)
