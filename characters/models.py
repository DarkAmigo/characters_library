from django.db import models


class Universe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Creator(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ability(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255)

    universe = models.ForeignKey(
        Universe,
        on_delete=models.CASCADE,
        related_name="characters"
    )

    creator = models.ForeignKey(
        Creator,
        on_delete=models.CASCADE,
        related_name="characters"
    )

    abilities = models.ManyToManyField(
        Ability,
        related_name="characters"
    )

    weapons = models.ManyToManyField(
        Weapon,
        related_name="characters"
    )

    teams = models.ManyToManyField(
        Team,
        related_name="characters"
    )

    def __str__(self):
        return self.name
