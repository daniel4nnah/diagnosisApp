# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Approl(models.Model):
    roleid = models.AutoField(db_column='RoleId', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppRol'


class Appuser(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEmail', max_length=100, blank=True, null=True)  # Field name made lowercase.
    userpassword = models.CharField(db_column='UserPassword', max_length=100, blank=True, null=True)  # Field name made lowercase.
    savedate = models.DateTimeField(db_column='SaveDate', blank=True, null=True)  # Field name made lowercase.
    changepassworddate = models.DateTimeField(db_column='ChangePasswordDate', blank=True, null=True)  # Field name made lowercase.
    userroleid = models.ForeignKey(Approl, models.DO_NOTHING, db_column='UserRoleId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AppUser'

class Hospital(models.Model):
    hospitalid = models.IntegerField(db_column='hospitalId', primary_key=True)  # Field name made lowercase.
    nombrehospital = models.CharField(db_column='nombreHospital', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(max_length=150, blank=True, null=True)
    departamento = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Hospital'


class Institucion(models.Model):
    institucionid = models.IntegerField(db_column='institucionId', primary_key=True)  # Field name made lowercase.
    nombreinstitucion = models.CharField(db_column='nombreInstitucion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(max_length=150, blank=True, null=True)
    departamento = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Institucion'


class Medicion(models.Model):
    idmedicion = models.AutoField(db_column='idMedicion', primary_key=True)  # Field name made lowercase.
    weeksmax = models.CharField(db_column='weeksMax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weeksmin = models.CharField(db_column='weeksMin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weeksdev = models.CharField(db_column='weeksDev', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valormin = models.CharField(db_column='valorMin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valormax = models.CharField(db_column='valorMax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valordev = models.CharField(db_column='valorDev', max_length=50, blank=True, null=True)  # Field name made lowercase.
    avg = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Medicion'


class Paciente(models.Model):
    idpac = models.AutoField(db_column='idPac', primary_key=True)  # Field name made lowercase.
    cedulapac = models.IntegerField(db_column='cedulaPac', blank=True, null=True)  # Field name made lowercase.
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=100, blank=True, null=True)
    nombreuno = models.CharField(db_column='nombreUno', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nombredos = models.CharField(db_column='nombreDos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechanac = models.CharField(db_column='fechaNac', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numgestacion = models.IntegerField(db_column='numGestacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Paciente'

class Personalsalud(models.Model):
    cedulamed = models.IntegerField(db_column='cedulaMed', primary_key=True)  # Field name made lowercase.
    nombresmed = models.CharField(db_column='nombresMed', max_length=150, blank=True, null=True)  # Field name made lowercase.
    apellidosmed = models.CharField(db_column='apellidosMed', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefonomed = models.CharField(db_column='telefonoMed', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccionmed = models.CharField(db_column='direccionMed', max_length=200, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Appuser, models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='HospitalId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonalSalud'


class Reporte(models.Model):
    idreporte = models.AutoField(db_column='idReporte', primary_key=True)  # Field name made lowercase.
    efw = models.CharField(max_length=100, blank=True, null=True)
    edb = models.CharField(max_length=100, blank=True, null=True)
    ga = models.CharField(max_length=100, blank=True, null=True)
    csp_1 = models.CharField(max_length=50, blank=True, null=True)
    csp_avg = models.CharField(max_length=50, blank=True, null=True)
    cm_1 = models.CharField(max_length=50, blank=True, null=True)
    cm_avg = models.CharField(max_length=50, blank=True, null=True)
    hc_hadlock_1 = models.CharField(max_length=50, blank=True, null=True)
    hc_hadlock_avg = models.CharField(max_length=50, blank=True, null=True)
    hc_hadlock_ga = models.CharField(max_length=50, blank=True, null=True)
    hc_hadlock_edc = models.CharField(max_length=50, blank=True, null=True)
    hc_hadlock_dev = models.CharField(max_length=50, blank=True, null=True)
    bdp_hadlock_1 = models.CharField(max_length=50, blank=True, null=True)
    bdp_hadlock_avg = models.CharField(max_length=50, blank=True, null=True)
    bdp_hadlock_ga = models.CharField(max_length=50, blank=True, null=True)
    bdp_hadlock_edc = models.CharField(max_length=50, blank=True, null=True)
    bdp_hadlock_dev = models.CharField(max_length=50, blank=True, null=True)
    cereb_hill_1 = models.CharField(max_length=50, blank=True, null=True)
    cereb_hill_avg = models.CharField(max_length=50, blank=True, null=True)
    cereb_hill_ga = models.CharField(max_length=50, blank=True, null=True)
    cereb_hill_edc = models.CharField(max_length=50, blank=True, null=True)
    cereb_hill_dev = models.CharField(max_length=50, blank=True, null=True)
    va_1 = models.CharField(max_length=50, blank=True, null=True)
    va_avg = models.CharField(max_length=50, blank=True, null=True)
    vp_1 = models.CharField(max_length=50, blank=True, null=True)
    vp_avg = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reporte'

class Consulta(models.Model):
    consultaid = models.AutoField(db_column='consultaId', primary_key=True)  # Field name made lowercase.
    fecha_consulta = models.DateTimeField(blank=True, null=True)
    motivo_consulta = models.CharField(max_length=100, blank=True, null=True)
    txtresults = models.CharField(db_column='txtResults', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cedulamed = models.ForeignKey('Personalsalud', models.DO_NOTHING, db_column='cedulaMed', blank=True, null=True)  # Field name made lowercase.
    idpac = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idPac', blank=True, null=True)  # Field name made lowercase.
    idfeto = models.IntegerField(db_column='idFeto', blank=True, null=True)  # Field name made lowercase.
    idreporte = models.ForeignKey('Reporte', models.DO_NOTHING, db_column='idReporte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Consulta'

class Patologia(models.Model):
    idpatologia = models.AutoField(db_column='idPatologia', primary_key=True)  # Field name made lowercase.
    nombrepatologia = models.IntegerField(db_column='nombrePatologia', blank=True, null=True)  # Field name made lowercase.
    valmin = models.CharField(db_column='valMin', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valmax = models.CharField(db_column='valMax', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weeks = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Patologia'


class Diagnostico(models.Model):
    iddiagnostico = models.AutoField(db_column='idDiagnostico', primary_key=True)  # Field name made lowercase.
    idresultado = models.IntegerField(db_column='idResultado', blank=True, null=True)  # Field name made lowercase.
    diagnostico = models.TextField(blank=True, null=True)
    idpatologia = models.ForeignKey('Patologia', models.DO_NOTHING, db_column='idPatologia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Diagnostico'


class Feto(models.Model):
    idfeto = models.AutoField(db_column='idFeto', primary_key=True)  # Field name made lowercase.
    idpac = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='idPac', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Feto'
        unique_together = (('idpac', 'idfeto'),)


class Historiaclinica(models.Model):
    idhistoriaclinica = models.AutoField(db_column='idHistoriaClinica', primary_key=True)  # Field name made lowercase.
    antquirurgico = models.TextField(db_column='antQuirurgico', blank=True, null=True)  # Field name made lowercase.
    antpatologico = models.TextField(db_column='antPatologico', blank=True, null=True)  # Field name made lowercase.
    antginecologico = models.TextField(db_column='antGinecologico', blank=True, null=True)  # Field name made lowercase.
    lmp = models.CharField(db_column='LMP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    idconsulta = models.ForeignKey(Consulta, models.DO_NOTHING, db_column='idConsulta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HistoriaClinica'


class Resultado(models.Model):
    idresultado = models.AutoField(db_column='idResultado', primary_key=True)  # Field name made lowercase.
    idreporte = models.ForeignKey(Reporte, models.DO_NOTHING, db_column='idReporte', blank=True, null=True)  # Field name made lowercase.
    idmedicion = models.ForeignKey(Medicion, models.DO_NOTHING, db_column='idMedicion', blank=True, null=True)  # Field name made lowercase.
    result = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Resultado'


class Tipomedicion(models.Model):
    idtipomedicion = models.AutoField(db_column='idTipoMedicion', primary_key=True)  # Field name made lowercase.
    nombremedicion = models.CharField(db_column='nombreMedicion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoMedicion'


class Unidad(models.Model):
    unidadid = models.IntegerField(db_column='unidadId', primary_key=True)  # Field name made lowercase.
    nombreunidad = models.CharField(db_column='nombreUnidad', max_length=150, blank=True, null=True)  # Field name made lowercase.
    hospitalid = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='hospitalId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Unidad'


class Usuarioexterno(models.Model):
    cedulaext = models.IntegerField(db_column='cedulaExt', primary_key=True)  # Field name made lowercase.
    nombresext = models.CharField(db_column='nombresExt', max_length=150, blank=True, null=True)  # Field name made lowercase.
    apellidosext = models.CharField(db_column='apellidosExt', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefonoext = models.CharField(db_column='telefonoExt', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccionext = models.CharField(db_column='direccionExt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Appuser, models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    institutionid = models.ForeignKey(Institucion, models.DO_NOTHING, db_column='InstitutionId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UsuarioExterno'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
