from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

import logging

class    EmailAuthBackend(object):
    """
    Email Authentication Backend
    Allows a user to sign in using an email/password pair rather than
    a username/password pair.
    """
    def authenticate(self, email=None, password=None):
        """ Authenticate a user based on email address as the user name"""
        """ user name is nothing but email id,to be in sync with user auth """
        """ customization we retained this way """
        try:
            logger = logging.getLogger(__name__)
            logger.debug("Authentication begins for user - %s", email);
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                logger.info("Authentication failed for user - %s", email)
                return None
        except User.DoesNotExist:
            logger.info("User doesn't exist for user %s", email)
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id."""
        """ signature is kept as user_id but we have to pass emailid as an input"""
        """ this designed this way to be in sync with user auth customization    """
        try:
            return  User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
