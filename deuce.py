# -*- coding: utf-8 -*-
"""
TellusDEUCE client tool
"""

from argparse import ArgumentParser

from tellus.deuce.client import Client as Deuce
from utils import get_token


def parse_args():
    """
    Parse command line arguments
    Returns:
        parsed arguments
    """

    usage = "python deuce.py get_work_list"
    parser = ArgumentParser(usage=usage)
    parser.add_argument(
        "operation",
        choices=["search", "request", "get_work_list", "get_work", "download"],
    )
    parser.add_argument("-t", "--token", required=False, help="API Token")
    parser.add_argument(
        "-s", "--satellite", required=False, default="", help="Satellite"
    )
    parser.add_argument(
        "-lblat",
        "--left_bottom_lat",
        required=False,
        default="",
        help="Left bottom latitude",
    )
    parser.add_argument(
        "-lblon",
        "--left_bottom_lon",
        required=False,
        default="",
        help="Left bottom longitude",
    )
    parser.add_argument(
        "-rtlat",
        "--right_top_lat",
        required=False,
        default="",
        help="Right top latitude",
    )
    parser.add_argument(
        "-rtlon",
        "--right_top_lon",
        required=False,
        default="",
        help="Right top longitude",
    )
    parser.add_argument(
        "-a", "--scene_id_a", required=False, default="", help="Scene ID A"
    )
    parser.add_argument(
        "-b", "--scene_id_b", required=False, default="", help="Scene ID B"
    )
    parser.add_argument(
        "-k", "--access_key", required=False, default="", help="Access key"
    )
    parser.add_argument(
        "-o", "--output", required=False, default="", help="Output file path"
    )
    parser.add_argument(
        "--tiff_type",
        required=False,
        default="cmap",
        choices=["base", "cmap"],
        help="TIFF Type",
    )
    return parser.parse_args()


def main(args):
    """Tellus DEUCE"""
    token = get_token(args)
    if token == "":
        return
    client = Deuce(token)

    if args.operation == "search":
        client.search(
            args.satellite,
            args.left_bottom_lat,
            args.left_bottom_lon,
            args.right_top_lat,
            args.right_top_lon,
        )
    elif args.operation == "request":
        client.request(
            args.satellite,
            args.left_bottom_lat,
            args.left_bottom_lon,
            args.right_top_lat,
            args.right_top_lon,
            args.scene_id_a,
            args.scene_id_b,
        )
    elif args.operation == "get_work_list":
        client.get_work_list()
    elif args.operation == "get_work":
        client.get_work(args.access_key)
    elif args.operation == "download":
        client.download(args.output, args.access_key, args.tiff_type)


if __name__ == "__main__":
    main(parse_args())
