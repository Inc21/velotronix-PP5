from django.db import models


class About(models.Model):
    """ About model """

    class Meta:
        verbose_name_plural = "About Us"

    name = models.CharField(max_length=254, null=False, blank=False,
                            default="velotronix")
    delivery_info = models.TextField(null=True, blank=True)
    returns_info = models.TextField(null=True, blank=True)
    faq = models.TextField(null=True, blank=True)
    privacy_policy = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    """ Contact model """
    author = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name + ' - ' + self.email

    class Meta:
        ordering = ['-created']
