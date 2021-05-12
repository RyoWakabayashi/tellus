# -*- coding: utf-8 -*-
"""
TelluSAR client tool
"""

from argparse import ArgumentParser

from tellus.sar.client import Client as Sar
from utils import get_token


def parse_args():
    """
    Parse command line arguments
    Returns:
        Parsed arguments
    """

    usage = "python tellusar.py get_work_list"
    parser = ArgumentParser(usage=usage)
    parser.add_argument(
        "operation",
        choices=[
            "get_free",
            "get_after",
            "request",
            "get_work_list",
            "get_work",
            "download",
        ],
    )
    parser.add_argument("-t", "--token", required=False, help="API Token")
    parser.add_argument("-s", "--scene_id", required=False, default="", help="Scene ID")
    parser.add_argument("-w", "--work_id", required=False, default="", help="Work ID")
    parser.add_argument(
        "-b", "--before", required=False, default="", help="Before Scene ID"
    )
    parser.add_argument(
        "-a", "--after", required=False, default="", help="After Scene ID"
    )
    parser.add_argument(
        "-p", "--polarisation", required=False, default="", help="Polarisation"
    )
    parser.add_argument(
        "-o", "--output", required=False, default="", help="Output file path"
    )
    parser.add_argument("-z", "--zoom", required=False, default="", help="Zoom")
    parser.add_argument("-x", required=False, default="", help="X-coordinate")
    parser.add_argument("-y", required=False, default="", help="Y-coordinate")
    return parser.parse_args()


def main(args):
    """TelluSAR"""
    token = get_token(args)
    if token == "":
        return
    client = Sar(token)

    if args.operation == "get_free":
        client.get_free()
    elif args.operation == "get_after":
        client.get_after(args.scene_id)
    elif args.operation == "request":
        client.request(args.before, args.after, args.polarisation)
    elif args.operation == "get_work_list":
        client.get_work_list()
    elif args.operation == "get_work":
        client.get_work(args.work_id)
    elif args.operation == "download":
        client.download(args.output, args.work_id, args.z, args.x, args.y)


if __name__ == "__main__":
    main(parse_args())
