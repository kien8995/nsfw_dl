"""
Read the license at:
https://github.com/AraHaan/nsfw_dl/blob/master/LICENSE
"""
from ..generic import GenericSearch


class LolibooruSearch(GenericSearch):
    """
    Gets a random image with a specific tag from lolibooru.
    """
    reqtype = "get"
    data_format = "json"

    @staticmethod
    def prepare_url(args):
        """
        prepares the request url.
        """
        return f"https://lolibooru.moe/post/index.json?tags={args}", {}, {}
