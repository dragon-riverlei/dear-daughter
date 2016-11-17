# -*- coding: utf-8 -*-

import random
import math
import os

mark_c = "✔"
mark_w = "✘"

layout = "%2s.   %2s %s %2s = %-3s  -> "
layout_mark = "%27s"
layout_v = "%2s.       %2s\n%8s  %2s\n      ――――――――\n%12s  -> "
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
        min_op1=frm, max_op1=frm, min_op2=0, max_op2=frm,
        count=count, op="+", complement=complement, vertical=vertical)


def add_within(within=10, count=20, complement=False, vertical=False):
    os.system('clear')
    generate(
        min_op1=0, max_op1=within, min_op2=0, max_op2=within,
        count=count, op="+", complement=complement, vertical=vertical)


def add_to(to=10, count=20, complement=False, vertical=False):
    os.system('clear')
    reset_index()
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
                return


def sub_from(frm=10, count=20, complement=False, vertical=False):
    os.system('clear')
    generate(
        min_op1=frm, max_op1=frm, min_op2=0, max_op2=frm,
        count=count, op="-", complement=complement, vertical=vertical)


def sub_within(within=10, count=20, complement=False, vertical=False):
    os.system('clear')
    generate(
        min_op1=0, max_op1=within, min_op2=0, max_op2=within,
        count=count, op="-", complement=complement, vertical=vertical)


def sub_to(to=9, count=20, complement=False, vertical=False):
    os.system('clear')
    op1 = range(0, 21)
    op2 = range(0, 21)
    while (index_less_than(count)):
        i1 = int(math.floor(random.random() * len(op1)))
        i2 = int(math.floor(random.random() * len(op2)))
        if op1[i1] - op2[i2] == to:
            try:
                do_print(op="-", op1=op1[i1], op2=op2[i2],
                         complement=complement, vertical=vertical)
            except KeyboardInterrupt:
                return


def generate(min_op1=0, max_op1=20, min_op2=0, max_op2=20,
             count=20, op="", complement=False, vertical=False):
    os.system('clear')
    reset_index()
    op1 = range(min_op1, max_op1 + 1)
    op2 = range(min_op2, max_op2 + 1)
    while (index_less_than(count)):
        i1 = int(math.floor(random.random() * len(op1)))
        i2 = int(math.floor(random.random() * len(op2)))
        try:
            do_print(op=op, op1=op1[i1], op2=op2[i2],
                     complement=complement, vertical=vertical)
        except KeyboardInterrupt:
            return


def do_print(op, op1, op2, complement=False, vertical=False):
    result = "?"
    if op == "+":
        inc_index()
        expected = op1 + op2
        reply(expected,
              layout % (index, op1, op, op2, result) if not vertical
              else layout_v % (index, op1, op, op2, result))
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
                  layout % (index, op1, op, op2, result) if not vertical
                  else layout_v % (index, op1, op, op2, result))
    elif op == "-":
        if op1 >= op2:
            inc_index()
            expected = op1 - op2
            reply(expected,
                  layout % (index, op1, op, op2, result) if not vertical
                  else layout_v % (index, op1, op, op2, result))
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
                      layout % (index, op1, op, op2, result) if not vertical
                      else layout_v % (index, op1, op, op2, result))
    else:
        if random.random() > 0.5:
            do_print("+", op1, op2, complement, vertical=vertical)
        else:
            do_print("-", op1, op2, complement, vertical=vertical)


def reply(expected, formula):
    actual = raw_input(formula)
    if not actual.isdigit():
        print layout_mark % mark_w
        return
    if expected == int(actual):
        print layout_mark % mark_c
    else:
        print layout_mark % mark_w
