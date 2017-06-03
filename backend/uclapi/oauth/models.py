from django.db import models
from .app_helpers import generate_user_token

class OAuthScope(models.Model):
    # We should really have a primary key for the OneToOneField
    id = models.AutoField(primary_key=True)

    # Can the key be used to show all rooms booked by the user?
    private_roombookings = models.BooleanField(default=False)

    # Can the key be used to access private timetable data?
    private_timetable = models.BooleanField(default=False)

    # Can the key be used to access private UCLU data?
    private_uclu = models.BooleanField(default=False)

    def scopeIsEqual(self, other):
        if not isinstance(other, self.__class__):
            return False
        
        if not self.private_roombookings == other.private_roombookings:
            return False

        if not self.private_timetable == other.private_timetable:
            return False

        if not self.private_uclu == other.private_uclu:
            return False

        return True

    def scopeDict(self):
        return {
            "private_roombookings": self.private_roombookings,
            "private_timetable": self.private_timetable,
            "private_uclu": self.private_uclu
        }

class OAuthToken(models.Model):
    # Use an incrementing ID that we can always rely on (assume a token could regenerate or be invalidated)
    id = models.AutoField(primary_key=True)
    # The app that requested this token to be created
    app = models.ForeignKey('dashboard.App', on_delete=models.CASCADE)
    # The user that this app will gain access to the data for. Every user that goes through the Shibboleth + OAuth
    # flow will get set up in the default database to ensure that we can fetch their, for example, eppn for custom
    # queries
    user = models.ForeignKey('dashboard.User', on_delete=models.CASCADE)

    # The actual token that can be used by an app to act on behalf of the user
    token = models.CharField(
        max_length=75,
        unique=True,
        default=generate_user_token
    )

    # The scope that the key works within. Every key has a unique scope
    # (in case the developer requests more permissions later)
    scope = models.OneToOneField(
        OAuthScope,
        on_delete=models.CASCADE
    )
