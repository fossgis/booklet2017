#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sys, os, csv

tnListen = {}

reader = csv.reader(open(sys.argv[1], "r"), delimiter=',')
# 0, 1,    2,   3,    4,       5,          6,       7,         8
# id,email,name,title,subtitle,description,abstract,start_time,name
for row in reader:
    if row[0] == "id":
        continue
    print("%{}".format(row[7]))
    if row[8] == "AM HS 10":
        print("\\abstractZehn{" + row[2] + "}%\n{" + row[3] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}\n")
    elif row[8] == "AM HS 9":
        print("\\abstractNeun{" + row[2] + "}%\n{" + row[3] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}\n")
    elif row[8] == "IM HS 13":
        print("\\abstractDreizehn{" + row[2] + "}%\n{" + row[3] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}\n")
    elif row[8] == "IM HS 11":
        print("\\abstractElf{" + row[2] + "}%\n{" + row[3] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}\n")
    else:
        print("\\abstractZehn{" + row[2] + "}%\n{" + row[3] + "}%\n{" + row[4] + "}%\n{" + row[5] + "}\n")
    print("\n")

