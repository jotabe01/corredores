from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class REGION(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre_r = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_r
    
class COMUNA(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre_c = models.CharField(max_length=100)
    region = models.ForeignKey(REGION, on_delete=models.CASCADE)    
    
    def __str__(self):
        return self.nombre_c
    
class DIRECCION(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(COMUNA, on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.direccion
    
class TIPO_USUSARIO(models.Model):
    id_tipo_u = models.AutoField(primary_key=True)
    tipo_u = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.tipo_u


class USUARIO(models.Model):
    id_usuario =models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    f_nacimiento= models.DateField()
    email = models.CharField(max_length=100)
    numero_tel= models.CharField(max_length=12)
    foto = models.ImageField(upload_to="usuarios", null=True)
    creador =models.CharField(max_length = 50, null=True, blank=True)
    
   
    id_tipo_u = models.ForeignKey(TIPO_USUSARIO, on_delete= models.CASCADE)
    user =  models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    direccion = models.OneToOneField(DIRECCION, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.nombre
    
    
class TIPO_PROPIEDAD(models.Model):
    id_tipo_p = models.AutoField(primary_key=True)
    tipo_propiedad = models.CharField(max_length = 50)
    
    
    def __str__(self):
        return self.tipo_propiedad
    
class PROPIEDAD(models.Model):
    id_propiedad = models.AutoField(primary_key=True)
    nombre_propiedad = models.CharField(max_length = 50)
    n_habitaciones= models.IntegerField(null = True)
    n_banos = models.IntegerField(null = True)
    precio_arriendo = models.IntegerField(null = True)
    estado = models.BooleanField(null=True)
    descripcion =models.CharField(max_length = 500)
    estacionamiento = models.CharField(max_length = 300)
    fotos = models.ImageField(upload_to="propiedades", null=True)
    m2 = models.DecimalField(max_digits = 7, decimal_places = 3)
    m2_terr = models.DecimalField(max_digits = 7, decimal_places = 3)
    n_rol = models.CharField(max_length = 50)
    anio_const = models.DateField()
    amoblada =models.BooleanField(null = True)
    disponibilidad = models.CharField(max_length = 50)
    enuso =models.CharField(max_length = 50)
    
    tipo_propiedad = models.ForeignKey(TIPO_PROPIEDAD, on_delete = models.CASCADE)
    direccion = models.OneToOneField(DIRECCION, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_propiedad
    
    
class PROPI_USU(models.Model):
    id_propi_usu = models.AutoField(primary_key=True)
    propi_usu = models.CharField(max_length = 50)
    propiedad = models.ForeignKey(PROPIEDAD, on_delete= models.CASCADE)
    usuario = models.ForeignKey(USUARIO, on_delete = models.CASCADE )

    def __str__(self):
        return self.propi_usu


class CONTRATO(models.Model):
    id_contrato= models.AutoField(primary_key=True)
    f_inicio = models.DateField()
    f_termino = models.DateField()
    f_creacion = models.DateField()
    estado_c = models.CharField(max_length = 30)
    reajuste = models.DecimalField(max_digits=4, decimal_places=2)
    firma = models.ImageField(upload_to="propiedades", null=True)
    notario = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 400)
    
    usuario = models.ForeignKey(USUARIO, on_delete = models.CASCADE)
    propiedad = models.ForeignKey(PROPIEDAD, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.descripcion
    
class BOLETA(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    f_emision = models.DateField()
    iva = models.DecimalField(max_digits=4, decimal_places=2)
    total = models.IntegerField()
    
    
class TIPOPAGO(models.Model):
    id_tipo_p = models.AutoField(primary_key=True)
    tipo_p = models.CharField(max_length=50)
    descripcion = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.tipo_p	
    

class EGRESO(models.Model):
    id_egreso = models.AutoField(primary_key=True)
    monto_pago = models.IntegerField()
    estado_pago = models.CharField(max_length=30)
    metodo_pago = models.CharField(max_length=100)
    fechap_inicio = models.DateField()
    fechap = models.DateField()
    fechap_limite = models.DateField()
    receptor = models.CharField(max_length=500)
    
    boleta = models.ForeignKey(BOLETA, on_delete=models.CASCADE)
    tipo_pago = models.ForeignKey(TIPOPAGO, on_delete=models.CASCADE)
    propiedad = models.ForeignKey(PROPIEDAD, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.receptor
    
    
class INGRESO(models.Model):
    id_ingresos = models.AutoField(primary_key=True)
    monto_ingreso = models.IntegerField()
    f_ingreso = models.DateField()
    emisor = models.CharField(max_length=50)
    rut_emisor = models.IntegerField()
    email_emisor = models.CharField(max_length=200, blank=True, null=True)
    
    propiedad = models.ForeignKey(PROPIEDAD, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.emisor
    
    
class OTRO(models.Model):
    id_otros = models.AutoField(primary_key=True)
    nombre_otros = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=300)
    
    propiedad = models.ForeignKey(PROPIEDAD, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_otros

class SERVICIO(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=300)
    
    propiedad = models.ForeignKey(PROPIEDAD, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_servicio
    
class ESPACIOADICIONAL(models.Model):
    id_espacio = models.AutoField(primary_key=True)
    nombre_espacio = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=400)
    
    propiedad = models.ForeignKey(PROPIEDAD, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_espacio