# -*- coding: utf-8 -*-

import enum
import logging
import math
import os
import random


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler("arithmetic.log")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

mark_c = "✔"
mark_w = "✘"

layout_2oprd = "%2s.   %2s %s %2s = %-3s  -> "
layout_2oprd_v = "%2s.       %2s\n%8s  %2s\n      ――――――――\n%12s  -> "
layout_2oprd_log = "%2s   %2s %s %2s = %-3s "
layout_mark = "%27s"

index = 0

min_default = 0
max_default = 20

formula_01 = [(min_default, max_default), '+', (min_default, max_default)]
formula_02 = [(min_default, max_default), '-', (min_default, max_default)]
formula_03 = [(min_default, max_default), '', (min_default, max_default)]
formula_04 = [(min_default, max_default), '+', (min_default, max_default),
              '+', (min_default, max_default)]
formula_05 = [(min_default, max_default), '+', (min_default, max_default),
              '-', (min_default, max_default)]
formula_06 = [(min_default, max_default), '-', (min_default, max_default),
              '+', (min_default, max_default)]
formula_07 = [(min_default, max_default), '-', (min_default, max_default),
              '-', (min_default, max_default)]
formula_08 = [(min_default, max_default), '', (min_default, max_default),
              '+', (min_default, max_default)]
formula_09 = [(min_default, max_default), '', (min_default, max_default),
              '-', (min_default, max_default)]
formula_10 = [(min_default, max_default), '', (min_default, max_default),
              '', (min_default, max_default)]

qpos_1 = 1
qpos_2 = 2
qpos_3 = 3
qpos_4 = 4
qpos_5 = 5
qpos_6 = 6


def reset_index():
    global index
    index = 0


def inc_index():
    global index
    index += 1


def index_less_than(count):
    global index
    return index < count
