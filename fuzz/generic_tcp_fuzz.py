#!/usr/bin/env python
# Designed for use with boofuzz v0.0.8
from boofuzz import *

def main():
  session = Session(
    target=Target(
      connection=SocketConnection("192.168.106.137", 6666, proto='tcp')))
 # s_initialize("ltime")
 # s_string("LTIME", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("srun")
 # s_string("SRUN", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("trun")
 # s_string("TRUN", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("gmon")
 # s_string("GMON", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("gdog")
 # s_string("GDOG", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("rtime")
 # s_string("RTIME", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("stats")
 # s_string("STATS", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

  s_initialize("kstet")
  s_string("KSTET", fuzzable=False)
  s_delim(" ", fuzzable=False)
  s_string("string")
  s_static("\r\n")

 # s_initialize("gter")
 # s_string("GTER", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("hter")
 # s_string("HTER", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("lter")
 # s_string("LTER", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")

 # s_initialize("kstan")
 # s_string("KSTAN", fuzzable=False)
 # s_delim(" ", fuzzable=False)
 # s_string("string")
 # s_static("\r\n")



 # session.connect(s_get("ltime"));
 # session.connect(s_get("srun"));
 # session.connect(s_get("trun"));
 # session.connect(s_get("gmon"));
 # session.connect(s_get("gdog"));
 # session.connect(s_get("rtime"));
 # session.connect(s_get("stats"));
  session.connect(s_get("kstet"));
 # session.connect(s_get("gter"));
 # session.connect(s_get("hter"));
 # session.connect(s_get("lter"));
 # session.connect(s_get("kstan"));
 # session.connect(s_get("stats"));

  session.fuzz();

if __name__ == "__main__":
    main()

