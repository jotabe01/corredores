from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from datetime import datetime
from django.http import HttpResponse
from functools import wraps


## validación de paginas por usuario
def corredor_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated  and request.user.usuario.id_tipo_u.id_tipo_u == 1:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("No tienes permiso para acceder a esta página.")
    return wrapper

def arrend_required(view_func2):
    @wraps(view_func2)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated  and request.user.usuario.id_tipo_u.id_tipo_u == 2:
            return view_func2(request, *args, **kwargs)
        else:
            return HttpResponse("No tienes permiso para acceder a esta página.")
    return wrapper


def index(request):


    return render(request, 'arriendos/index.html')

##Funciones Corredor

@corredor_required
@login_required(login_url='/inicio_s')
def dashboard(request):
    usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/dashboard.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')

@corredor_required
@login_required(login_url='/inicio_s')
def propiedades(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/propiedades.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    
@corredor_required
@login_required(login_url='/inicio_s')
def addpropiedad(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/addpropiedad.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    

@corredor_required
@login_required(login_url='/inicio_s')
def addpropietario(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/addpropietario.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    
@corredor_required
@login_required(login_url='/inicio_s')
def addarrendatario(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/addarrendatario.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    

@corredor_required
@login_required(login_url='/inicio_s')
def detallepropiedad(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/detallepropiedad.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    

@corredor_required
@login_required(login_url='/inicio_s')
def detallearrendatario(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/detallearrendatario.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    

@corredor_required
@login_required(login_url='/inicio_s')
def detallepropietario(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/detallepropietario.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    

@corredor_required
@login_required(login_url='/inicio_s')
def pagar(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/pagar.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    

@corredor_required    
@login_required(login_url='/inicio_s')
def propietarios(request):
    usuario = get_object_or_404(USUARIO, user=request.user)
    usuarios = USUARIO.objects.all()
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        contexto ={
            'usuario':usuario,
            'usuarios':usuarios,
            
            }
        return render(request, 'arriendos/propietarios.html', contexto)
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    
    
@corredor_required   
@login_required(login_url='/inicio_s')
def arrendatarios(request):
    usuario = get_object_or_404(USUARIO, user=request.user)
    usuarios = USUARIO.objects.all()
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        contexto ={
            'usuario':usuario,
            'usuarios':usuarios
        }
        return render(request, 'arriendos/arrendatarios.html',contexto)
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    
@corredor_required    
@login_required(login_url='/inicio_s')
def finanzas(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/finanzas.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')

@corredor_required    
@login_required(login_url='/inicio_s')
def perfilu(request):
    tipos_usuarios = TIPO_USUSARIO.objects.all()
    contexto = {
        'tipos_usuarios': tipos_usuarios
    }
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/perfilu.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    

@corredor_required    
@login_required(login_url='/inicio_s')
def detallepago(request):
    tipos_usuarios = TIPO_USUSARIO.objects.all()
    contexto = {
        'tipos_usuarios': tipos_usuarios
    }
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/detallepago.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    

@corredor_required    
@login_required(login_url='/inicio_s')
def detallepagocorredor(request):
    tipos_usuarios = TIPO_USUSARIO.objects.all()
    contexto = {
        'tipos_usuarios': tipos_usuarios
    }
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/detallepagocorredor.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')


@corredor_required    
@login_required(login_url='/inicio_s')
def contactanos(request):
    tipos_usuarios = TIPO_USUSARIO.objects.all()
    contexto = {
        'tipos_usuarios': tipos_usuarios
    }
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/contactanos.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    
@corredor_required     
@login_required(login_url='/inicio_s')
def contratos(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/contratos.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    
@corredor_required     
@login_required(login_url='/inicio_s')
def addcontrato(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/addcontrato.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
    



def wallet(request):
    
    
    return render(request,'arriendos/wallet.html')


def registro(request):
    tipos_usuarios = TIPO_USUSARIO.objects.all()
    contexto = {
        'tipos_usuarios': tipos_usuarios
    }
    return render (request, 'arriendos/sign-up.html', contexto)

def tables(request):
    return render (request, 'arriendos/tables.html')

def calcular_edad(fecha_nacimiento):
    fecha_nac = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nac.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day))
    return edad

def registrar(request):
    nombre_u = request.POST['nombre']
    apellidos_u = request.POST['apellidos']
    rut_u = request.POST['rut']
    fecha_nacimiento = request.POST['f_nacimiento']
    correo_u = request.POST['correo']
    numero_u = request.POST['numero_tel']
    tipo_u = request.POST['tipo_usuario']
    contraseña_u = request.POST['Contraseña']
    contraseña_conf = request.POST['Contraseña1']
    creador_u = request.user
   

    edad_usuario = calcular_edad(fecha_nacimiento)

    if edad_usuario < 18:
        messages.error(request, 'Debes tener al menos 18 años para registrarte', extra_tags="alert-danger")
        return redirect('index')
    else:
        if 'imagen_us' in request.FILES:
                imagen_u = request.FILES['imagen_us']
        else:
            imagen_u = 'usuarios\\avatar.jpg'
        tip_o = TIPO_USUSARIO.objects.get(id_tipo_u = tipo_u) #al ser foranea debe ser extraida de la otra tabala
   
        try:
            b=USUARIO.objects.get(email=correo_u)
            messages.error(request,'El correo no esta disponible',extra_tags="alert-danger")
            return redirect('index')
        except USUARIO.DoesNotExist:
            user1 = User.objects.create_user(correo_u, correo_u, contraseña_u)
            user1.is_staff = 0
            user1.save() 
            if contraseña_conf == contraseña_u:
            
            
                a=USUARIO.objects.create(nombre= nombre_u, apellidos = apellidos_u, rut = rut_u,f_nacimiento=fecha_nacimiento,email=correo_u,numero_tel = numero_u, id_tipo_u = tip_o, foto =imagen_u, user = user1, creador = creador_u)
                messages.success(request,'Usuario registrado',extra_tags="alert-success")
        
                return redirect('index')
                
            else:
                messages.error(request,'La contraseña no coinside',extra_tags="alert-danger")    
                return redirect('index')         


##Funciones arrendartario 

@arrend_required    
@login_required(login_url='/inicio_s')
def view_arrend(request):
    usuario = usuario = get_object_or_404(USUARIO, user=request.user)
    # Verifica si el usuario autenticado es dueño del perfil
    if usuario.user == request.user:
        # El usuario tiene acceso al perfil
        return render(request, 'arriendos/view-arrend.html', {'usuario': usuario})
    else:
        # El usuario no tiene permiso para ver este perfil
        return render(request, 'arriendos/index.html')
        
        
    
## Funciones Login y Log out
def logout_view(request):
    logout(request)
    return redirect('index')
    
def inicio_s(request):
    return render(request, 'arriendos/sign-in.html')

def login_view(request):
    username_u = request.POST['username_i']
    password_u = request.POST['password']
    user = authenticate(username = username_u, password = password_u)

    if user is not None:
        if user.is_active:
            login(request,user)
            messages.success(request,'Bienvenido '+username_u+ ', has iniciado sesion ', extra_tags='alert-success')
            if user.usuario.id_tipo_u.id_tipo_u == 1:  
                return redirect('dashboard')
            elif user.usuario.id_tipo_u.id_tipo_u == 2:
                return redirect('view_arrend')
            elif user.usuario.id_tipo_u.id_tipo_u == 3:
                return redirect('index')
        else:
            messages.error(request,'Usuario inactivo', extra_tags='alert-danger')
    else:
        messages.error(request,'El nombre de usuario y la contraseña que ingresaste no coinciden con nuestros registros. Por favor, revisa e inténtalo de nuevo.', extra_tags='alert-danger')
    return redirect('inicio_s')


