import urllib.request

import json

class Connection:

    def __init__(self, host):

        self._host = host

        self._series = []

    def get(self, url, username=None, password=None):

        return self.__open(url, username=username, password=password)

    def __open(

        self,

        url,

        method=GET,

        headers=None,

        params=None,

        baseurl="",

        decode_json=True,

        auth=None,

        username=None,

        password=None,

    ):

        if username is not None:

            auth = urllib.request.HTTPDigestAuthHandler()

            auth.add_password(realm=None, uri=url, user=username, passwd=password)

        LOGGER.debug("URL: %s", url)

        try:

            opener = urllib.request.build_opener(urllib.request.HTTPSHandler())

            urllib.request.install_opener(opener)

            req = urllib.request.Request(url)

            if headers is not None:

                for key, value in headers.items():

                    req.add_header(key, value)

            if params is not None:

                req.data = urllib.parse.urlencode(params).encode('utf-8')

            resp = urllib.request.urlopen(req)

            if decode_json:

                return json.loads(resp.read().decode('utf-8'))

            return resp

        except urllib.error.HTTPError as e:

            LOGGER.debug(e.__doc__.strip())

            raise e

