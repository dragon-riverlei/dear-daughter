#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import ConfigParser
import re

class QiaoEduDB():
    db = None
    
    def __init__(self):
        cfg = ConfigParser.ConfigParser()
        from os.path import expanduser
        home = expanduser("~")
        cfg.read(home+"/.my.cnf")
        (host, port, user, passwd) = (cfg.get("client", "host"), cfg.get("client", "port"), cfg.get("client", "user"), cfg.get("client", "password"))
        self.db = MySQLdb.connect(host=host, port=int(port), user=user, passwd=passwd, db="qiao_edu",charset="utf8")

    def query_junior_high_schools(self):
        self.db.query("select * from junior_high_schools")
        result = self.db.use_result()
        print result.fetch_row(0)

    def insert_junior_high_school(self):
        cur = self.db.cursor()
        for line in open("/cygdrive/d/GitHub/dragon-riverlei/dear-daughter/to02JuniorHigh/2015/shanghaiJuniorHighSchoolCode2015").readlines():
            values = line.split(",")
            (code, area, name) = (values[0], values[1], values[2])
            cur.execute("insert into  junior_high_school values (%s, %s, %s)", (code, area, name))
        self.db.commit()

    def insert_senior_high_school(self):
        cur = self.db.cursor()
        names  = set()
        for line in open("/cygdrive/d/GitHub/dragon-riverlei/dear-daughter/to04University/2015/admission0").readlines():
            values = line.split(",")
            names.add(values[1])
        for name in names:
            cur.execute("insert into senior_high_school values (%s)", [name])
        self.db.commit()

    def insert_senior_high_school_pre_admission(self):
        cur = self.db.cursor()
        for line in open("/cygdrive/d/GitHub/dragon-riverlei/dear-daughter/to03SeniorHigh/2015/shanghaiSeniorHighSchoolPreAdmission2015").readlines():
            (stu_no, to_school) = line.split(",")
            cur.execute("insert into  senior_high_school_pre_admission values (%s, %s, %s, %s)", (stu_no, stu_no[2:8], to_school, "2015"))
        self.db.commit()

    def insert_university(self):
        cur = self.db.cursor()
        for line in open("/cygdrive/d/GitHub/dragon-riverlei/dear-daughter/to04University/candidateUniversityCode").readlines():
            (code, name) = line.split(",")
            cur.execute("insert into  university values (%s, %s)", (code, name))
        self.db.commit()

    def insert_university_admission0_2015():
        cur = self.db.cursor()
        for line in open("/cygdrive/d/GitHub/dragon-riverlei/dear-daughter/to04University/2015/admission0").readlines():
            (code, name) = line.split(",")
            cur.execute("insert into  university values (%s, %s)", (code, name))
        self.db.commit()
        
if __name__ == "__main__":
    qdb = QiaoEduDB()
    qdb.insert_junior_high_school()
    qdb.insert_senior_high_school()
    qdb.insert_senior_high_school_pre_admission()
    qdb.insert_university()
