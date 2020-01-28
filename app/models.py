from django.db import models

# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AccountDetail(models.Model):
    BRAND_CHOICES = (
        ("onyx", "ONYX"),
        ("inning", "INNING"),
        ("gt", "GT"),
    )
    PATTERN_CHOICES = (
        ("301", "301"),
        ("311", "311"),
        ("121", "121"),
        ("104", "104"),
        ("105", "105"),
        ("307", "307"),
        ("123", "123"),
        ("gT", "GT"),
    )
    SIZE_CHOICES = (
        ('1100r20','1100R20'),
        ('1000r20', '1000R20'),
        ('1200r20', '1200R20'),
        ('900r20', '900R20'),
        ('825-16', '825-16'),
        ('725-16', '725-16'),
    )

    customer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='customer')
    date = models.DateField()
    description = models.CharField(max_length=200)
    qty = models.IntegerField()
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, default=BRAND_CHOICES[0][1])
    pattern = models.CharField(max_length=20, choices=PATTERN_CHOICES, default=PATTERN_CHOICES[0][1])
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default=SIZE_CHOICES[0][1])
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    unit_price = models.BigIntegerField()
    credit = models.BigIntegerField()
    debit = models.BigIntegerField()
    balance = models.BigIntegerField()

    def save(self, *args, **kwargs):
        self.credit = self.qty * self.unit_price / 2
        self.balance = self.credit - self.debit
        super(AccountDetail, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.customer}'

