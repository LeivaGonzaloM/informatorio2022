from django.views import generic
from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages


# ----- vistas principales ----- #

def Principal(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'miscelaneo/about.html')

def mision(request):
    return render(request, 'miscelaneo/mision.html')

def vision(request):
    return render(request, 'miscelaneo/vision.html')

def galeria(request):
    return render(request, 'miscelaneo/galeria.html')

def contacto(request):
    return render(request, 'miscelaneo/contacto.html')

# ----- vistas de categorías ----- #

def listarCategoria(request):
    categorias = Categoria.objects.all()
    return render(request, "categoria/listar_categoria.html", {'categorias': categorias})

def crearCategoria(request):
    formulario = CategoriaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listarcategorias')
    return render(request, "categoria/crear_categoria.html", {'formulario': formulario})

def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('listarcategorias')

def editarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    formulario = CategoriaForm(request.POST or None, request.FILES or None, instance=categoria)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listarcategorias')
    return render(request, "categoria/modificar_categoria.html", {'formulario': formulario})

# ----- vistas de noticias ----- #

def listarNoticias(request):
    noticias = Noticia.objects.all().order_by('-fechaPublicacion')
    return render(request, "noticia/listar_noticias.html", {'noticias': noticias})

# def crearNoticia(request):
#     formulario = NoticiaForm(request.POST or None, request.FILES or None)
#     if formulario.is_valid():
#         formulario.save()
#         return redirect('listarNoticias')
#     return render(request, "noticia/crear_noticia.html", {'formulario': formulario})

class CrearNoticia(generic.CreateView):
    model = Noticia
    template_name = 'noticia/crear_noticia.html'
    form_class = NoticiaForm

    def get_success_url(self):
        return reverse('crear-noticia')

def eliminarNoticia(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    return redirect('listarNoticias')

def editarNoticia(request, id):
    noticia = Noticia.objects.get(id=id)
    formulario = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listarnoticias')
    return render(request, "noticia/modificar_noticia.html", {'formulario': formulario})

# ----- vistas de Personas ----- #

def listaPersonas(request):
    listaPersonas = Persona.objects.all()
    return render(request, "persona/listar_persona.html", {'listaPersonas': listaPersonas})

def crearPersona(request):
    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        detalleUsuario=Persona(username=username, email=email, password=password)
        email_exists = (Persona.objects.filter(email = email))
        user_exists = (Persona.objects.filter(username = username))
        if user_exists:
            messages.success(request, 'El nombre de usuario' + request.POST['username']+' ya existe.')
            return redirect('/crearPersona')
        elif email_exists:
            messages.success(request, 'El correo electrónico ' + request.POST['email']+' ya existe.')
            return redirect('/crearPersona')
        else:
            Persona(username=username, email=email, password=password).save()
            request.session['email']=detalleUsuario.email
            return redirect('inicio')        
    else:
        return render(request, 'persona/crear_persona.html')
  
def eliminarPersona(request, id):
    noticia = Noticia.objects.get(id=id)
    noticia.delete()
    return redirect('listaPersonas')

def editarPersona(request, id):
    noticia = Noticia.objects.get(id=id)
    formulario = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listaPersonas')
    return render(request, "persona/modificar_persona.html", {'formulario': formulario})

# ----- vistas de Comentarios ----- #

# ver como sería ....

# ----- vistas de Sesión ----- #

def login(request):
    if request.method=="POST":
        try:
            detalleUsuario=Persona.objects.get(email=request.POST['email'], password=request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['email']=detalleUsuario.email
            return render(request, 'base/index.html')
        except Persona.DoesNotExist as e:
            messages.success(request, 'Nombre de usuraio o Contraseña incorrecto')
    return render(request, 'sesion/login.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return render(request, 'base/index.html')
    return render(request, 'base/index.html')

