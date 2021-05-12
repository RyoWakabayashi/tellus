# pylint: disable=invalid-name
# -*- coding: utf-8 -*-
"""
TelluSAR
"""


from tellus.tellus import Tellus

API_ROOT = "https://tellusar.tellusxdp.com/api/v1"


class TelluSAR(Tellus):
    """
    TelluSAR
    """

    def __init__(self, api_token):
        super().__init__(api_token)
        self.auth()

    def auth(self):
        """
        Authenticate
        """
        self.auth_v1("tellus-product", "tellusar-api-f")

    def get_free_scene(self):
        """
        Get free scene
        """
        url = f"{API_ROOT}/search"
        return self.get(url)

    def get_scene_after(self, scene_id):
        """
        Get free scene after ID
        Args:
            scene_id: str : Scene ID
        """
        url = f"{API_ROOT}/search/{scene_id}/afters"
        return self.get(url)

    def request_work(self, before_scene_id, after_scene_id, polarisation):
        """
        Request work
        Args:
            before_scene_id: str : Before Scene ID
            after_scene_id: str : After Scene ID
            polarisation: str : Polarisation
        """
        url = f"{API_ROOT}/works"
        payload = {
            "before_scene_id": before_scene_id,
            "after_scene_id": after_scene_id,
            "polarisation": polarisation,
            "nlook_rg": 5,
            "nlook_az": 7,
            "filter": 0,
        }
        return self.get(url, payload)

    def get_work_list(self):
        """
        Get work list
        """
        url = f"{API_ROOT}/works"
        return self.get(url)

    def get_work(self, work_id):
        """
        Get work
        Args:
            work_id: str : Work ID
        """
        url = f"{API_ROOT}/works/{work_id}"
        return self.get(url)

    def download(
        self, name, work_id, z, x, y
    ):  # pylint: disable=invalid-name,too-many-arguments
        """
        Download
        Args:
            name: str : Output file name
            work_id: str : Work ID
            z: int : Zoom
            x: int : X-coordinate
            y: int : Y-coordinate
        """
        url = f"{API_ROOT}/works/{work_id}/pngs/fringe_diffs/{z}/{x}/{y}.png"
        data = self.get_file(url)
        with open(name, "wb") as file:
            file.write(data)
