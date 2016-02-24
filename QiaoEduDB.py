#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import ConfigParser

class QiaoEduDB():

    def getDB(self):
        cfg = ConfigParser.ConfigParser()
        from os.path import expanduser
        home = expanduser("~")
        cfg.read(home+"/.my.cnf")
        (host, port, user, passwd) = (cfg.get("client", "host"), cfg.get("client", "port"), cfg.get("client", "user"), cfg.get("client", "password"))
        return MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, charset="utf8")


    if __name__ == "__main__":
        getDB()
