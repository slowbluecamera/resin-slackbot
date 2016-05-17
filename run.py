#!/usr/bin/env python

import os
import sys
import logging
from slackbot.bot import Bot

def main():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    sys.path.append("plugins")

    if 'SLACKBOT_API_TOKEN' not in os.environ:
        print "'SLACKBOT_API_TOKEN' environment variable not set. Exiting..."
        exit(1)

    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
