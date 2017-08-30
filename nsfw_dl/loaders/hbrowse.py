"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericRandom


class HbrowseRandom(GenericRandom):
    """
    Gets a random image from hbrowse.
    """
    reqtype = "get"
    data_format = "aiohttp/url"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return "http://www.hbrowse.com/random", {}, {}
