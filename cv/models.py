from django.db import models
from django.utils.translation import ugettext_lazy as _

EXPERIENCE_TYPES = (
    (None, _('unknown')),
    ('PRACT', _('praktykant')),
    ('ENGEE', _('specjalista/inżynier')),
    ('MANAG', _('kierownik/manager')),
    ('FREEL', _('freelancer')),
    ('OTHER', _('other')),
)
SKILL_LEVELS = (
    (None, _('unknown')),
    ('20', _('familiar')),
    ('40', _('beginner')),
    ('60', _('skilled')),
    ('80', _('advanced')),
    ('100', _('expert')),
)
CATEGORIES = (
    (None, _('unknown')),
    ('DEV', _('programowanie')),
    ('PRO', _('zawodowe')),
    ('OTH', _('inne')),
)
MONTHS = (
    (None, _('unknown')),
    ('01', _('styczeń')),
    ('02', _('luty')),
    ('03', _('marzec')),
    ('04', _('kwiecień')),
    ('05', _('maj')),
    ('06', _('czerwiec')),
    ('07', _('lipiec')),
    ('08', _('sierpień')),
    ('09', _('wrzesień')),
    ('10', _('październik')),
    ('11', _('listopad')),
    ('12', _('grudzień')),
)
class Resume(models.Model):
    firstname = models.CharField(max_length=150, verbose_name=_("First name"))
    lastname = models.CharField(max_length=150, verbose_name=_("Last name"))
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Title"))
    resume = models.TextField(max_length=3000, blank=True, null=True, verbose_name=_("resume"), help_text=_("Short profile's description"))
    image = models.ImageField(blank=True, null=True, verbose_name=_("image"), upload_to="static/pictures/")
    date_birth = models.DateField(blank=True, null=True, verbose_name=_("date of birth"))
    # phone = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("phone"))
    website = models.URLField(max_length=300, blank=True, null=True, verbose_name=_("website"))
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("email"))
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("city"))
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("country"))
    # address = models.CharField(max_length=300, blank=True, null=True, verbose_name=_("address"))

    skill_summary = models.TextField(max_length=1000, blank=True, null=True, verbose_name=_("summary of skills"))
    experience_summary = models.TextField(max_length=1000, blank=True, null=True, verbose_name=_("summary of experience"))
    training_summary = models.TextField(max_length=1000, blank=True, null=True, verbose_name=_("summary of trainings"))
    project_summary = models.TextField(max_length=1000, blank=True, null=True, verbose_name=_("summary of projects"))

    driving_license = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("driving license"))
    hobbies = models.TextField(max_length=1000, blank=True, null=True, verbose_name=_("hobbies"))
    tags = models.CharField(max_length=500, blank=True, null=True, verbose_name=_("tags"))

    # skype = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Skype ID"))
    # twitter = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Twitter"))
    # linkedin = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("LinkedIn ID"))
    # google = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Google+ ID"))
    # stackoverflow = models.IntegerField(blank=True, null=True, verbose_name=_("StackOverflow ID"))
    github = models.CharField(max_length=300, blank=True, null=True, verbose_name=_("GitHub ID"))

    def publish(self):
        self.save()

    def __str__(self):
        return self.firstname

class Education(models.Model):
    # resume = models.ForeignKey("Resume", related_name='trainings')

    school = models.CharField(max_length=150, verbose_name=_("school"))
    degree = models.CharField(max_length=150, verbose_name=_("degree"))
    field = models.CharField(max_length=150, blank=True, verbose_name=_("field"))
    speciality = models.CharField(max_length=150, blank=True, verbose_name=_("speciality"))
    status = models.CharField(max_length=150, blank=True, verbose_name=_("status"))
    thesis = models.TextField(max_length=300, blank=True, verbose_name=_("thesis"))

    year_start = models.IntegerField(null=True, blank=True, verbose_name=_("year_start"))
    month_start = models.CharField(choices=MONTHS, max_length=2, null=True, blank=True, verbose_name=_("month_start"))
    year_end = models.IntegerField(null=True, blank=True, verbose_name=_("year_end"))
    month_end = models.CharField(choices=MONTHS, max_length=2, null=True, blank=True, verbose_name=_("month_end"))

    def publish(self):
        self.save()

    def __str__(self):
        return self.degree

class ResponsibilityItem(models.Model):
    responsibility_description = models.TextField(max_length=300, blank=True, verbose_name=_("responsibility_item"))

    def __str__(self):
        return self.responsibility_description

class Experience(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("title"))
    enterprise = models.CharField(max_length=200, blank=True, verbose_name=_("enterprise"))
    # context = models.TextField(max_length=1000, blank=True, verbose_name=_("context"))
    #responsibility = models.TextField(max_length=3000, blank=True, verbose_name=_("responsibility"))
    responsibility_exp = models.ManyToManyField(ResponsibilityItem)
    #results = models.TextField(max_length=3000, blank=True, verbose_name=_("results"))
    type = models.CharField(choices=EXPERIENCE_TYPES, max_length=5, null=True, verbose_name=_("type"))
    # environment = models.CharField(max_length=400, blank=True, verbose_name=_("environment"))

    start_year = models.IntegerField(verbose_name=_("start year"))
    start_month = models.IntegerField(verbose_name=_("start month"))
    still = models.BooleanField(default=True, verbose_name=_("still in office"))
    end_year = models.IntegerField(null=True, blank=True, verbose_name=_("end year"))
    end_month = models.IntegerField(null=True, blank=True, verbose_name=_("end month"))

    def publish(self):
        self.save()

    def __str__(self):
        return self.enterprise

# class Responsibility(models.Model):
#      experience = models.ForeignKey(Experience, on_delete=models.CASCADE, default=None)
#      responsibility = models.ForeignKey(ResponsibilityItem, on_delete=models.CASCADE)

    # class SkillType(models.Model):
#     name = models.CharField(max_length=200, unique=True, verbose_name=_("name"))
    # description = models.TextField(max_length=2000, blank=True, verbose_name=_("description"))
    # url = models.URLField(max_length=300, blank=True, verbose_name=_("URL"))
    # tags = models.CharField(max_length=500, blank=True, verbose_name=_("tags"))
    # color = models.CharField(max_length=50, blank=True, verbose_name=_("color"))

    # def publish(self):
    #     self.save()
    #
    # def __str__(self):
    #     return self.name
class SkillItem(models.Model):
    # resume = models.ForeignKey("curriculum.Resume", related_name='skills')
    # category = models.ForeignKey('SkillType', related_name='items')
    category = models.CharField(max_length=3, choices=CATEGORIES, null=True, verbose_name='category')
    level = models.CharField(max_length=3, choices=SKILL_LEVELS, verbose_name=_("level"))
    skill = models.CharField(max_length=50, blank=True, verbose_name=_("skill"))

    # start_year = models.IntegerField(choices=utils.YEARS, default=utils.current_year, null=True, blank=True, verbose_name=_("start year"))
    # start_month = models.IntegerField(choices=utils.MONTHS, default=utils.current_month, null=True, blank=True, verbose_name=_("start month"))

    # weight = models.IntegerField(choices=utils.WEIGHTS, default=1, verbose_name=_("weight"))
    def publish(self):
        self.save()

    def __str__(self):
        return self.skill