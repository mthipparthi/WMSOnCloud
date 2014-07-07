from django.db import models

# Create your models here.

'''####################################################
   Model for Error Handling
   ####################################################
'''

class RSCErrorMessage(models.Model):
    # Unique Message Identifier
    msg_id = models.IntegerField(primary_key=True)

    # type of the message
    msg_type = models.CharField(max_length=1,
                                blank=False,
                                help_text="Type of the message like E-Error, I-Info, W-Warning")

    # Language in 2 letter code
    lang = models.CharField(max_length=2,
                            help_text="Language of the message")


    # Error message text
    msg_text = models.CharField(max_length=250,
                                blank=False,
                                help_text="Error Message")

    def __unicode__(self):
        return self.msg_id

    class Meta:
        db_table = "t_rsc_error_message"

    def as_json(self):
        return dict(
            msgid=self.msg_id,
            type=self.msg_type,
            msg=self.msg_text)

    def isError(self):
        return (self.msg_type == 'E')

    def isWarning(self):
        return (self.msg_type == 'W')

    def isInforamtion(self):
        return (self.msg_type == 'I')


