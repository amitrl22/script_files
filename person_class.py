

class person:

    def__init__(self,fname,lname,email):

    self.fname=fname
    self.lname=lname
    self.email=email

    def__str__(self):

        return'person({0}{1}{2})'.format(___)

    def fullname(self):
        return self.fname

    def getemail(self):
        return self.email

    p=person('abc','xyx','abc@xyz.com')

    print p

    fn=p.fullname()

    print 'my fullname is',fn

