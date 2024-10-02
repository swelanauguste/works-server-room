import uuid

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Rack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Stack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Switch(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    stack = models.ForeignKey(
        Stack, on_delete=models.CASCADE, null=True, blank=True, related_name="switches"
    )
    rack = models.ForeignKey(
        Rack, on_delete=models.CASCADE, null=True, blank=True, related_name="racks"
    )

    class Meta:
        verbose_name_plural = "switches"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-{self.serial_number}")
        super(Switch, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.serial_number}"


class vLan(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "vlans"
        verbose_name = "vlan"

    def save(self, *args, **kwargs):
        self.role = self.role.lower()
        super(vLan, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Port(models.Model):
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    port = models.PositiveIntegerField(null=True)
    switch = models.ForeignKey(
        Switch, on_delete=models.CASCADE, null=True, blank=True, related_name="ports"
    )
    vlan = models.ManyToManyField(vLan, blank=True, related_name="vlans")
    note = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["port"]
        unique_together = ["switch", "port"]

    def save(self, *args, **kwargs):
        self.slug = uuid.uuid4()
        super(Port, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("port-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"pt-{self.port}"
