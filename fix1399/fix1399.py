# coding=utf-8

from __future__ import unicode_literals, absolute_import, division, print_function

import sopel


def configure(config):
    pass


def setup(bot):
    global interval_count
    interval_count = 0


@sopel.module.commands('simple')
def simple_callable(bot, trigger, extra='A'):
    bot.say('extra: {}'.format(extra))

@sopel.module.commands('simple2')
def simple_callable2(bot, trigger, extra='2'):
    bot.say('extra: {}'.format(extra))


# @sopel.module.interval(1)
# def interval_callable(bot, extra='a'):
#     global interval_count
#     interval_count += 1
#     bot.say('extra: {}; count: {}'.format(extra, interval_count), '#sopel-dev')