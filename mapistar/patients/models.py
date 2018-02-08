# Standard Libraries
from string import capwords

# Third Party Libraries
from django.db import models

CAPWORDS_ATTRS = ('name', 'firstname')


class PatientManager(models.Manager):
    """
    custum patient manger to modifie create and update
    """
    attrs = CAPWORDS_ATTRS

    def create(self, **kwargs):
        """
        enhancement
        """
        # capwors certain fields
        for i in self.attrs:
            kwargs[i] = capwords(kwargs[i])

        # recall base create
        return super(PatientManager, self).create(**kwargs)


class Patient(models.Model):
    """
    ase class of patient.&
    Require on ly 3 fields : name, firstname, birthdate
    """
    attrs = CAPWORDS_ATTRS
    # required Field
    name = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthdate = models.DateField()
    sexe = models.BooleanField(default=True)  # True if women else false
    # non required fields

    street = models.CharField(blank=True, max_length=200, default="")
    postalcode = models.CharField(blank=True, max_length=5, default="")
    city = models.CharField(max_length=200, blank=True, default="")
    phonenumber = models.CharField(blank=True, max_length=20, default="")
    email = models.EmailField(blank=True, max_length=100, default="")
    alive = models.BooleanField(default=True)

    objects = PatientManager()

    def __str__(self):
        """
        nice printing Firstname Name
        """
        return self.firstname + ' ' + self.name

    def save(self, *args, **kwargs):
        """
        customizing save method, adds :
        - fore capwords for name et firstanme
        """
        for i in self.attrs:
            setattr(self, i, capwords(getattr(self, i)))

        super(Patient, self).save(*args, **kwargs)


"""
champs à ajouter :
date de décès
décédé
médecin traitant déclaré
notes divers
"""
