#!/usr/bin/env python
# -*- coding: utf-8 -*-

af_db = dict(
  ipht=r"Leibniz Institute of Photonic Technology Jena",
  iap=r"Institute of Applied Physics Jena",
  epfl=r"\'Ecole Polytechnique F\'ed\'erale de Lausanne",
  usd=r"University of Southern Denmark",
  alcatel=r"Alcatel-Lucent Bell Labs France",
  zheji=r"Zhejiang University",
  iceland=r"University of Iceland"
  )

affiliations = ["dummy"]

class Author():
    def __init__(self, name, institutes, email=None):
        self.affil = []
        if type(institutes) == str:
            institutes = [institutes]
        for inst in institutes:
            inst_name = af_db[inst]
            if not inst_name in affiliations:
                affiliations.append(inst_name)
            self.affil.append(affiliations.index(inst_name))
            
        self.name = name
        if email:
            self.email = "\\thanks{%s}" % email
        else:
            self.email = ""
    
    def print_beamer(self, last=False):
        output = "  "  + self.name + r"\inst{" + \
                 ",".join([str(num) for num in self.affil]) + "} " + self.email
        if not last:
            output = output.ljust(75) + r"\and"
        print output

    def print_authblk(self):
        print r"\author[" + ",".join([str(num) for num in self.affil]) + "]{" + self.name + "}"


###############################################################################
authors = [
  Author(r"R.~Kiselev", ["ipht", "iap"]),
  Author(r"S.~Kharitonov", ["epfl"]),
  Author(r"A.~Kumar", ["usd"]),
  Author(r"I.~J\'auregui", ["alcatel"]),
  Author(r"X.~Shi", ["zheji"]),
  Author(r"K.~Le\'osson", ["iceland"]),
  Author(r"T.~Pertsch", ["iap"]),
  Author(r"S.~Bozhevolnyi", ["usd"]),
  Author(r"S.~Nolte", ["iap"]),
  Author(r"A.~Chipouline", ["iap"])
  ]
###############################################################################

print r"\author[~~R. Kiselev, \texttt{roman.kiselev@ipht-jena.de}~~~~~~~]{"
for a in authors:
    a.print_beamer(a==authors[-1])
print "  }"

print r"\institute{"
for num, af in enumerate(affiliations):
    if num == 0:
        continue
    output = r"  \inst{" + str(num) + "} " + af
    if not af == affiliations[-1]:
        output = output.ljust(75-13) + r"\vspace{-3mm}\and"
    print output
print "  }"



print "\n" + "-"*20 + "\n"
print r"\usepackage{authblk}"
print "% Font size for list of authors and affiliations"
print r"\renewcommand\Authfont{\fontsize{11}{1}\selectfont}"
print r"\renewcommand\Affilfont{\fontsize{9}{1}\itshape}"

for a in authors:
    a.print_authblk()
for num, af in enumerate(affiliations):
    if num == 0:
        continue
    print r"\affil[" + str(num) + "]{" + af + "}"


