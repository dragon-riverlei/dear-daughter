# -*- coding: utf-8 -*-

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

layout_2oprd = "%2s.   %2s %s %2s %s %-3s  -> "
layout_3oprd = "%2s.   %2s %s %2s %s %2s %s %-3s  -> "
layout_2oprd_v = "%2s.       %2s\n%8s  %2s\n      ――――――――\n%12s  -> "
layout_2oprd_log = "%2s   %2s %s %2s %s %-3s "
layout_3oprd_log = "%2s   %2s %s %2s %s %2s %s %-3s "
layout_2oprd_mark = "%27s"
layout_3oprd_mark = "%36s"


class QiaoArith():
    index = 0
    min_default = 0
    max_default = 20
    valid_operators = ['+', '-', '', '=', '?']
    valid_operands = [int]
    vertical = False

    def __init__(self):
        self.load_default_formulas()

    def load_default_formulas(self):
        self.formula_1_1 = [(self.min_default, self.max_default),
                            '+',
                            (self.min_default, self.max_default)]
        self.formula_1_2 = [(self.min_default, self.max_default),
                            '-',
                            (self.min_default, self.max_default)]
        self.formula_1_3 = [(self.min_default, self.max_default),
                            '',
                            (self.min_default, self.max_default)]

        self.formula_2_1 = [(self.min_default, self.max_default),
                            '+',
                            (self.min_default, self.max_default),
                            '+',
                            (self.min_default, self.max_default)]
        self.formula_2_2 = [(self.min_default, self.max_default),
                            '+',
                            (self.min_default, self.max_default),
                            '-',
                            (self.min_default, self.max_default)]
        self.formula_2_3 = [(self.min_default, self.max_default),
                            '+',
                            (self.min_default, self.max_default),
                            '',
                            (self.min_default, self.max_default)]
        self.formula_2_4 = [(self.min_default, self.max_default),
                            '-',
                            (self.min_default, self.max_default),
                            '+',
                            (self.min_default, self.max_default)]
        self.formula_2_5 = [(self.min_default, self.max_default),
                            '-',
                            (self.min_default, self.max_default),
                            '-',
                            (self.min_default, self.max_default)]
        self.formula_2_6 = [(self.min_default, self.max_default),
                            '-',
                            (self.min_default, self.max_default),
                            '',
                            (self.min_default, self.max_default)]
        self.formula_2_7 = [(self.min_default, self.max_default),
                            '',
                            (self.min_default, self.max_default),
                            '+',
                            (self.min_default, self.max_default)]
        self.formula_2_8 = [(self.min_default, self.max_default),
                            '',
                            (self.min_default, self.max_default),
                            '-',
                            (self.min_default, self.max_default)]
        self.formula_2_9 = [(self.min_default, self.max_default),
                            '',
                            (self.min_default, self.max_default),
                            '',
                            (self.min_default, self.max_default)]

    def reset_default_formulas(self, min_default, max_default):
        self.min_default = min_default
        self.max_default = max_default
        self.load_default_formulas()

    def reset_index(self):
        self.index = 0

    def inc_index(self):
        self.index += 1

    def index_less_than(self, count):
        return self.index < count

    def validate_formula(self, formula):
        if formula is None:
            return False

        # at least 3 elements in a formula
        if len(formula) < 3:
            print "At least 3 elements in a formula."
            print "Number of elements in the given formula is: " + len(formula)
            return False

        # number of elements in a formula should be odd
        if len(formula) % 2 == 0:
            print "Number of elements in a formula should be odd."
            print "Number of elements in the given formula is: " + len(formula)
            return False

        # operators in a formula should be supported
        for operator in formula[1::2]:
            if operator not in self.valid_operators:
                print "Operators in a formula should be supported."
                print "Found unsupported operator: " + operator
                return False

        # types of operands in a formula should be supported
        for operand in formula[0::2]:
            if(len(operand) != 2):
                print "Operand in a formula should have exactly 2 elements."
                print "Found invalid operand: " + operand
                return False
            if not (type(operand[0]) in self.valid_operands and
                    type(operand[1]) in self.valid_operands and
                    operand[0] <= operand[1]):
                print "Operand in a formula should be the supported type" \
                      "with 2nd no less than 1st."
                print "Found invalid operand: " + operand
                return False

    def generate(self, formula=None, count=20, qpos="last"):
        if formula is None:
            print "No formula specified."
            return
        if self.validate_formula(formula):
            print "Invalid formula."
            return
        if not qpos == "last" and not str(qpos).isalnum():
            raise ValueError('qpos must be "last" or number.')
        os.system('clear')
        self.reset_index()
        equations = []
        logger.info(
            "generate begins with formula " + str(formula))
        if formula[-2:] == '=':
            while(self.index_less_than(count)):
                equation = self.backward_scan(formula)
                if equation is not None:
                    equations.append(equation)
                    self.inc_index()
        else:
            while(self.index_less_than(count)):
                equation = self.forward_scan(formula)
                if equation is not None:
                    head = (self.valid_operators[0], equation[0])
                    tail = zip(equation[1::2], equation[2::2])
                    result = reduce(self.calculate_wrapper, tail, head)[1]
                    equations.append(
                        equation + [self.valid_operators[3], result])
                    self.inc_index()
        if qpos == "last":
            qpos = len(equations[0])
        elif int(qpos) > len(equations[0]):
            qpos = len(equations[0])
        else:
            qpos = int(qpos)
        try:
            index = 1
            for e in equations:
                expected = e[qpos - 1]
                e[qpos - 1] = self.valid_operators[4]
                self.display_reply(expected, e, index)
                index += 1
        except KeyboardInterrupt:
            logger.info(
                "generate cancelled with formula " + str(formula))

    def forward_scan(self, formula):
        op = formula[1]
        if op == "":
            if random.random() > 0.5:
                op = "+"
            else:
                op = "-"
        if type(formula[0]) is tuple:
            op1s = range(formula[0][0], formula[0][1] + 1)
            i1 = int(math.floor(random.random() * len(op1s)))
            op1 = op1s[i1]
        else:
            op1 = formula[0]
        op2s = range(formula[2][0], formula[2][1] + 1)
        i2 = int(math.floor(random.random() * len(op2s)))
        op2 = op2s[i2]
        while (op == "-" and op1 < op2):
            i2 = int(math.floor(random.random() * len(op2s)))
            op2 = op2s[i2]
        if len(formula) == 3:
            return [op1, op, op2]
        else:
            r = self.calculate(op1, op, op2)
            f = [r] + formula[3:]
            return [op1, op, op2] + self.forward_scan(f)[1:]

    def backward_scan(self, formula):
        pass

    def calculate(self, op1, op, op2):
        if op == self.valid_operators[0]:
            return op1 + op2
        elif op == self.valid_operators[1]:
            return op1 - op2
        else:
            raise ValueError('Non-supported operator: ' + op)

    def calculate_wrapper(self, x, y):
        r = self.calculate(x[1], y[0], y[1])
        return (self.valid_operators[0], r)

    def display_reply(self, expected, equation, index):
        if self.vertical:
            self.display_reply_v(expected, equation, index)
        else:
            self.display_reply_h(expected, equation, index)

    def display_reply_h(self, expected, equation, index):
        if len(equation) == 5:
            layout = layout_2oprd
            layout_log = layout_2oprd_log
            layout_mark = layout_2oprd_mark
        elif len(equation) == 7:
            layout = layout_3oprd
            layout_log = layout_3oprd_log
            layout_mark = layout_3oprd_mark
        e = tuple([index] + equation)
        logger.info("formula " +
                    layout_log % tuple([index] + equation) + " begins")
        actual = raw_input(layout % e)
        if str(expected) == actual:
            logger.info("formula " +
                        layout_log % tuple([index] + equation) + " ends")
            print layout_mark % mark_c
        else:
            logger.info("formula " +
                        layout_log % tuple([index] + equation) +
                        " ends with error: " + actual)
            print layout_mark % mark_w

    def display_reply_v(self, expected, equation, index):
        if len(equation) == 5:
            layout = layout_2oprd_v
            layout_log = layout_2oprd_log
            layout_mark = layout_2oprd_mark
            e = tuple([index] + equation[0:3] + [equation[4]])
        logger.info("formula " +
                    layout_log % tuple([index] + equation) + " begins")
        actual = raw_input(layout % e)
        if str(expected) == actual:
            logger.info("formula " +
                        layout_log % tuple([index] + equation) + " ends")
            print layout_mark % mark_c
        else:
            logger.info("formula " +
                        layout_log % tuple([index] + equation) +
                        " ends with error: " + actual)
            print layout_mark % mark_w
