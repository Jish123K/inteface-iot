import argparse

import asyncio

import logging

import sys

import time

import aiohttp

import aiofiles

LOOP = asyncio.get_event_loop()

logging.basicConfig(level="DEBUG")

class Tester:

    def __init__(self, ip_addr, username, password):

        self._ip_addr = ip_addr

        self._username = username

        self._password = password

    async def run(self):

        try:

            async with aiohttp.ClientSession() as session:

                self.iotawatt = Iotawatt(

                    "iotawatt", self._ip_addr, session, self._username, self._password

                )

                await self.iotawatt.connect()

        except aiohttp.ClientError as err:

            logging.error("%s", err)

            return

        while True:

            logging.info("=============================================")

            await self.iotawatt.update()

            logging.info("=============================================")

            await asyncio.sleep(5)

def main(argv):

    my_parser = argparse.ArgumentParser(description="Run the IoTaWatt tester")

    my_parser.add_argument(

        "IPAddress", metavar="IP Address", type=str, help="IP Address of IoTaWatt"

    )

    my_parser.add_argument("-u", metavar="Username", type=str, help="Username")

    my_parser.add_argument("-p", metavar="Password", type=str, help="Password")

    args = my_parser.parse_args()

    logging.info("Started")

    test = Tester(args.IPAddress, args.u, args.p)

    LOOP.run_until_complete(test.run())

if __name__ == "__main__":

    main(sys.argv[1:])

