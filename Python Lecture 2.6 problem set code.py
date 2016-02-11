if 6 > 7:
    print "Yep"
else:
    print "Nope"
   
    
      
var = 'Panda'
if var == "panda":
   print "Cute!"
elif var == "Panda":
   print "Regal!"
else:
   print "Ugly..."
   
   
   
temp = '32'
if temp > 85:
   print "Hot"
elif temp > 62:
   print "Comfortable" 
else:
   print "Cold" 
   
   
temp = 120
if temp > 85:
   print "Hot"
elif temp > 100:
   print "REALLY HOT!"
elif temp > 60:
   print "Comfortable" 
else:
   print "Cold"
   
   
happy = 3
if happy > 2:
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