__author__ = 'teo'

a = None
if not a:
    print 'None evaluates to False'

a = False
if not a:
    print 'False obviously evaluates to False'

a = 0
if not a:
    print '0 evaluates to False'

a = ''
if not a:
    print '\'\' evaluates to False'

a = ()
if not a:
    print '() evaluates to False'

a = []
if not a:
    print '[] evaluates to false'

a = {}
if not a:
    print '{} evaluates to false'

print 'boolean operators: "and", "or", "not". '