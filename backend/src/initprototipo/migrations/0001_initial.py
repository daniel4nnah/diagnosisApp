# Generated by Django 4.1.5 on 2023-01-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approl',
            fields=[
                ('roleid', models.AutoField(db_column='RoleId', primary_key=True, serialize=False)),
                ('rolename', models.CharField(db_column='RoleName', max_length=50)),
            ],
            options={
                'db_table': 'AppRol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Appuser',
            fields=[
                ('userid', models.AutoField(db_column='UserId', primary_key=True, serialize=False)),
                ('useremail', models.CharField(blank=True, db_column='UserEmail', max_length=100, null=True)),
                ('userpassword', models.CharField(blank=True, db_column='UserPassword', max_length=100, null=True)),
                ('savedate', models.DateTimeField(blank=True, db_column='SaveDate', null=True)),
                ('changepassworddate', models.DateTimeField(blank=True, db_column='ChangePasswordDate', null=True)),
            ],
            options={
                'db_table': 'AppUser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('consultaid', models.AutoField(db_column='consultaId', primary_key=True, serialize=False)),
                ('fecha_consulta', models.DateTimeField(blank=True, null=True)),
                ('motivo_consulta', models.CharField(blank=True, max_length=100, null=True)),
                ('txtresults', models.CharField(blank=True, db_column='txtResults', max_length=100, null=True)),
                ('idfeto', models.IntegerField(blank=True, db_column='idFeto', null=True)),
            ],
            options={
                'db_table': 'Consulta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('iddiagnostico', models.AutoField(db_column='idDiagnostico', primary_key=True, serialize=False)),
                ('idresultado', models.IntegerField(blank=True, db_column='idResultado', null=True)),
                ('diagnostico', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Diagnostico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feto',
            fields=[
                ('idfeto', models.AutoField(db_column='idFeto', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Feto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Historiaclinica',
            fields=[
                ('idhistoriaclinica', models.AutoField(db_column='idHistoriaClinica', primary_key=True, serialize=False)),
                ('antquirurgico', models.TextField(blank=True, db_column='antQuirurgico', null=True)),
                ('antpatologico', models.TextField(blank=True, db_column='antPatologico', null=True)),
                ('antginecologico', models.TextField(blank=True, db_column='antGinecologico', null=True)),
                ('lmp', models.CharField(blank=True, db_column='LMP', max_length=50, null=True)),
            ],
            options={
                'db_table': 'HistoriaClinica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospitalid', models.IntegerField(db_column='hospitalId', primary_key=True, serialize=False)),
                ('nombrehospital', models.CharField(blank=True, db_column='nombreHospital', max_length=150, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=150, null=True)),
                ('departamento', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'Hospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('institucionid', models.IntegerField(db_column='institucionId', primary_key=True, serialize=False)),
                ('nombreinstitucion', models.CharField(blank=True, db_column='nombreInstitucion', max_length=150, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=150, null=True)),
                ('departamento', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'Institucion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('idmedicion', models.AutoField(db_column='idMedicion', primary_key=True, serialize=False)),
                ('weeksmax', models.CharField(blank=True, db_column='weeksMax', max_length=50, null=True)),
                ('weeksmin', models.CharField(blank=True, db_column='weeksMin', max_length=50, null=True)),
                ('weeksdev', models.CharField(blank=True, db_column='weeksDev', max_length=50, null=True)),
                ('valormin', models.CharField(blank=True, db_column='valorMin', max_length=50, null=True)),
                ('valormax', models.CharField(blank=True, db_column='valorMax', max_length=50, null=True)),
                ('valordev', models.CharField(blank=True, db_column='valorDev', max_length=50, null=True)),
                ('avg', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Medicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idpac', models.AutoField(db_column='idPac', primary_key=True, serialize=False)),
                ('cedulapac', models.IntegerField(blank=True, db_column='cedulaPac', null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=100, null=True)),
                ('nombreuno', models.CharField(blank=True, db_column='nombreUno', max_length=100, null=True)),
                ('nombredos', models.CharField(blank=True, db_column='nombreDos', max_length=100, null=True)),
                ('fechanac', models.CharField(blank=True, db_column='fechaNac', max_length=100, null=True)),
                ('numgestacion', models.IntegerField(blank=True, db_column='numGestacion', null=True)),
            ],
            options={
                'db_table': 'Paciente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patologia',
            fields=[
                ('idpatologia', models.AutoField(db_column='idPatologia', primary_key=True, serialize=False)),
                ('nombrepatologia', models.IntegerField(blank=True, db_column='nombrePatologia', null=True)),
                ('valmin', models.CharField(blank=True, db_column='valMin', max_length=50, null=True)),
                ('valmax', models.CharField(blank=True, db_column='valMax', max_length=50, null=True)),
                ('weeks', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Patologia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personalsalud',
            fields=[
                ('cedulamed', models.IntegerField(db_column='cedulaMed', primary_key=True, serialize=False)),
                ('nombresmed', models.CharField(blank=True, db_column='nombresMed', max_length=150, null=True)),
                ('apellidosmed', models.CharField(blank=True, db_column='apellidosMed', max_length=150, null=True)),
                ('telefonomed', models.CharField(blank=True, db_column='telefonoMed', max_length=50, null=True)),
                ('direccionmed', models.CharField(blank=True, db_column='direccionMed', max_length=200, null=True)),
            ],
            options={
                'db_table': 'PersonalSalud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('idreporte', models.AutoField(db_column='idReporte', primary_key=True, serialize=False)),
                ('efw', models.CharField(blank=True, max_length=100, null=True)),
                ('edb', models.CharField(blank=True, max_length=100, null=True)),
                ('ga', models.CharField(blank=True, max_length=100, null=True)),
                ('csp_1', models.CharField(blank=True, max_length=50, null=True)),
                ('csp_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('cm_1', models.CharField(blank=True, max_length=50, null=True)),
                ('cm_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_1', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_ga', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_edc', models.CharField(blank=True, max_length=50, null=True)),
                ('hc_hadlock_dev', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_1', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_ga', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_edc', models.CharField(blank=True, max_length=50, null=True)),
                ('bdp_hadlock_dev', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_1', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_ga', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_edc', models.CharField(blank=True, max_length=50, null=True)),
                ('cereb_hill_dev', models.CharField(blank=True, max_length=50, null=True)),
                ('va_1', models.CharField(blank=True, max_length=50, null=True)),
                ('va_avg', models.CharField(blank=True, max_length=50, null=True)),
                ('vp_1', models.CharField(blank=True, max_length=50, null=True)),
                ('vp_avg', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Reporte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('idresultado', models.AutoField(db_column='idResultado', primary_key=True, serialize=False)),
                ('result', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Resultado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tipomedicion',
            fields=[
                ('idtipomedicion', models.AutoField(db_column='idTipoMedicion', primary_key=True, serialize=False)),
                ('nombremedicion', models.CharField(blank=True, db_column='nombreMedicion', max_length=150, null=True)),
            ],
            options={
                'db_table': 'TipoMedicion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('unidadid', models.IntegerField(db_column='unidadId', primary_key=True, serialize=False)),
                ('nombreunidad', models.CharField(blank=True, db_column='nombreUnidad', max_length=150, null=True)),
            ],
            options={
                'db_table': 'Unidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarioexterno',
            fields=[
                ('cedulaext', models.IntegerField(db_column='cedulaExt', primary_key=True, serialize=False)),
                ('nombresext', models.CharField(blank=True, db_column='nombresExt', max_length=150, null=True)),
                ('apellidosext', models.CharField(blank=True, db_column='apellidosExt', max_length=150, null=True)),
                ('telefonoext', models.CharField(blank=True, db_column='telefonoExt', max_length=50, null=True)),
                ('direccionext', models.CharField(blank=True, db_column='direccionExt', max_length=200, null=True)),
                ('expirationdate', models.DateTimeField(blank=True, db_column='ExpirationDate', null=True)),
            ],
            options={
                'db_table': 'UsuarioExterno',
                'managed': False,
            },
        ),
    ]
