import re

rule = '(st, 0) : (sh, 1, R)'
#rulesTest = re.search("s[a-z0-9], [0-9/eo#xy]|(, [R/L])", rule)
rulesTest = re.search("^\(s[a-z0-9], [0-9/eo#xy]\) : \(s[a-z0-9], [0-9/eo#xy], [R/L]\)", rule)
if not rulesTest:
   print ("\nEntered data is not in the correct format, please remove and try again")
else:
   print ('OK')
