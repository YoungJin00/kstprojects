from django.db import models
from django.conf import settings


class UserManagerAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    manager_id = models.CharField(max_length=50)
    manager_password = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'User_manager_account'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Businessschedule(models.Model):
    businessschedule_number = models.AutoField(db_column='businessSchedule_number', primary_key=True)  # Field name made lowercase.
    software_product_family_number = models.ForeignKey('SoftwareProductFamily', models.DO_NOTHING, db_column='software_product_family_number')
    manager_number = models.ForeignKey('Manager', models.DO_NOTHING, db_column='manager_number')
    counsellingtype_number = models.ForeignKey('Counselingtype', models.DO_NOTHING, db_column='counsellingType_number')  # Field name made lowercase.
    businessschedule_title = models.CharField(db_column='businessSchedule_title', max_length=20)  # Field name made lowercase.
    businessschedule_content = models.TextField(db_column='businessSchedule_content')  # Field name made lowercase.
    businessschedule_plandate = models.DateTimeField(db_column='businessSchedule_planDate')  # Field name made lowercase.
    businessschedule_regidate = models.DateTimeField(db_column='businessSchedule_regiDate')  # Field name made lowercase.
    businessschedule_updatedate = models.DateTimeField(db_column='businessSchedule_updateDate')  # Field name made lowercase.
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'businessSchedule'


class Counseling(models.Model):
    counseling_number = models.AutoField(primary_key=True)
    manager_number = models.ForeignKey('Manager', models.DO_NOTHING, db_column='manager_number')
    counsellingtype_number = models.ForeignKey('Counselingtype', models.DO_NOTHING, db_column='counsellingType_number')  # Field name made lowercase.
    institution_number = models.ForeignKey('Institution', models.DO_NOTHING, db_column='institution_number')
    software_product_family_number = models.ForeignKey('SoftwareProductFamily', models.DO_NOTHING, db_column='software_product_family_number')
    counseling_title = models.CharField(max_length=20)
    counseling_content = models.TextField()
    counseling_processing_phase = models.CharField(max_length=10)
    counseling_processing_content = models.CharField(max_length=10)
    counseling_note = models.CharField(max_length=255)
    counseling_processing_date = models.DateTimeField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counseling'


class Counselingtype(models.Model):
    counselingtype_number = models.AutoField(db_column='counselingType_number', primary_key=True)  # Field name made lowercase.
    counselingtype_largecategory = models.CharField(db_column='counselingType_largeCategory', max_length=10)  # Field name made lowercase.
    counselingtype_smallcategory = models.CharField(db_column='counselingType_smallCategory', max_length=10)  # Field name made lowercase.
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counselingType'


class CounselingManual(models.Model):
    counseling_manual_number = models.AutoField(primary_key=True)
    manager_number = models.ForeignKey('Manager', models.DO_NOTHING, db_column='manager_number')
    counseling_manual_title = models.CharField(max_length=30)
    counseling_manual_content = models.CharField(max_length=1024, blank=True, null=True)
    counseling_manual_creation_date = models.DateTimeField(blank=True, null=True)
    counseling_manual_revision_date = models.DateTimeField(blank=True, null=True)
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counseling_manual'


class CounselingManualComment(models.Model):
    counseling_manual_comment_number = models.AutoField(primary_key=True)
    manager_number = models.ForeignKey('Manager', models.DO_NOTHING, db_column='manager_number')
    counseling_manual_number = models.ForeignKey(CounselingManual, models.DO_NOTHING, db_column='counseling_manual_number')
    counseling_manual_comment_content = models.CharField(max_length=1024, blank=True, null=True)
    counseling_manual_comment_creation_date = models.DateTimeField(blank=True, null=True)
    counseling_manual_comment_revision_date = models.DateTimeField(blank=True, null=True)
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counseling_manual_comment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Institution(models.Model):
    institution_number = models.AutoField(primary_key=True)
    manager_number = models.ForeignKey('Manager', models.DO_NOTHING, db_column='manager_number')
    software_product_family_number = models.ForeignKey('SoftwareProductFamily', models.DO_NOTHING, db_column='software_product_family_number')
    institution_name = models.CharField(max_length=50, db_collation='utf8_general_ci')
    institutional_representative_name = models.CharField(max_length=20)
    institutional_phonenumber = models.CharField(max_length=20)
    institutional_representative_phonenumber = models.CharField(max_length=20)
    institutional_address = models.CharField(max_length=50)
    institutional_representative_mail = models.CharField(max_length=20)
    institutional_type = models.IntegerField()
    program_use = models.IntegerField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institution'


