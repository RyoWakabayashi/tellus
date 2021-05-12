import os


def get_token(args):
    """
    Parse command line arguments
    Args:
        args: object : Parsed arguments
    Returns:
        Tellus API token
    """
    if args.token is not None:
        return args.token

    if "TELLUS_API_TOKEN" in os.environ:
        return os.environ["TELLUS_API_TOKEN"]

    print(
        "Please set your API token in option '-t <API_TOKEN>' "
        + "or environment variable TELLUS_API_TOKEN"
    )
    return ""
