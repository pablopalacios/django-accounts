from hashlib import md5

from django.db import models

from authtools.models import AbstractNamedUser


class User(AbstractNamedUser):

    def get_gravatar_hash(self):
        email = self.email.lower().encode()
        hash = md5(email).hexdigest()
        return hash

    def gravatar(self, size=80, default='mm'):
        url = 'http://www.gravatar.com/avatar/{hash}?size={size}&d={default}'
        return url.format(size=size, hash=self.get_gravatar_hash(), default=default)
