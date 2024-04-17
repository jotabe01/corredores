# Generated by Django 4.2.5 on 2024-03-27 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BOLETA',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('f_emision', models.DateField()),
                ('iva', models.DecimalField(decimal_places=2, max_digits=4)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='COMUNA',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_c', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DIRECCION',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=100)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='PROPIEDAD',
            fields=[
                ('id_propiedad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_propiedad', models.CharField(max_length=50)),
                ('n_habitaciones', models.IntegerField(null=True)),
                ('n_banos', models.IntegerField(null=True)),
                ('precio_arriendo', models.IntegerField(null=True)),
                ('estado', models.BooleanField(null=True)),
                ('descripcion', models.CharField(max_length=500)),
                ('estacionamiento', models.CharField(max_length=300)),
                ('fotos', models.ImageField(null=True, upload_to='propiedades')),
                ('m2', models.DecimalField(decimal_places=3, max_digits=7)),
                ('m2_terr', models.DecimalField(decimal_places=3, max_digits=7)),
                ('n_rol', models.CharField(max_length=50)),
                ('anio_const', models.DateField()),
                ('amoblada', models.BooleanField(null=True)),
                ('disponibilidad', models.CharField(max_length=50)),
                ('enuso', models.CharField(max_length=50)),
                ('direccion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='arriendos.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='REGION',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_r', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TIPO_PROPIEDAD',
            fields=[
                ('id_tipo_p', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_propiedad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TIPO_USUSARIO',
            fields=[
                ('id_tipo_u', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_u', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TIPOPAGO',
            fields=[
                ('id_tipo_p', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_p', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='USUARIO',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=12)),
                ('f_nacimiento', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('numero_tel', models.CharField(max_length=12)),
                ('foto', models.ImageField(null=True, upload_to='usuarios')),
                ('creador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios_creados', to='arriendos.usuario')),
                ('direccion', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='arriendos.direccion')),
                ('id_tipo_u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.tipo_ususario')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SERVICIO',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=300)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.propiedad')),
            ],
        ),
        migrations.AddField(
            model_name='propiedad',
            name='tipo_propiedad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.tipo_propiedad'),
        ),
        migrations.CreateModel(
            name='PROPI_USU',
            fields=[
                ('id_propi_usu', models.AutoField(primary_key=True, serialize=False)),
                ('propi_usu', models.CharField(max_length=50)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.propiedad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='OTRO',
            fields=[
                ('id_otros', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_otros', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=300)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.propiedad')),
            ],
        ),
        migrations.CreateModel(
            name='INGRESO',
            fields=[
                ('id_ingresos', models.AutoField(primary_key=True, serialize=False)),
                ('monto_ingreso', models.IntegerField()),
                ('f_ingreso', models.DateField()),
                ('emisor', models.CharField(max_length=50)),
                ('rut_emisor', models.IntegerField()),
                ('email_emisor', models.CharField(blank=True, max_length=200, null=True)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.propiedad')),
            ],
        ),
        migrations.CreateModel(
            name='ESPACIOADICIONAL',
            fields=[
                ('id_espacio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_espacio', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=400)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.propiedad')),
            ],
        ),
        migrations.CreateModel(
            name='EGRESO',
            fields=[
                ('id_egreso', models.AutoField(primary_key=True, serialize=False)),
                ('monto_pago', models.IntegerField()),
                ('estado_pago', models.CharField(max_length=30)),
                ('metodo_pago', models.CharField(max_length=100)),
                ('fechap_inicio', models.DateField()),
                ('fechap', models.DateField()),
                ('fechap_limite', models.DateField()),
                ('receptor', models.CharField(max_length=500)),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.boleta')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.propiedad')),
                ('tipo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.tipopago')),
            ],
        ),
        migrations.CreateModel(
            name='CONTRATO',
            fields=[
                ('id_contrato', models.AutoField(primary_key=True, serialize=False)),
                ('f_inicio', models.DateField()),
                ('f_termino', models.DateField()),
                ('f_creacion', models.DateField()),
                ('estado_c', models.CharField(max_length=30)),
                ('reajuste', models.DecimalField(decimal_places=2, max_digits=4)),
                ('firma', models.ImageField(null=True, upload_to='propiedades')),
                ('notario', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=400)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.propiedad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arriendos.region'),
        ),
    ]
