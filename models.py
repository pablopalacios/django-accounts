from hashlib import md5

from django.db import models

from authtools.models import AbstractNamedUser


class User(AbstractNamedUser):

    def gravatar(self, size=80, default='mm'):
        email = self.email.lower().encode()
        hash = md5(email).hexdigest()
        url = 'http://www.gravatar.com/avatar/{hash}?size={size}&d={default}'
        return url.format(size=size, hash=hash, default=default)
