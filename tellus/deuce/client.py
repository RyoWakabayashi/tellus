# -*- coding: utf-8 -*-
"""
Tellus DEUCE client
"""


from tellus.deuce.tellus_deuce import TellusDEUCE


class Client:
    """
    Tellus DEUCE client
    """

    def __init__(self, token):
        self.tellus = TellusDEUCE(token)

    def search(  # pylint: disable=too-many-arguments
        self, satellite, left_bottom_lat, left_bottom_lon, right_top_lat, right_top_lon
    ):
        """
        Search
        """
        executed = self.tellus.search(
            satellite, left_bottom_lat, left_bottom_lon, right_top_lat, right_top_lon
        )
        for scene in executed["scenes"]:
            print(scene["dataset_id"], scene["observation_datetime"])

    def request(  # pylint: disable=too-many-arguments
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
        difference_data = self.tellus.difference(
            satellite,
            left_bottom_lat,
            left_bottom_lon,
            right_top_lat,
            right_top_lon,
            scene_id_a,
            scene_id_b,
        )
        access_key = difference_data["access_key"]
        print(access_key)

    def get_work_list(self):
        """
        Get work list
        """
        work_list = self.tellus.get_work_list()
        for work in work_list:
            print(work["access_key"], work["status"])

    def get_work(self, access_key):
        """
        Get work
        Args:
            access_key: str : Access key
        """
        work = self.tellus.get_work(access_key)
        print(work["status"])

    def download(self, output, access_key, tiff_type):
        """
        Download
        Args:
            name: str : Output file name
            access_key: str : Access key
            tiff_type: str : base or cmap
        """
        work = self.tellus.get_work(access_key)
        if work["status"] != "complete":
            print("Not completed")
            return
        self.tellus.download(output, access_key, tiff_type)
