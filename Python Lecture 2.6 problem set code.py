 print "Nope"
 print "Cute!"
 print "Cold" 
 print "Hot"
 print "hello world"
varA = 'abcg'
varB = 'def'
if (type(varA) or type(varB)) == str:
    print "string involved"

if type(varA) == str or type(varB) == str:
    print 'string involved'
elif varA > varB:
    print 'bigger'
elif varA == varB:
    print 'equal'
else:
    print 'smaller'