class Manager(models.Model):
    manager_number = models.AutoField(primary_key=True)
    manager_division = models.CharField(max_length=15)
    manager_position = models.CharField(max_length=15)
    manager_name = models.CharField(max_length=20)
    manager_picture_url = models.CharField(max_length=512)
    manager_phonenumber = models.CharField(max_length=100)
    manager_emergency_phonenumber = models.CharField(max_length=100)
    manager_email = models.CharField(max_length=100)
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class ManagerAccount(models.Model):
    manager_account_number = models.AutoField(primary_key=True)
    manager_number = models.ForeignKey(Manager, models.DO_NOTHING, db_column='manager_number')
    manager_id = models.CharField(max_length=30)
    manager_password = models.CharField(max_length=50)
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager_account'


class Notice(models.Model):
    notice_number = models.AutoField(primary_key=True)
    software_product_family_number = models.ForeignKey('SoftwareProductFamily', models.DO_NOTHING, db_column='software_product_family_number')
    manager_number = models.ForeignKey(Manager, models.DO_NOTHING, db_column='manager_number')
    notice_title = models.CharField(max_length=100)
    notice_content = models.TextField()
    notice_attachmentlink = models.CharField(db_column='notice_attachmentLink', max_length=1024)  # Field name made lowercase.
    notice_creationdate = models.DateTimeField(db_column='notice_creationDate')  # Field name made lowercase.
    notice_updatedate = models.DateTimeField(db_column='notice_updateDate')  # Field name made lowercase.
    notice_views = models.IntegerField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notice'


class SoftwareProductFamily(models.Model):
    software_product_family_number = models.AutoField(primary_key=True)
    software_product_family_type = models.CharField(max_length=40)
    software_product_family_name = models.CharField(max_length=40)
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software_product_family'


class SoftwareUpdate(models.Model):
    software_update_number = models.AutoField(primary_key=True)
    manager_number = models.ForeignKey(Manager, models.DO_NOTHING, db_column='manager_number')
    software_product_family_number = models.ForeignKey(SoftwareProductFamily, models.DO_NOTHING, db_column='software_product_family_number')
    software_update_title = models.CharField(max_length=50)
    software_update_content = models.CharField(max_length=1024)
    software_update_creation_date = models.DateTimeField()
    software_update_revision_date = models.DateTimeField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software_update'


class Statisticsprocessingstage(models.Model):
    statisticsprocessingstage_number = models.AutoField(db_column='statisticsProcessingStage_number', primary_key=True)  # Field name made lowercase.
    counseling_processing_phase = models.CharField(max_length=10)
    contact_history_count = models.IntegerField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statisticsProcessingStage'


class StatisticsDate(models.Model):
    statistics_date_number = models.AutoField(primary_key=True)
    contact_date = models.DateField()
    contact_history_count = models.IntegerField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistics_date'


class StatisticsInstitution(models.Model):
    statistics_institution = models.AutoField(primary_key=True)
    institution_number = models.ForeignKey(Institution, models.DO_NOTHING, db_column='institution_number')
    contact_history_count = models.IntegerField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistics_institution'


class StatisticsSoftwareProductFamily(models.Model):
    statistics_software_product_family_number = models.AutoField(primary_key=True)
    software_product_family_number = models.ForeignKey(SoftwareProductFamily, models.DO_NOTHING, db_column='software_product_family_number')
    contact_history_count = models.IntegerField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistics_software_product_family'


class StatisticsType(models.Model):
    statistics_type = models.AutoField(primary_key=True)
    counselingtype_number = models.ForeignKey(Counselingtype, models.DO_NOTHING, db_column='counselingType_number')  # Field name made lowercase.
    contact_history_count = models.IntegerField()
    information_creation_date = models.DateTimeField(blank=True, null=True)
    information_revision_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statistics_type'



























