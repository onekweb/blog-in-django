from django.contrib.auth.backends import ModelBackend

class MyModelBackend(ModelBackend):
    def authenticate(self, username None, password None):
        print "My Logic"
        return super(MyModeBackend, self).authenticate(username username, password password)