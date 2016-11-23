# -*- coding: utf-8 -*-

import random
import math
import os
import logging


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

layout = "%2s.   %2s %s %2s = %-3s  -> "
layout_v = "%2s.       %2s\n%8s  %2s\n      ――――――――\n%12s  -> "
layout_l = "%2s   %2s %s %2s = %-3s "
layout_mark = "%27s"

index = 0


def reset_index():
    global index
    index = 0


def inc_index():
    global index
    index += 1


def index_less_than(count):
    global index
    return index < count


def add_from(frm=10, count=20, complement=False, vertical=False):
    os.system('clear')
    generate(
        min_op1=frm, max_op1=frm,
        count=count, op="+", complement=complement, vertical=vertical)


def add_within(within=10, count=20, complement=False, vertical=False):
    os.system('clear')
    generate(
        min_op1=0, max_op1=within, min_op2=0, max_op2=within,
        count=count, op="+", complement=complement, vertical=vertical)


def add_to(to=10, count=20, complement=False, vertical=False):
    os.system('clear')
    reset_index()
    logger.info(
        "add_to begins with min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
        "op=%s,count=%s,complement=%s,vertical=%s" %
        (0, to, 0, to, "-", count, complement, vertical))
    op1 = range(0, to + 1)
    op2 = range(0, to + 1)
    while (index_less_than(count)):
        i1 = int(math.floor(random.random() * len(op1)))
        i2 = int(math.floor(random.random() * len(op2)))
        if op1[i1] + op2[i2] == to:
            try:
                do_print(op="+", op1=op1[i1], op2=op2[i2],
                         complement=complement, vertical=vertical)
            except KeyboardInterrupt:
                logger.info(
                    "add_to cancelled with "
                    "min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
                    "op=%s,count=%s,complement=%s,vertical=%s" %
                    (0, to, 0, to, "-", count, complement, vertical))
                return
    logger.info(
        "add_to ends with min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
        "op=%s,count=%s,complement=%s,vertical=%s" %
        (0, to, 0, to, "-", count, complement, vertical))


def sub_from(frm=10, count=20, complement=False, vertical=False):
    os.system('clear')
    generate(
        min_op1=frm, max_op1=frm,
        count=count, op="-", complement=complement, vertical=vertical)


def sub_within(within=10, count=20, complement=False, vertical=False):
    os.system('clear')
    generate(
        min_op1=0, max_op1=within, min_op2=0, max_op2=within,
        count=count, op="-", complement=complement, vertical=vertical)


def sub_to(to=9, min_op1=0, max_op1=20, min_op2=0, max_op2=20,
           count=20, complement=False, vertical=False):
    os.system('clear')
    reset_index()
    logger.info(
        "sub_to begins with min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
        "op=%s,count=%s,complement=%s,vertical=%s" %
        (min_op1, max_op1, min_op2, max_op2,
         "-", count, complement, vertical))
    op1 = range(0, max_op1 + 1)
    op2 = range(0, max_op2 + 1)
    while (index_less_than(count)):
        i1 = int(math.floor(random.random() * len(op1)))
        i2 = int(math.floor(random.random() * len(op2)))
        if op1[i1] - op2[i2] == to:
            try:
                do_print(op="-", op1=op1[i1], op2=op2[i2],
                         complement=complement, vertical=vertical)
            except KeyboardInterrupt:
                logger.info(
                    "sub_to cancelled with "
                    "min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
                    "op=%s,count=%s,complement=%s,vertical=%s" %
                    (min_op1, max_op1, min_op2, max_op2,
                     "-", count, complement, vertical))
                return
    logger.info(
        "sub_to ends with min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
        "op=%s,count=%s,complement=%s,vertical=%s" %
        (min_op1, max_op1, min_op2, max_op2,
         "-", count, complement, vertical))


def generate(min_op1=0, max_op1=20, min_op2=0, max_op2=20,
             count=20, op="", complement=False, vertical=False):
    os.system('clear')
    reset_index()
    logger.info(
        "generate begins with "
        "min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
        "op=%s,count=%s,complement=%s,vertical=%s" %
        (min_op1, max_op1, min_op2, max_op2,
         "-", count, complement, vertical))
    op1 = range(min_op1, max_op1 + 1)
    op2 = range(min_op2, max_op2 + 1)
    while (index_less_than(count)):
        i1 = int(math.floor(random.random() * len(op1)))
        i2 = int(math.floor(random.random() * len(op2)))
        try:
            do_print(op=op, op1=op1[i1], op2=op2[i2],
                     complement=complement, vertical=vertical)
        except KeyboardInterrupt:
            logger.info(
                "generate cancelled with "
                "min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
                "op=%s,count=%s,complement=%s,vertical=%s" %
                (min_op1, max_op1, min_op2, max_op2,
                 "-", count, complement, vertical))
            return
    logger.info(
        "generate ends with "
        "min_op1=%s,max_op1=%s,min_op2=%s,max_op2=%s,"
        "op=%s,count=%s,complement=%s,vertical=%s" %
        (min_op1, max_op1, min_op2, max_op2,
         "-", count, complement, vertical))


def do_print(op, op1, op2, complement=False, vertical=False):
    result = "?"
    if op == "+":
        inc_index()
        expected = op1 + op2
        reply(expected,
              layout if not vertical else layout_v,
              (index, op1, op, op2, result))
        if complement is True:
            inc_index()
            result = op1 + op2
            if random.random() > 0.5:
                expected = op1
                op1 = "?"
            else:
                expected = op2
                op2 = "?"
            reply(expected,
                  layout if not vertical else layout_v,
                  (index, op1, op, op2, result))
    elif op == "-":
        if op1 >= op2:
            inc_index()
            expected = op1 - op2
            reply(expected,
                  layout if not vertical else layout_v,
                  (index, op1, op, op2, result))
            if complement is True:
                inc_index()
                result = op1 - op2
                if random.random() > 0.5:
                    expected = op1
                    op1 = "?"
                else:
                    expected = op2
                    op2 = "?"
                reply(expected,
                      layout if not vertical else layout_v,
                      (index, op1, op, op2, result))
    else:
        if random.random() > 0.5:
            do_print("+", op1, op2, complement, vertical=vertical)
        else:
            do_print("-", op1, op2, complement, vertical=vertical)


def reply(expected, layout, values):
    logger.info("formula " + layout_l % values + " begins")
    actual = raw_input(layout % values)
    if not actual.isdigit():
        logger.info("formula " + layout_l % values +
                    " ends with error: " + actual)
        print layout_mark % mark_w
        return
    if expected == int(actual):
        logger.info("formula " + layout_l % values + " ends")
        print layout_mark % mark_c
    else:
        logger.info("formula " + layout_l % values +
                    " ends with error: " + actual)
        print layout_mark % mark_w
