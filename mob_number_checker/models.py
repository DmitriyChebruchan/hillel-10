from django.db import (
    models,
)


# Create your models here.
class PhoneNumber(models.Model):
    phone_number = models.CharField(
        max_length=30,
        null=False,
    )

    def __str__(
        self,
    ):
        return f"{self.phone_number}"


class VerificationPair(models.Model):
    phone_number = models.ForeignKey(
        PhoneNumber,
        on_delete=models.CASCADE,
    )
    code = models.CharField(max_length=10)
