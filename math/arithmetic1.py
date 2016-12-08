# -*- coding: utf-8 -*-

import logging
import math
import numpy
import os
import random
import time


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fh = logging.FileHandler("arithmetic.log")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


class QiaoArith():
    mark_c = "✔"
    mark_w = "✘"
    mark_rank = "❆"

    rank_on = False
    rank_0 = 30
    rank_1 = 20
    rank_2 = 15
    rank_3 = 10
    rank_4 = 5
    rank_5 = 2

    layout_2oprd = "%2s.   %2s %s %2s %s %-3s  -> "
    layout_3oprd = "%2s.   %2s %s %2s %s %2s %s %-3s  -> "
    layout_2oprd_v = "%2s.       %2s\n%8s  %2s\n      ――――――――\n%12s  -> "
    layout_3oprd_v = "%2s.       %2s\n%8s  %2s\n%8s  %2s\n      ――――――――" \
                     "\n%12s  -> "
    layout_2oprd_log = "%2s   %2s %s %2s %s %-3s "
    layout_3oprd_log = "%2s   %2s %s %2s %s %2s %s %-3s "
    layout_2oprd_mark = "%27s %5.1f %5s"
    layout_3oprd_mark = "%36s %5.1f %5s"

    index = 0
    min_default = 0
    max_default = 20
    valid_operators = ['+', '-', '', '=', '?']
    valid_operands = [int]
    vertical = False

    def __init__(self):
        self.load_default_formulas()

    def menu(self):
        menu = """
 1. 10以内加法
 2. 10以内减法
 3. 10以内加减
 4. 10以内连加
 5. 10以内连减
 6. 10以内连加连减

 7. 20以内不进位加法
 8. 20以内不退位减法
 9. 20以内不进位不退位
10. 20以内进位加法
11. 20以内退位减法
12. 20以内进位退位加减

13. 20以内加减
14. 20以内连加
15. 20以内连减
16. 20以内连加连减
        """
        os.system('clear')
        print menu
        num = raw_input("Enter a number: ")
        f = self.f1_1
        if str(num) == "1":
            f = [(0, 10), '+', (0, 10), '=', (0, 10)]
        elif str(num) == "2":
            f = [(0, 10), '-', (0, 10), '=', (0, 10)]
        else:
            f = self.f1_1
        self.generate(f)

    def load_default_formulas(self):
        self.f1_1 = [(self.min_default, self.max_default),
                     '+',
                     (self.min_default, self.max_default)]
        self.f1_2 = [(self.min_default, self.max_default),
                     '-',
                     (self.min_default, self.max_default)]
        self.f1_3 = [(self.min_default, self.max_default),
                     '',
                     (self.min_default, self.max_default)]

        self.f2_1 = [(self.min_default, self.max_default),
                     '+',
                     (self.min_default, self.max_default),
                     '+',
                     (self.min_default, self.max_default)]
        self.f2_2 = [(self.min_default, self.max_default),
                     '+',
                     (self.min_default, self.max_default),
                     '-',
                     (self.min_default, self.max_default)]
        self.f2_3 = [(self.min_default, self.max_default),
                     '+',
                     (self.min_default, self.max_default),
                     '',
                     (self.min_default, self.max_default)]
        self.f2_4 = [(self.min_default, self.max_default),
                     '-',
                     (self.min_default, self.max_default),
                     '+',
                     (self.min_default, self.max_default)]
        self.f2_5 = [(self.min_default, self.max_default),
                     '-',
                     (self.min_default, self.max_default),
                     '-',
                     (self.min_default, self.max_default)]
        self.f2_6 = [(self.min_default, self.max_default),
                     '-',
                     (self.min_default, self.max_default),
                     '',
                     (self.min_default, self.max_default)]
        self.f2_7 = [(self.min_default, self.max_default),
                     '',
                     (self.min_default, self.max_default),
                     '+',
                     (self.min_default, self.max_default)]
        self.f2_8 = [(self.min_default, self.max_default),
                     '',
                     (self.min_default, self.max_default),
                     '-',
                     (self.min_default, self.max_default)]
        self.f2_9 = [(self.min_default, self.max_default),
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
                    operand[0] < operand[1]):
                print "Operand in a formula should be the supported type" \
                      "with 2nd greater than 1st."
                print "Found invalid operand: " + operand
                return False

        # further validation when the result has constraints
        if formula[-2] == '=':
            lb, ub = formula[0]
            for e in zip(formula[1:len(formula)-1:2],
                         formula[2:len(formula)-1:2]):
                if e[0] == "+":
                    ub = ub + e[1][1]
                    lb = lb + e[1][0]
                elif e[0] == "-":
                    if ub <= e[1][0]:
                        print "No or not enought intersect between " + \
                              str((lb, ub)) + ":" + str(e[1])
                        return False
                    ub = ub - e[1][0]
                    if lb >= e[1][1]:
                        lb = lb - e[1][1]
                    else:
                        lb = 0
                else:
                    print "Operator should not be empty " \
                          "when result is specified."
            expected = range(formula[-1][0], formula[-1][1]+1)
            got = range(lb, ub+1)
            if len(set(expected) & set(got)) < 1:
                print "Specified result range out of possible range."
                return False
        return True

    def generate(self, formula=None, count=20, qpos="last"):
        if formula is None:
            print "No formula specified."
            return
        if not self.validate_formula(formula):
            print "Invalid formula."
            return
        if not qpos == "last" and not str(qpos).isalnum():
            raise ValueError('qpos must be "last" or number.')
        os.system('clear')
        self.reset_index()
        equations = []
        logger.info(
            "generate begins with formula " + str(formula))
        if formula[-2] == '=':
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
            results = []
            for e in equations:
                expected = e[qpos - 1]
                print e
                e[qpos - 1] = self.valid_operators[4]
                results.append(self.display_reply(expected, e, index))
                index += 1
        except KeyboardInterrupt:
            logger.info(
                "generate cancelled with formula " + str(formula))
        times = [r[0] for r in results]
        average = numpy.mean(times)
        rank_txt = self.rank_txt(average)
        corrects = [r[1] for r in results if r[1] is True]
        print str(len(corrects)) + " correct out of " + str(len(results))
        if self.rank_on:
            print "Average speed:" + rank_txt

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

    def backward_scan(self, formula, equation):
        if type(formula[-1]) is tuple:
            results = range(formula[-1][0], formula[-1][1] + 1)
            ir = int(math.floor(random.random() * len(results)))
            result = results[ir]
        else:
            result = formula[-1]
        if len(formula) == 3:
            if formula[0][0] <= result <= formula[0][1]:
                equation.append(result)
                return True
            else:
                return False
        else:
            op2s = range(formula[-3][0], formula[-3][1] + 1)
            idx_map = [0] * len(op2s)
            while (len([idx for idx in idx_map if idx == 0]) != 0):
                i2 = int(math.floor(random.random() * len(op2s)))
                op2 = op2s[i2]
                idx_map[i2] += 1
                op = formula[-4]
                if op == "":
                    if random.random() > 0.5:
                        op = "+"
                    else:
                        op = "-"
                while (op == "+" and result < op2):
                    i2 = int(math.floor(random.random() * len(op2s)))
                    op2 = op2s[i2]
                sub_result = self.calculate(result, self.oppo_op(op), op2)
                sub_formula = formula[0:-4] + ['=', sub_result]
                if self.backward_scan(self, sub_formula) is True:
                    equation + [op, op2]
                    return True
            return False

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

    def oppo_op(self, op):
        if op == "+":
            return "-"
        else:
            return "+"

    def display_reply(self, expected, equation, index):
        if self.vertical:
            return self.display_reply_v(expected, equation, index)
        else:
            return self.display_reply_h(expected, equation, index)

    def display_reply_h(self, expected, equation, index):
        if len(equation) == 5:
            layout = self.layout_2oprd
            layout_log = self.layout_2oprd_log
            layout_mark = self.layout_2oprd_mark
        elif len(equation) == 7:
            layout = self.layout_3oprd
            layout_log = self.layout_3oprd_log
            layout_mark = self.layout_3oprd_mark
        e = tuple([index] + equation)
        logger.info("formula " +
                    layout_log % tuple([index] + equation) + " begins")
        start = time.time()
        actual = raw_input(layout % e)
        end = time.time()
        spent = end - start
        rank_txt = ""
        if self.rank_on:
            rank_txt = self.rank_txt(spent)
        if str(expected) == actual:
            logger.info("formula " +
                        layout_log % tuple([index] + equation) + " ends")
            print layout_mark % (self.mark_c, spent, rank_txt)
            return (spent, True)
        else:
            logger.info("formula " +
                        layout_log % tuple([index] + equation) +
                        " ends with error: " + actual)
            print layout_mark % (self.mark_c, spent, rank_txt)
            return (spent, False)

    def display_reply_v(self, expected, equation, index):
        if len(equation) == 5:
            layout = self.layout_2oprd_v
            layout_log = self.layout_2oprd_log
            layout_mark = self.layout_2oprd_mark
            e = tuple([index] + equation[0:3] + [equation[4]])
        elif len(equation) == 7:
            layout = self.layout_3oprd_v
            layout_log = self.layout_3oprd_log
            layout_mark = self.layout_3oprd_mark
            e = tuple([index] + equation[0:5] + [equation[6]])
        logger.info("formula " +
                    layout_log % tuple([index] + equation) + " begins")
        start = time.time()
        actual = raw_input(layout % e)
        end = time.time()
        spent = end - start
        rank_txt = ""
        if self.rank_on:
            rank_txt = self.rank_txt(spent)
        if str(expected) == actual:
            logger.info("formula " +
                        layout_log % tuple([index] + equation) + " ends")
            print layout_mark % (self.mark_c, spent, rank_txt)
            return (spent, True)
        else:
            logger.info("formula " +
                        layout_log % tuple([index] + equation) +
                        " ends with error: " + actual)
            print layout_mark % (self.mark_w, spent, rank_txt)
            return (spent, False)

    def rank_txt(self, time_spent):
        rankn = 0
        if time_spent >= self.rank_0:
            rankn = 0
        elif time_spent >= self.rank_1:
            rankn = 1
        elif time_spent >= self.rank_2:
            rankn = 2
        elif time_spent >= self.rank_3:
            rankn = 3
        elif time_spent >= self.rank_4:
            rankn = 4
        elif time_spent >= self.rank_5:
            rankn = 5
        else:
            rankn = 6
        return self.mark_rank * rankn
