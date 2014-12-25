#!/usr/bin/env python
# -*- coding: utf-8 -*-



affil = dict(ipht=r"Leibniz Institute of Photonic Technology Jena",
             iap=r"Institute of Applied Physics Jena",
             epfl=r"\'Ecole Polytechnique F\'ed\'erale de Lausanne",
             usd=r"University of Southern Denmark",
             alcatel=r"Alcatel-Lucent Bell Labs France",
             zheji=r"Zhejiang University",
             iceland=r"University of Iceland")

afnums = [(idx + 1, af) for (idx, af) in enumerate(affil)]

class Author():
    def __init__(self, name, af_keys, email=None):
        self.name = name
        self.affil = af_keys
        self.email = email
    
    def afnums(self):
        numbers = []
        for af in self.affil:
            for afnum in afnums:
                if afnum[1] == af:
                    numbers.append(afnum[0])
        return ",".join([str(number) for number in sorted(numbers)])


###############################################################################
authors = [
  Author("Roman Kiselev", ["ipht", "iap"], "roman.kiselev@ipht-jena.de"),
  Author("Svyatoslav Kharitonov", ["epfl"]),
  Author("Ashwani Kumar", ["usd"]),
  Author(r"Ivan Fern\'andez de J\'auregui Ruiz", ["alcatel"]),
  Author("Xueliang Shi", ["zheij"]),
  Author(r"Kristj\'an Le\'osson", ["iceland"]),
  Author("Thomas Pertsch", ["iap"]),
  Author("Sergey Bozhevolnyi", ["usd"]),
  Author("Stefan Nolte", ["iap"]),
  Author("Arkadi Chipouline", ["iap"])
  ]
###############################################################################

print r"\author{"
for a in authors:
    print "  " + a.name + "\t" + r"\inst{" + a.afnums() + r"} \and"
print "  }"

print r"\institute{"
for af in afnums:
    print r"  \inst{" + str(af[0]) + "} " + affil[af[1]] + "\t" + r"\and"
print "  }"



print "\n" + "-"*20 + "\n"
print r"\usepackage{authblk}"
for a in authors:
    print r"\author[" + a.afnums() + "]{" + a.name + "}"
for af in afnums:
    print r"\affil[" + str(af[0]) + "]{" + affil[af[1]] + "}"



# TODO
# 1) Add email support
# 2) Remove last \and
# 3) Simplify code








