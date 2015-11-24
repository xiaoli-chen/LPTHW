class parent(object):
    def implicit(self):
        print "Parent implicit()"
    
    
    
class grandp(object):
    def implicit(self):
        print "Grandpa and Grandma"

class child(parent,grandp):
    def implicit(self):
        print "Child explicit()"
        super(child,self).implicit()
        print "Child changed"
    
dad = parent()
son = child()

dad.implicit()
son.implicit()
#dad.implicit()

#dad2 = child()
#dad2.implicit()
