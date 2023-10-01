from django.db import models
from django.utils import timezone

class SoftDeleteMixin(models.Model):
    """ A mixin for adding soft deletion functionality to a model."""

    is_deleted = models.BooleanField(default=False, db_index=True, help_text="Is the record deleted?")
    deleted_at = models.DateTimeField(null=True, blank=True, help_text="Date and time of deletion")

    class Meta:
        abstract = True

    def delete(self):
        """ Soft delete the record."""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def undelete(self):
        """ Restore a soft-deleted record."""
        self.is_deleted = False
        self.deleted_at = None
        self.save()


class IsActiveMixin(models.Model):

    is_active = models.BooleanField(default=True, help_text="Is the user account active?")

    class Meta:
        abstract = True

    def activate(self):
        """ Activate the user account. """
        self.is_active = True
        self.save()

    def deactivate(self):
        """ Deactivate the user account. """
        self.is_active = False
        self.save()


class UserMixin(models.Model):
    class Meta:
        abstract = True


    email = models.EmailField(max_length=200, unique=True, db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
