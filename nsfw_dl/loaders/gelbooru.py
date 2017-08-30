"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom


class GelbooruRandom(GenericRandom):
    """
    Gets a random image from gelbooru.
    """
    reqtype = "get"
    data_format = "bs4/html"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://www.gelbooru.com/index.php?page=post&s=random", {}, {}