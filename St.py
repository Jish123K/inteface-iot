import aiohttp

import requests

class Iotainterface:

    def __init__(self, ip_addr, username, password):

        self._ip_addr = ip_addr

        self._username = username

        self._password = password

        self._session = requests.Session()

    async def get(self, path, params=None):

        url = f"http://{self._ip_addr}/{path}"

        auth = aiohttp.BasicAuth(self._username, self._password)

        async with aiohttp.ClientSession(auth=auth) as session:

            async with session.get(url, params=params) as response:

                response.raise_for_status()

                return await response.json()

    async def post(self, path, data=None):

        url = f"http://{self._ip_addr}/{path}"

        auth = aiohttp.BasicAuth(self._username, self._password)

        async with aiohttp.ClientSession(auth=auth) as session:

            async with session.post(url, json=data) as response:

                response.raise_for_status()

                from distutils.core import setup

setup(

    name="iotainterfacepy",

    version="0.1.0",

    author="Your Name",

    author_email="your.email@example.com",

    description="Python library for the IoTaWatt Energy device",

    url="https://github.com/your_username/iotainterfacepy",

    packages=["iotainterfacepy"],

    install_requires=["aiohttp", "requests"],

    python_requires=">=3.8",

)
                return await response.json()
