# coding=utf-8
from __future__ import absolute_import, unicode_literals

import sopel

__all__ = [
    'interval_callable'
]

global interval_count
interval_count = 0


@sopel.module.interval(1)
def interval_callable(bot, extra='a'):
    global interval_count
    interval_count += 1
    bot.say('extra: {}; count: {}'.format(extra, interval_count), '#sopel-dev')