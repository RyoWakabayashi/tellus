# -*- coding: utf-8 -*-
"""
TelluSAR client
"""


from tellus.sar.tellusar import TelluSAR


class Client:
    """
    TelluSAR client
    """

    def __init__(self, token):
        self.tellus = TelluSAR(token)

    def get_free(self):
        """
        Get free scene
        """
        scene_list = self.tellus.get_free_scene()
        for scene in scene_list["data"]["scenes"]:
            print(
                scene["scene_id"], scene["observation_datetime"], scene["polarisations"]
            )

    def get_after(self, scene_id):
        """
        Get free scene after ID
        Args:
            scene_id: str : Scene ID
        """
        scene_list = self.tellus.get_scene_after(scene_id)
        for scene in scene_list["data"]["scenes"]:
            print(
                scene["scene_id"], scene["observation_datetime"], scene["polarisations"]
            )

    def request(self, before, after, polarisation):
        """
        Request work
        Args:
            before_scene_id: str : Before Scene ID
            after_scene_id: str : After Scene ID
            polarisation: str : Polarisation
        """
        work_result = self.tellus.request_work(before, after, polarisation)
        works = work_result["data"]["works"]
        for work in works:
            print(work["work_id"], work["complete_date"])

    def get_work_list(self):
        """
        Get work list
        """
        work_result = self.tellus.get_work_list()
        works = work_result["data"]["works"]
        for work in works:
            print(work["work_id"], work["complete_date"])

    def get_work(self, work_id):
        """
        Get work
        Args:
            work_id: str : Work ID
        """
        work_result = self.tellus.get_work(work_id)
        work = work_result["data"]
        print(work["work_id"], work["complete_date"])

    def download(
        self, output, work_id, z, x, y
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
        self.tellus.download(output, work_id, z, x, y)
