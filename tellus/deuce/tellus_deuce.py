# -*- coding: utf-8 -*-
"""
Tellus DEUCE
"""


from tellus.tellus import Tellus

API_ROOT = "https://deuce.tellusxdp.com/api/v1"


class TellusDEUCE(Tellus):
    """
    Tellus DEUCE
    """

    def __init__(self, api_token):
        super().__init__(api_token)
        self.auth()

    def auth(self):
        """
        Authenticate
        """
        self.auth_v2("2f443df3-3355-4232-99bc-01dbe5dc6ca3")
        return

    def search(  # pylint: disable=too-many-arguments
        self, satellite, left_bottom_lat, left_bottom_lon, right_top_lat, right_top_lon
    ):
        """
        Search
        """
        url = f"{API_ROOT}/{satellite}/search?"
        url += f"left_bottom_lat={left_bottom_lat}&left_bottom_lon={left_bottom_lon}"
        url += f"&right_top_lat={right_top_lat}&right_top_lon={right_top_lon}"
        return self.get(url)

    def difference(  # pylint: disable=too-many-arguments
        self,
        satellite,
        left_bottom_lat,
        left_bottom_lon,
        right_top_lat,
        right_top_lon,
        scene_id_a,
        scene_id_b,
    ):
        """
        Get difference
        """
        url = f"{API_ROOT}/{satellite}/difference/scene_id?"
        url += f"left_bottom_lat={left_bottom_lat}&left_bottom_lon={left_bottom_lon}&"
        url += f"right_top_lat={right_top_lat}&right_top_lon={right_top_lon}&"
        url += f"scene_id_a={scene_id_a}&scene_id_b={scene_id_b}"
        return self.get(url)

    def get_work_list(self):
        """
        Get work list
        """
        url = f"{API_ROOT}/works"
        return self.get(url)

    def get_work(self, access_key):
        """
        Get work
        Args:
            access_key: str : Access key
        """
        url = f"{API_ROOT}/work/{access_key}"
        return self.get(url)

    def download(self, name, access_key, tiff_type):
        """
        Download
        Args:
            name: str : Output file name
            access_key: str : Access key
            tiff_type: str : base or cmap
        """
        url = f"{API_ROOT}/{access_key}/image/{tiff_type}.tiff"
        data = self.get_file(url)
        with open(name, "wb") as file:
            file.write(data)
