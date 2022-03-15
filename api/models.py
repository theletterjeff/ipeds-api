"""
Models for IPEDS data. To access source data, visit
https://nces.ed.gov/ipeds/use-the-data, click on the `Survey Data`
drop-down, and select "Complete Data Files".
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    """
    User with email as the default identifier field
    (instead of username).
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class IPEDSDictionary(models.Model):
    """
    Dictionary of variables
    - model_name: The model that the dictionary data references
    - varnumber: Identifier number for variable
    - varname: Column-header name (short, all-caps) for variable
    - DataType: Either 'A' (alphanumeric) or 'N' (numeric)
    - Fieldwidth: Max length of the field
    - DataFormat: Either 'Alpha' (alphanumeric), 'Disc' (discrete), or 'Cont' (continuous)
    - imputationvar: Unknown
    - varTitle: Human-readable variable title
    - longDescription: Longer description of the data in the field
    """
    # Added fields
    MODEL_NAMES = (
        ('InstitutionProfile', 'InstitutionProfile'),
    )
    model_name = models.CharField(choices=MODEL_NAMES, max_length=50)

    # Fields from `varlist` tab
    varnumber = models.IntegerField()
    varname = models.CharField(max_length=20)
    DataType = models.CharField(max_length=1)
    Fieldwidth = models.IntegerField()
    DataFormat = models.CharField(max_length=5)
    imputationvar = models.CharField(blank=True, max_length=20)
    varTitle = models.CharField(max_length=200)

    # Fields from `Description` tab
    longDescription = models.TextField()

class InstitutionProfile(models.Model):
    """
    Institution profile data related to `HD<year>.zip` files.
    """
    # Added fields
    year = models.IntegerField()

    # Native fields
    UNITID = models.FloatField()
    INSTNM = models.CharField(max_length=120)
    IALIAS = models.CharField(blank=True, max_length=2000)
    ADDR = models.CharField(blank=True, max_length=100)
    CITY = models.CharField(max_length=30)
    STABBR = models.CharField(max_length=2)
    ZIP = models.CharField(max_length=10)
    FIPS = models.IntegerField()
    OBEREG = models.IntegerField()
    CHFNM = models.CharField(blank=True, max_length=50)
    CHFTITLE = models.CharField(blank=True, max_length=50)
    GENTELE = models.CharField(blank=True, max_length=15)
    EIN = models.CharField(max_length=9)
    DUNS = models.TextField(blank=True)
    OPEID = models.CharField(max_length=8)
    OPEFLAG = models.IntegerField()
    WEBADDR = models.CharField(blank=True, max_length=150)
    ADMINURL = models.CharField(blank=True, max_length=200)
    FAIDURL = models.CharField(blank=True, max_length=200)
    APPLURL = models.CharField(blank=True, max_length=200)
    NPRICURL = models.CharField(blank=True, max_length=200)
    VETURL = models.CharField(blank=True, max_length=200)
    ATHURL = models.CharField(blank=True, max_length=15)
    DISAURL = models.CharField(blank=True, max_length=200)
    SECTOR = models.IntegerField()
    ICLEVEL = models.IntegerField()
    CONTROL = models.IntegerField()
    HLOFFER = models.IntegerField()
    UGOFFER = models.IntegerField()
    GROFFER = models.IntegerField()
    HDEGOFR1 = models.IntegerField()
    DEGGRANT = models.IntegerField()
    HBCU = models.IntegerField()
    HOSPITAL = models.IntegerField()
    MEDICAL = models.IntegerField()
    TRIBAL = models.IntegerField()
    LOCALE = models.IntegerField()
    OPENPUBL = models.IntegerField()
    ACT = models.CharField(max_length=1)
    NEWID = models.FloatField()
    DEATHYR = models.IntegerField()
    CLOSEDAT = models.CharField(max_length=10)
    CYACTIVE = models.IntegerField()
    POSTSEC = models.IntegerField()
    PSEFLAG = models.IntegerField()
    PSET4FLG = models.IntegerField()
    RPTMTH = models.IntegerField()
    INSTCAT = models.IntegerField()
    C18BASIC = models.IntegerField()
    C18IPUG = models.IntegerField()
    C18IPGRD = models.IntegerField()
    C18UGPRF = models.IntegerField()
    C18ENPRF = models.IntegerField()
    C18SZSET = models.IntegerField()
    C15BASIC = models.IntegerField()
    CCBASIC = models.IntegerField()
    CARNEGIE = models.IntegerField()
    LANDGRNT = models.IntegerField()
    INSTSIZE = models.IntegerField()
    F1SYSTYP = models.IntegerField()
    F1SYSNAM = models.CharField(max_length=80)
    F1SYSCOD = models.CharField(max_length=6)
    CBSA = models.IntegerField()
    CBSATYPE = models.IntegerField()
    CSA = models.IntegerField()
    NECTA = models.IntegerField()
    COUNTYCD = models.IntegerField()
    COUNTYNM = models.CharField(blank=True, max_length=30)
    CNGDSTCD = models.IntegerField()
    LONGITUD = models.FloatField()
    LATITUDE = models.FloatField()
    DFRCGID = models.IntegerField()
    DFRCUSCG = models.IntegerField()

    def __str__(self):
        return self.UNITID
        