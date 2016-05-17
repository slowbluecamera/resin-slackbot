# -*- coding: utf-8 -*-

import re
import logging
from slackbot.bot import respond_to
from slackbot.bot import listen_to

logger = logging.getLogger(__name__)

@respond_to('Hello, world.$', re.IGNORECASE)
def hello_reply(message):
    logger.info('hello_reply()')
    message.reply('Hello yourself!')
    message.react('robot_face')

@listen_to('Hello, world.$')
def hello_send(message):
    logger.info('hello_send()')
    message.send('Hello everyone!')
    message.react('eggplant')
