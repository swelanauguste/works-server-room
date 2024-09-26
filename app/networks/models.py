from django.db import models
from django.urls import reverse


class Rack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"rk-{self.name}"


class Stack(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"st-{self.name}"


class Switch(models.Model):
    name = models.CharField(max_length=100)
    stack = models.ForeignKey(
        Stack, on_delete=models.CASCADE, null=True, blank=True, related_name="switches"
    )
    rack = models.ForeignKey(
        Rack, on_delete=models.CASCADE, null=True, related_name="switches"
    )

    def __str__(self):
        return f"sw-{self.name} - {self.rack}"


class Network(models.Model):
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Port(models.Model):
    port = models.PositiveIntegerField(null=True)
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE, null=True, blank=True)
    switch = models.ForeignKey(
        Switch, on_delete=models.CASCADE, null=True, blank=True, related_name="ports"
    )
    network = models.ForeignKey(
        Network, on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(
        max_length=10,
        choices=[
            ("voice", "voice"),
            ("data", "data"),
            ("voice-data", "voice-data"),
            ("down", "down"),
            ("uplink", "uplink"),
            ("DMZ", "DMZ"),
            ("MGMT", "MGMT"),
            ("WIFI", "WIFI"),
            ("projects", "projects"),
        ],
        default="v-d",
    )
    vlan = models.CharField(max_length=10, blank=True)
    note = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["port"]
        unique_together = ["switch", "port"]

    def get_title(self):
        if self.network and self.vlan:
            return f"{self.get_status_display()}-{self.network}-{self.vlan}"
        if self.network:
            return f"{self.get_status_display()}-{self.network}"
        if self.vlan:
            return f"{self.get_status_display()}-{self.vlan}"

        return f"{self.get_status_display()}"

    def get_absolute_url(self):
        return reverse("port-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"pt-{self.port}"
