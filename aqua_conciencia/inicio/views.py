from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# =========================
# FUNCIONES GENERALES
# =========================

def inicio(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            return redirect('/panel/')
    return render(request, 'inicio/login.html')

def restablecer(request):
    return render(request, 'inicio/restablecer_contraseña.html')

def crear_cuenta(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        usuario = request.POST['usuario']
        password = request.POST['password']
        User.objects.create_user(username=usuario, email=correo, password=password)
        return redirect('inicio')
    return render(request, 'inicio/creacion_cuenta.html')

def panel(request):
    return render(request, 'inicio/panel.html')

def noticias(request):
    return render(request, 'inicio/noticias.html')

def foro(request):
    return render(request, 'inicio/foro.html')

def perfil(request):
    return render(request, 'inicio/perfil.html')

def configuracion(request):
    return render(request, 'inicio/configuracion.html')

def quiz(request):
    return render(request, 'inicio/quiz.html')

# =========================
# FUNCIÓN AUXILIAR PARA QUIZ
# =========================

def manejar_quiz(request, preguntas, numero, resultado_url, template):
    total = len(preguntas)

    if numero == 1:
        request.session["correctas"] = 0
        request.session["errores"] = []

    pregunta_actual = preguntas[numero - 1]

    if request.method == "POST":
        respuesta = request.POST.get("respuesta")
        if respuesta == pregunta_actual["correcta"]:
            request.session["correctas"] += 1
        else:
            errores = request.session["errores"]
            errores.append({
                "pregunta": pregunta_actual["pregunta"],
                "respuesta_correcta": pregunta_actual["correcta"],
                "explicacion": pregunta_actual["explicacion"]
            })
            request.session["errores"] = errores

        if numero == total:
            return redirect(resultado_url)
        return redirect(request.resolver_match.url_name, numero=numero + 1)

    return render(request, template, {
        "pregunta": pregunta_actual,
        "numero": numero,
        "total": total
    })

# =========================
# QUIZ 1
# =========================

def quiz1(request, numero):
    preguntas = [
    {
        "pregunta": "¿Cuál de estos recursos es indispensable para la vida?",
        "opciones": ["Agua", "Arena", "Petróleo", "Hierro"],
        "correcta": "Agua",
        "explicacion": "El agua es esencial para la vida de todos los seres vivos."
    },
    {
        "pregunta": "¿Qué acción ayuda a ahorrar agua en casa?",
        "opciones": [
            "Cerrar la llave mientras te cepillas los dientes",
            "Dejar correr el agua",
            "Lavar la vereda con manguera todos los días",
            "Jugar con agua durante horas"
        ],
        "correcta": "Cerrar la llave mientras te cepillas los dientes",
        "explicacion": "Cerrar la llave mientras no la usas permite ahorrar muchos litros de agua."
    },
    {
        "pregunta": "¿Quiénes necesitan agua para vivir?",
        "opciones": [
            "Solo las personas",
            "Solo los animales",
            "Solo las plantas",
            "Todos los seres vivos"
        ],
        "correcta": "Todos los seres vivos",
        "explicacion": "Personas, animales y plantas necesitan agua para vivir."
    },
    {
        "pregunta": "¿Cuál de estos lugares contiene agua dulce?",
        "opciones": [
            "Un río",
            "El océano",
            "El mar",
            "La playa"
        ],
        "correcta": "Un río",
        "explicacion": "Los ríos contienen agua dulce, mientras que mares y océanos contienen agua salada."
    },
    {
        "pregunta": "¿Qué debemos hacer si vemos basura cerca de un río?",
        "opciones": [
            "Recogerla y botarla donde corresponde",
            "Empujarla al agua",
            "Ignorarla",
            "Enterrarla en la orilla"
        ],
        "correcta": "Recogerla y botarla donde corresponde",
        "explicacion": "Mantener limpios los ríos ayuda a proteger la naturaleza."
    },
    {
        "pregunta": "¿Cuál de estas acciones contamina el agua?",
        "opciones": [
            "Botar aceite por el lavaplatos",
            "Cerrar la llave",
            "Reciclar",
            "Plantar árboles"
        ],
        "correcta": "Botar aceite por el lavaplatos",
        "explicacion": "El aceite usado contamina grandes cantidades de agua."
    },
    {
        "pregunta": "¿Por qué debemos cuidar el agua?",
        "opciones": [
            "Porque es necesaria para la vida",
            "Porque cambia de color",
            "Porque produce electricidad",
            "Porque reemplaza el aire"
        ],
        "correcta": "Porque es necesaria para la vida",
        "explicacion": "Sin agua no existiría la vida en nuestro planeta."
    },
    {
        "pregunta": "¿Qué animal necesita agua limpia para vivir?",
        "opciones": [
            "Un pez",
            "Un camello",
            "Una gallina",
            "Una hormiga"
        ],
        "correcta": "Un pez",
        "explicacion": "Los peces viven en el agua y necesitan que esté limpia."
    },
    {
        "pregunta": "¿Qué color representa normalmente el agua en mapas y dibujos?",
        "opciones": [
            "Azul",
            "Rojo",
            "Negro",
            "Gris"
        ],
        "correcta": "Azul",
        "explicacion": "El color azul representa ríos, lagos y océanos."
    },
    {
        "pregunta": "¿Cuál es el objetivo principal de AquaConciencia?",
        "opciones": [
            "Enseñar a cuidar el agua y el medioambiente",
            "Vender productos",
            "Hablar solo de animales",
            "Enseñar matemáticas"
        ],
        "correcta": "Enseñar a cuidar el agua y el medioambiente",
        "explicacion": "AquaConciencia busca educar sobre la importancia del agua y su conservación."
    }
]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz1", "inicio/quiz1.html")

def resultado_quiz1(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })

# =========================
# QUIZ 2
# =========================

# =========================
# QUIZ 2 (Turberas y contaminación hídrica en Chiloé)
# =========================

def quiz2(request, numero):
    preguntas = [
    {
        "pregunta": "¿Dónde se encuentra el archipiélago de Chiloé?",
        "opciones": ["Región de Los Lagos", "Región de Atacama", "Región de Arica", "Región de Magallanes"],
        "correcta": "Región de Los Lagos",
        "explicacion": "Chiloé pertenece a la Región de Los Lagos, en el sur de Chile."
    },
    {
        "pregunta": "¿Qué ecosistema de Chiloé almacena grandes cantidades de agua?",
        "opciones": ["Turberas", "Desiertos", "Playas", "Volcanes"],
        "correcta": "Turberas",
        "explicacion": "Las turberas funcionan como enormes esponjas que almacenan agua."
    },
    {
        "pregunta": "¿Por qué es importante cuidar los ríos de Chiloé?",
        "opciones": [
            "Porque entregan agua a personas, animales y plantas",
            "Porque producen petróleo",
            "Porque contienen agua salada",
            "Porque no tienen vida"
        ],
        "correcta": "Porque entregan agua a personas, animales y plantas",
        "explicacion": "Los ríos son fundamentales para la vida de los ecosistemas y las comunidades."
    },
    {
        "pregunta": "¿Cuál de estas acciones contamina un río?",
        "opciones": [
            "Botar basura",
            "Reciclar",
            "Plantar árboles",
            "Ahorrar agua"
        ],
        "correcta": "Botar basura",
        "explicacion": "La basura daña la calidad del agua y afecta a los seres vivos."
    },
    {
        "pregunta": "¿Qué animal vive en ambientes acuáticos y necesita agua limpia?",
        "opciones": [
            "Pez",
            "Cóndor",
            "Caballo",
            "Zorro"
        ],
        "correcta": "Pez",
        "explicacion": "Los peces necesitan agua limpia para sobrevivir."
    },
    {
        "pregunta": "¿Qué debemos hacer con las botellas plásticas después de usarlas?",
        "opciones": [
            "Reciclarlas",
            "Botarlas al río",
            "Quemarlas",
            "Dejarlas en la playa"
        ],
        "correcta": "Reciclarlas",
        "explicacion": "El reciclaje evita que los plásticos lleguen a los ríos y mares."
    },
    {
        "pregunta": "¿Qué sucede cuando el agua está contaminada?",
        "opciones": [
            "Se afectan las plantas, animales y personas",
            "Se vuelve más limpia",
            "Aumenta la cantidad de peces",
            "No ocurre nada"
        ],
        "correcta": "Se afectan las plantas, animales y personas",
        "explicacion": "La contaminación perjudica a todos los seres vivos."
    },
    {
        "pregunta": "¿Qué acción ayuda a proteger el agua?",
        "opciones": [
            "Usar solo el agua necesaria",
            "Dejar la llave abierta",
            "Botar aceite al lavaplatos",
            "Lavar autos en un río"
        ],
        "correcta": "Usar solo el agua necesaria",
        "explicacion": "Usar el agua de forma responsable ayuda a conservar este recurso."
    },
    {
        "pregunta": "¿Cuál es uno de los objetivos de AquaConciencia?",
        "opciones": [
            "Enseñar a cuidar el agua",
            "Vender productos",
            "Enseñar solo historia",
            "Construir carreteras"
        ],
        "correcta": "Enseñar a cuidar el agua",
        "explicacion": "La plataforma busca crear conciencia sobre la importancia del agua."
    },
    {
        "pregunta": "¿Qué beneficio tiene cuidar el agua hoy?",
        "opciones": [
            "Que las futuras generaciones también puedan disfrutarla",
            "Que haya menos lluvia",
            "Que desaparezcan los ríos",
            "Que aumente la contaminación"
        ],
        "correcta": "Que las futuras generaciones también puedan disfrutarla",
        "explicacion": "Cuidar el agua asegura este recurso para las personas del futuro."
    }
]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz2", "inicio/quiz1.html")

def resultado_quiz2(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })

# =========================
# QUIZ 3
# =========================

# =========================
# QUIZ 3 (Ecosistemas de Chiloé y conciencia ambiental)
# =========================

def quiz3(request, numero):
    preguntas = [
    {
        "pregunta": "¿Qué es una cuenca hidrográfica?",
        "opciones": [
            "Un lugar donde el agua de lluvia llega a un mismo río o lago",
            "Un tipo de pez",
            "Una montaña",
            "Una playa"
        ],
        "correcta": "Un lugar donde el agua de lluvia llega a un mismo río o lago",
        "explicacion": "Una cuenca reúne toda el agua que escurre hacia un mismo río, lago o mar."
    },
    {
        "pregunta": "¿Qué ocurre cuando se tala un bosque cerca de un río?",
        "opciones": [
            "Aumenta la erosión del suelo",
            "El agua se vuelve más limpia",
            "No ocurre nada",
            "El río desaparece"
        ],
        "correcta": "Aumenta la erosión del suelo",
        "explicacion": "Los árboles ayudan a sujetar el suelo y evitan que llegue sedimento al río."
    },
    {
        "pregunta": "¿Qué animal necesita agua limpia para sobrevivir?",
        "opciones": [
            "La ranita de Darwin",
            "El camello",
            "El avestruz",
            "El canguro"
        ],
        "correcta": "La ranita de Darwin",
        "explicacion": "La ranita de Darwin vive en ambientes húmedos y necesita agua limpia."
    },
    {
        "pregunta": "¿Por qué es importante cuidar los humedales?",
        "opciones": [
            "Porque almacenan agua y son hogar de muchas especies",
            "Porque producen plástico",
            "Porque generan petróleo",
            "Porque secan los ríos"
        ],
        "correcta": "Porque almacenan agua y son hogar de muchas especies",
        "explicacion": "Los humedales ayudan a conservar el agua y la biodiversidad."
    },
    {
        "pregunta": "¿Cuál de estas acciones ayuda a disminuir la contaminación del agua?",
        "opciones": [
            "Reciclar correctamente",
            "Botar aceite al lavaplatos",
            "Lanzar basura al río",
            "Quemar residuos"
        ],
        "correcta": "Reciclar correctamente",
        "explicacion": "Reciclar evita que muchos residuos lleguen a ríos y mares."
    },
    {
        "pregunta": "¿Qué función cumplen las plantas cercanas a los ríos?",
        "opciones": [
            "Filtran contaminantes y protegen las orillas",
            "Ensucian el agua",
            "Impiden que llueva",
            "Aumentan la contaminación"
        ],
        "correcta": "Filtran contaminantes y protegen las orillas",
        "explicacion": "La vegetación ayuda a mantener el agua más limpia."
    },
    {
        "pregunta": "¿Qué significa usar el agua de manera responsable?",
        "opciones": [
            "Utilizar solo la necesaria y evitar desperdiciarla",
            "Dejar correr la llave",
            "Usarla sin pensar",
            "Gastar toda el agua posible"
        ],
        "correcta": "Utilizar solo la necesaria y evitar desperdiciarla",
        "explicacion": "Cada persona puede ayudar ahorrando agua en su vida diaria."
    },
    {
        "pregunta": "¿Qué sucede si un río está muy contaminado?",
        "opciones": [
            "Las plantas y animales pueden morir",
            "El agua mejora",
            "Aumentan los peces",
            "No ocurre nada"
        ],
        "correcta": "Las plantas y animales pueden morir",
        "explicacion": "La contaminación afecta a todos los seres vivos que dependen del río."
    },
    {
        "pregunta": "¿Cuál de estos lugares almacena grandes cantidades de agua dulce?",
        "opciones": [
            "Las turberas",
            "Los estacionamientos",
            "Las carreteras",
            "Los edificios"
        ],
        "correcta": "Las turberas",
        "explicacion": "Las turberas funcionan como enormes esponjas naturales."
    },
    {
        "pregunta": "¿Qué podemos hacer para cuidar el agua en nuestra escuela?",
        "opciones": [
            "Cerrar bien las llaves y avisar si hay fugas",
            "Dejar correr el agua",
            "Botar basura en el patio",
            "Lavar constantemente las veredas"
        ],
        "correcta": "Cerrar bien las llaves y avisar si hay fugas",
        "explicacion": "Pequeñas acciones ayudan a ahorrar mucha agua."
    }
]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz3", "inicio/quiz1.html")

def resultado_quiz3(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })

# =========================
# QUIZ 4
# =========================

# =========================
# QUIZ 4 (Acciones para cuidar el agua en Chiloé)
# =========================

def quiz4(request, numero):
    preguntas = [
    {
        "pregunta": "¿Qué función cumplen las turberas en Chiloé?",
        "opciones": [
            "Almacenan agua y carbono",
            "Producen electricidad",
            "Generan petróleo",
            "Fabrican oxígeno"
        ],
        "correcta": "Almacenan agua y carbono",
        "explicacion": "Las turberas almacenan grandes cantidades de agua y carbono, ayudando al equilibrio del ecosistema."
    },
    {
        "pregunta": "¿Qué actividad económica de Chiloé puede contaminar el agua si no se controla adecuadamente?",
        "opciones": [
            "Salmonicultura",
            "Apicultura",
            "Artesanía",
            "Turismo rural"
        ],
        "correcta": "Salmonicultura",
        "explicacion": "La salmonicultura puede generar contaminación por residuos y uso de medicamentos."
    },
    {
        "pregunta": "¿Qué ocurre cuando los residuos llegan a un río?",
        "opciones": [
            "Se afecta la vida de plantas y animales",
            "El agua se vuelve potable",
            "Aumenta la biodiversidad",
            "No ocurre nada"
        ],
        "correcta": "Se afecta la vida de plantas y animales",
        "explicacion": "Los residuos contaminan el agua y dañan los ecosistemas acuáticos."
    },
    {
        "pregunta": "¿Cuál de estas acciones ayuda a proteger las turberas?",
        "opciones": [
            "Evitar su extracción",
            "Quemarlas",
            "Construir sobre ellas",
            "Botar basura"
        ],
        "correcta": "Evitar su extracción",
        "explicacion": "Las turberas tardan cientos de años en formarse, por lo que deben protegerse."
    },
    {
        "pregunta": "¿Por qué el agua es importante para los animales?",
        "opciones": [
            "Porque la necesitan para vivir",
            "Porque cambia su color",
            "Porque produce alimentos",
            "Porque reemplaza el aire"
        ],
        "correcta": "Porque la necesitan para vivir",
        "explicacion": "Todos los seres vivos necesitan agua para sobrevivir."
    },
    {
        "pregunta": "¿Qué acción ayuda a mantener limpios los ríos?",
        "opciones": [
            "Recoger la basura",
            "Lanzar envases plásticos",
            "Botar aceite",
            "Verter detergentes"
        ],
        "correcta": "Recoger la basura",
        "explicacion": "Mantener los ríos limpios protege la flora, fauna y la salud de las personas."
    },
    {
        "pregunta": "¿Qué efecto tiene la contaminación del agua sobre los peces?",
        "opciones": [
            "Puede enfermarlos o provocar su muerte",
            "Los hace crecer más",
            "No les afecta",
            "Los vuelve más rápidos"
        ],
        "correcta": "Puede enfermarlos o provocar su muerte",
        "explicacion": "Los contaminantes disminuyen la calidad del agua y afectan a los peces."
    },
    {
        "pregunta": "¿Qué podemos hacer para cuidar el agua en nuestra casa?",
        "opciones": [
            "Reparar llaves que gotean",
            "Dejar correr el agua",
            "Lavar el auto todos los días",
            "Usar la manguera para limpiar"
        ],
        "correcta": "Reparar llaves que gotean",
        "explicacion": "Una pequeña fuga puede desperdiciar mucha agua durante el día."
    },
    {
        "pregunta": "¿Qué significa proteger la biodiversidad?",
        "opciones": [
            "Cuidar todas las especies de seres vivos",
            "Eliminar plantas",
            "Construir más ciudades",
            "Extraer todos los recursos naturales"
        ],
        "correcta": "Cuidar todas las especies de seres vivos",
        "explicacion": "La biodiversidad incluye todos los seres vivos y los ecosistemas donde habitan."
    },
    {
        "pregunta": "¿Cuál es el principal objetivo de AquaConciencia?",
        "opciones": [
            "Educar sobre el cuidado del agua y el medioambiente",
            "Vender productos",
            "Construir carreteras",
            "Extraer recursos naturales"
        ],
        "correcta": "Educar sobre el cuidado del agua y el medioambiente",
        "explicacion": "AquaConciencia busca enseñar de forma interactiva la importancia de proteger el agua."
    }
]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz4", "inicio/quiz1.html")

def resultado_quiz4(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })

# =========================
# QUIZ 5
# =========================

# =========================
# QUIZ 5 (Impactos sociales y económicos de la contaminación hídrica en Chiloé)
# =========================

def quiz5(request, numero):
    preguntas = [
        {
            "pregunta": "¿Qué actividad económica se ve afectada por la contaminación hídrica en Chiloé?",
            "opciones": ["Pesca artesanal", "Minería", "Agricultura de desierto", "Turismo espacial"],
            "correcta": "Pesca artesanal",
            "explicacion": "La contaminación hídrica afecta directamente a la pesca artesanal, base económica de muchas familias."
        },
        {
            "pregunta": "¿Qué impacto tiene la salmonicultura en las comunidades locales?",
            "opciones": ["Genera contaminación", "Mejora la salud", "No tiene impacto", "Reduce la contaminación"],
            "correcta": "Genera contaminación",
            "explicacion": "La salmonicultura libera antibióticos y desechos que contaminan las aguas."
        },
        {
            "pregunta": "¿Qué recurso hídrico se pierde con la explotación de turberas?",
            "opciones": ["Agua dulce", "Petróleo", "Gas natural", "Metales"],
            "correcta": "Agua dulce",
            "explicacion": "Las turberas son reservorios naturales de agua dulce que se pierden al explotarlas."
        },
        {
            "pregunta": "¿Qué efecto social tiene la contaminación hídrica?",
            "opciones": ["Afecta la calidad de vida", "Mejora la educación", "Aumenta la biodiversidad", "No afecta"],
            "correcta": "Afecta la calidad de vida",
            "explicacion": "La contaminación hídrica impacta la salud y bienestar de las comunidades."
        },
        {
            "pregunta": "¿Qué sector económico depende del agua limpia?",
            "opciones": ["Turismo", "Pesca", "Agricultura", "Todos"],
            "correcta": "Todos",
            "explicacion": "Turismo, pesca y agricultura dependen de agua limpia para desarrollarse."
        },
        {
            "pregunta": "¿Qué impacto tiene la pérdida de biodiversidad en Chiloé?",
            "opciones": ["Reduce recursos naturales", "Aumenta la riqueza", "No afecta", "Genera más agua"],
            "correcta": "Reduce recursos naturales",
            "explicacion": "La pérdida de biodiversidad disminuye los recursos disponibles para las comunidades."
        },
        {
            "pregunta": "¿Qué acción comunitaria ayuda a enfrentar la contaminación hídrica?",
            "opciones": ["Educación ambiental", "Explotación indiscriminada", "Deforestación", "Uso excesivo de químicos"],
            "correcta": "Educación ambiental",
            "explicacion": "La educación ambiental fortalece la conciencia y acción comunitaria."
        },
        {
            "pregunta": "¿Qué problema genera la contaminación hídrica en el turismo?",
            "opciones": ["Disminuye visitantes", "Aumenta ingresos", "No afecta", "Mejora la experiencia"],
            "correcta": "Disminuye visitantes",
            "explicacion": "El turismo se ve afectado porque los visitantes buscan ambientes limpios y saludables."
        },
        {
            "pregunta": "¿Qué modelo educativo usa AquaConciencia para abordar estos problemas?",
            "opciones": ["CDIO", "ISO", "ABC", "STEM"],
            "correcta": "CDIO",
            "explicacion": "El proyecto se basa en el modelo CDIO: Concebir, Diseñar, Implementar y Operar."
        },
        {
            "pregunta": "¿Cuál es el objetivo social de AquaConciencia?",
            "opciones": ["Concientizar a estudiantes", "Explotar turberas", "Vender salmones", "Generar energía"],
            "correcta": "Concientizar a estudiantes",
            "explicacion": "El objetivo es educar y concientizar a los estudiantes sobre la importancia del agua."
        }
    ]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz5", "inicio/quiz1.html")

def resultado_quiz5(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })

# =========================
# QUIZ 6
# =========================

# =========================
# QUIZ 6 (Acciones individuales y comunitarias para proteger el agua en Chiloé)
# =========================

def quiz6(request, numero):
    preguntas = [
        {
            "pregunta": "¿Qué acción personal ayuda a ahorrar agua en casa?",
            "opciones": ["Cerrar la llave al cepillarse", "Dejar la llave abierta", "Lavar el auto todos los días", "Regar en exceso"],
            "correcta": "Cerrar la llave al cepillarse",
            "explicacion": "Cerrar la llave mientras te cepillas los dientes ahorra litros de agua diariamente."
        },
        {
            "pregunta": "¿Qué práctica comunitaria ayuda a reducir la contaminación hídrica?",
            "opciones": ["Educación ambiental", "Botar basura al río", "Explotar turberas", "Usar químicos sin control"],
            "correcta": "Educación ambiental",
            "explicacion": "La educación ambiental fortalece la conciencia y acción comunitaria."
        },
        {
            "pregunta": "¿Qué debemos hacer con los residuos peligrosos como aceites o baterías?",
            "opciones": ["Llevarlos a puntos limpios", "Botarlos al río", "Enterrarlos", "Quemarlos"],
            "correcta": "Llevarlos a puntos limpios",
            "explicacion": "Los residuos peligrosos deben reciclarse en puntos limpios para evitar contaminación."
        },
        {
            "pregunta": "¿Qué acción ayuda a proteger las turberas?",
            "opciones": ["Evitar su explotación", "Quemarlas", "Usarlas como vertedero", "Drenarlas"],
            "correcta": "Evitar su explotación",
            "explicacion": "Las turberas deben conservarse porque almacenan agua y carbono."
        },
        {
            "pregunta": "¿Qué recurso debemos cuidar para mantener la vida?",
            "opciones": ["Agua", "Plástico", "Petróleo", "Carbón"],
            "correcta": "Agua",
            "explicacion": "El agua es vital para todos los seres vivos."
        },
        {
            "pregunta": "¿Qué acción reduce la contaminación de ríos?",
            "opciones": ["No botar basura", "Usar pesticidas", "Explotar turberas", "Verter químicos"],
            "correcta": "No botar basura",
            "explicacion": "Evitar botar basura en ríos protege la biodiversidad acuática."
        },
        {
            "pregunta": "¿Qué estrategia propone AquaConciencia para enseñar sobre el agua?",
            "opciones": ["Mapa interactivo", "Películas", "Canciones", "Deportes"],
            "correcta": "Mapa interactivo",
            "explicacion": "La plataforma usa un mapa interactivo para mostrar zonas afectadas."
        },
        {
            "pregunta": "¿Qué modelo educativo guía AquaConciencia?",
            "opciones": ["CDIO", "ISO", "ABC", "STEM"],
            "correcta": "CDIO",
            "explicacion": "El proyecto se basa en el modelo CDIO: Concebir, Diseñar, Implementar y Operar."
        },
        {
            "pregunta": "¿Qué beneficio aporta AquaConciencia a los estudiantes?",
            "opciones": ["Conciencia ambiental temprana", "Más contaminación", "Menos biodiversidad", "Explotación de recursos"],
            "correcta": "Conciencia ambiental temprana",
            "explicacion": "Busca que los estudiantes comprendan la importancia de cuidar el agua desde pequeños."
        },
        {
            "pregunta": "¿Qué acción comunitaria ayuda a proteger los ecosistemas de Chiloé?",
            "opciones": ["Participar en limpiezas de playas y ríos", "Botar basura", "Explotar turberas", "Usar químicos sin control"],
            "correcta": "Participar en limpiezas de playas y ríos",
            "explicacion": "Las limpiezas comunitarias ayudan a reducir la contaminación y proteger los ecosistemas."
        }
    ]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz6", "inicio/quiz1.html")

def resultado_quiz6(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })
# =========================
# QUIZ 7 (Impactos ecológicos en Chiloé)
# =========================

def quiz7(request, numero):
    preguntas = [
        {
            "pregunta": "¿Qué ecosistema de Chiloé se ve más afectado por la explotación de turberas?",
            "opciones": ["Humedales", "Desiertos", "Playas", "Volcanes"],
            "correcta": "Humedales",
            "explicacion": "Las turberas forman parte de los humedales y su explotación altera el equilibrio hídrico."
        },
        {
            "pregunta": "¿Qué especie marina se ve afectada por la contaminación salmonera?",
            "opciones": ["Moluscos y peces nativos", "Leones marinos", "Ballenas", "Pingüinos"],
            "correcta": "Moluscos y peces nativos",
            "explicacion": "Los desechos de la salmonicultura afectan directamente a moluscos y peces nativos."
        },
        {
            "pregunta": "¿Qué impacto tiene la contaminación hídrica en la biodiversidad?",
            "opciones": ["Reduce especies", "Aumenta peces", "Mejora ecosistemas", "No afecta"],
            "correcta": "Reduce especies",
            "explicacion": "La contaminación disminuye la biodiversidad y afecta el equilibrio ecológico."
        },
        {
            "pregunta": "¿Qué recurso natural se pierde con la explotación de turberas?",
            "opciones": ["Agua dulce", "Petróleo", "Gas natural", "Metales"],
            "correcta": "Agua dulce",
            "explicacion": "Las turberas son reservorios naturales de agua dulce."
        },
        {
            "pregunta": "¿Qué ecosistema ayuda a almacenar carbono en Chiloé?",
            "opciones": ["Turberas", "Desiertos", "Bosques secos", "Playas"],
            "correcta": "Turberas",
            "explicacion": "Las turberas almacenan grandes cantidades de carbono, regulando el clima."
        },
        {
            "pregunta": "¿Qué problema ambiental genera la salmonicultura?",
            "opciones": ["Contaminación de aguas", "Purificación de ríos", "Aumento de oxígeno", "Mejora de ecosistemas"],
            "correcta": "Contaminación de aguas",
            "explicacion": "La salmonicultura libera antibióticos y desechos que contaminan el agua."
        },
        {
            "pregunta": "¿Qué acción humana afecta la fauna de Chiloé?",
            "opciones": ["Explotación de turberas", "Reforestación", "Educación ambiental", "Turismo sustentable"],
            "correcta": "Explotación de turberas",
            "explicacion": "La explotación de turberas destruye hábitats de fauna local."
        },
        {
            "pregunta": "¿Qué ecosistema se ve alterado por la contaminación hídrica?",
            "opciones": ["Ríos y mares", "Desiertos", "Montañas secas", "Glaciares"],
            "correcta": "Ríos y mares",
            "explicacion": "La contaminación hídrica afecta directamente ríos y mares de Chiloé."
        },
        {
            "pregunta": "¿Qué especie emblemática de Chiloé depende de aguas limpias?",
            "opciones": ["Chorito", "Cóndor", "Zorro chilote", "Canguro"],
            "correcta": "Chorito",
            "explicacion": "El chorito es una especie emblemática que depende de aguas limpias para sobrevivir."
        },
        {
            "pregunta": "¿Cuál es el objetivo ecológico de AquaConciencia?",
            "opciones": ["Concientizar sobre ecosistemas", "Explotar turberas", "Vender salmones", "Generar energía"],
            "correcta": "Concientizar sobre ecosistemas",
            "explicacion": "El objetivo es educar sobre la importancia de los ecosistemas y el agua en Chiloé."
        }
    ]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz7", "inicio/quiz1.html")

def resultado_quiz7(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })
# =========================
# QUIZ 8 (Educación ambiental y participación comunitaria en Chiloé)
# =========================

def quiz8(request, numero):
    preguntas = [
        {
            "pregunta": "¿Qué acción comunitaria ayuda a reducir la contaminación hídrica?",
            "opciones": ["Participar en limpiezas de playas y ríos", "Botar basura", "Explotar turberas", "Usar químicos sin control"],
            "correcta": "Participar en limpiezas de playas y ríos",
            "explicacion": "Las limpiezas comunitarias ayudan a reducir la contaminación y proteger los ecosistemas."
        },
        {
            "pregunta": "¿Qué práctica fomenta la conciencia ambiental en estudiantes?",
            "opciones": ["Educación ambiental", "Deforestación", "Contaminación", "Explotación indiscriminada"],
            "correcta": "Educación ambiental",
            "explicacion": "La educación ambiental permite que los estudiantes comprendan la importancia de cuidar el agua."
        },
        {
            "pregunta": "¿Qué recurso natural es el foco principal de AquaConciencia?",
            "opciones": ["Agua", "Petróleo", "Carbón", "Hierro"],
            "correcta": "Agua",
            "explicacion": "El agua es el recurso vital que AquaConciencia busca proteger."
        },
        {
            "pregunta": "¿Qué acción personal ayuda a cuidar el agua?",
            "opciones": ["Cerrar la llave al cepillarse", "Dejar la llave abierta", "Lavar el auto todos los días", "Botar químicos al río"],
            "correcta": "Cerrar la llave al cepillarse",
            "explicacion": "Cerrar la llave mientras te cepillas los dientes ahorra litros de agua diariamente."
        },
        {
            "pregunta": "¿Qué estrategia educativa usa AquaConciencia?",
            "opciones": ["Mapa interactivo", "Películas", "Canciones", "Deportes"],
            "correcta": "Mapa interactivo",
            "explicacion": "La plataforma usa un mapa interactivo para mostrar zonas afectadas."
        },
        {
            "pregunta": "¿Qué modelo educativo guía AquaConciencia?",
            "opciones": ["CDIO", "ISO", "ABC", "STEM"],
            "correcta": "CDIO",
            "explicacion": "El proyecto se basa en el modelo CDIO: Concebir, Diseñar, Implementar y Operar."
        },
        {
            "pregunta": "¿Qué acción comunitaria ayuda a proteger las turberas?",
            "opciones": ["Evitar su explotación", "Quemarlas", "Usarlas como vertedero", "Drenarlas"],
            "correcta": "Evitar su explotación",
            "explicacion": "Las turberas deben conservarse porque almacenan agua y carbono."
        },
        {
            "pregunta": "¿Qué beneficio aporta AquaConciencia a los estudiantes?",
            "opciones": ["Conciencia ambiental temprana", "Más contaminación", "Menos biodiversidad", "Explotación de recursos"],
            "correcta": "Conciencia ambiental temprana",
            "explicacion": "Busca que los estudiantes comprendan la importancia de cuidar el agua desde pequeños."
        },
        {
            "pregunta": "¿Qué acción comunitaria fortalece la participación ciudadana?",
            "opciones": ["Charlas y talleres ambientales", "Botar basura", "Explotar turberas", "Usar químicos sin control"],
            "correcta": "Charlas y talleres ambientales",
            "explicacion": "Las charlas y talleres fomentan la participación ciudadana en temas ambientales."
        },
        {
            "pregunta": "¿Cuál es el objetivo social de AquaConciencia?",
            "opciones": ["Concientizar a estudiantes", "Explotar turberas", "Vender salmones", "Generar energía"],
            "correcta": "Concientizar a estudiantes",
            "explicacion": "El objetivo es educar y concientizar a los estudiantes sobre la importancia del agua."
        }
    ]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz8", "inicio/quiz1.html")

def resultado_quiz8(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })
# =========================
# QUIZ 9 (Problemas ambientales globales vs Chiloé)
# =========================

def quiz9(request, numero):
    preguntas = [
        {
            "pregunta": "¿Qué problema ambiental global se relaciona con la contaminación hídrica en Chiloé?",
            "opciones": ["Cambio climático", "Deforestación", "Ruido urbano", "Contaminación lumínica"],
            "correcta": "Cambio climático",
            "explicacion": "La contaminación hídrica contribuye al cambio climático al alterar ecosistemas y ciclos naturales."
        },
        {
            "pregunta": "¿Qué ecosistema global es similar a las turberas de Chiloé?",
            "opciones": ["Humedales", "Desiertos", "Glaciares", "Montañas secas"],
            "correcta": "Humedales",
            "explicacion": "Las turberas son humedales que almacenan agua y carbono, presentes en distintas partes del mundo."
        },
        {
            "pregunta": "¿Qué industria genera contaminación hídrica tanto en Chiloé como en otros países?",
            "opciones": ["Salmonicultura", "Agricultura intensiva", "Minería", "Todas"],
            "correcta": "Todas",
            "explicacion": "La salmonicultura, agricultura intensiva y minería generan contaminación hídrica en distintos lugares."
        },
        {
            "pregunta": "¿Qué recurso natural se ve afectado globalmente por la contaminación hídrica?",
            "opciones": ["Agua dulce", "Petróleo", "Carbón", "Hierro"],
            "correcta": "Agua dulce",
            "explicacion": "El agua dulce es un recurso limitado y afectado en todo el mundo."
        },
        {
            "pregunta": "¿Qué acción global ayuda a enfrentar la contaminación hídrica?",
            "opciones": ["Educación ambiental", "Explotación indiscriminada", "Deforestación", "Uso excesivo de químicos"],
            "correcta": "Educación ambiental",
            "explicacion": "La educación ambiental es clave para enfrentar la contaminación hídrica a nivel global."
        },
        {
            "pregunta": "¿Qué impacto social genera la contaminación hídrica en comunidades locales y globales?",
            "opciones": ["Afecta la salud y calidad de vida", "Mejora la economía", "No afecta", "Genera más biodiversidad"],
            "correcta": "Afecta la salud y calidad de vida",
            "explicacion": "La contaminación hídrica impacta la salud y bienestar de las comunidades en todo el mundo."
        },
        {
            "pregunta": "¿Qué ecosistema global almacena carbono como las turberas?",
            "opciones": ["Bosques tropicales", "Humedales", "Manglares", "Todos"],
            "correcta": "Todos",
            "explicacion": "Bosques tropicales, humedales y manglares almacenan carbono y regulan el clima."
        },
        {
            "pregunta": "¿Qué problema ambiental global se compara con la salmonicultura en Chiloé?",
            "opciones": ["Agricultura intensiva", "Deforestación", "Contaminación del aire", "Contaminación lumínica"],
            "correcta": "Agricultura intensiva",
            "explicacion": "La agricultura intensiva genera impactos similares a la salmonicultura: contaminación y pérdida de biodiversidad."
        },
        {
            "pregunta": "¿Qué acción internacional busca proteger el agua?",
            "opciones": ["Convenios ambientales", "Explotación indiscriminada", "Uso excesivo de plásticos", "Deforestación"],
            "correcta": "Convenios ambientales",
            "explicacion": "Los convenios internacionales buscan proteger el agua y los ecosistemas."
        },
        {
            "pregunta": "¿Cuál es el objetivo de comparar problemas globales con los de Chiloé?",
            "opciones": ["Concientizar sobre la conexión local-global", "Explotar más recursos", "Ignorar la contaminación", "Generar energía fósil"],
            "correcta": "Concientizar sobre la conexión local-global",
            "explicacion": "Comparar problemas ayuda a entender que la contaminación hídrica es un desafío mundial con impactos locales."
        }
    ]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz9", "inicio/quiz1.html")

def resultado_quiz9(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })
# =========================
# QUIZ 10 (Acciones futuras y sostenibilidad en Chiloé)
# =========================

def quiz10(request, numero):
    preguntas = [
        {
            "pregunta": "¿Qué podemos hacer para que haya agua limpia en el futuro?",
            "opciones": ["Cuidar ríos y lagos", "Botar basura", "Usar químicos sin control", "Explotar turberas"],
            "correcta": "Cuidar ríos y lagos",
            "explicacion": "Si cuidamos ríos y lagos, aseguramos agua limpia para las próximas generaciones."
        },
        {
            "pregunta": "¿Qué energía ayuda a cuidar el planeta?",
            "opciones": ["Solar y eólica", "Carbón", "Petróleo", "Plásticos"],
            "correcta": "Solar y eólica",
            "explicacion": "Las energías renovables como la solar y la eólica no contaminan el agua ni el aire."
        },
        {
            "pregunta": "¿Qué acción comunitaria ayuda a un futuro más limpio?",
            "opciones": ["Reciclaje", "Quemar basura", "Botar plásticos al mar", "Explotar turberas"],
            "correcta": "Reciclaje",
            "explicacion": "Reciclar reduce la contaminación y protege los ecosistemas."
        },
        {
            "pregunta": "¿Qué debemos hacer para proteger los animales de Chiloé?",
            "opciones": ["Cuidar sus hábitats", "Botar basura", "Contaminar ríos", "Usar químicos sin control"],
            "correcta": "Cuidar sus hábitats",
            "explicacion": "Si cuidamos los hábitats, los animales pueden vivir seguros y saludables."
        },
        {
            "pregunta": "¿Qué recurso natural debemos proteger para el futuro?",
            "opciones": ["Agua", "Plástico", "Carbón", "Petróleo"],
            "correcta": "Agua",
            "explicacion": "El agua es vital para la vida y debemos protegerla."
        },
        {
            "pregunta": "¿Qué acción ayuda a reducir el uso de plásticos?",
            "opciones": ["Usar bolsas reutilizables", "Botar plásticos al mar", "Quemar plásticos", "Usar más desechables"],
            "correcta": "Usar bolsas reutilizables",
            "explicacion": "Las bolsas reutilizables evitan que los plásticos contaminen ríos y mares."
        },
        {
            "pregunta": "¿Qué podemos hacer para que los niños aprendan a cuidar el agua?",
            "opciones": ["Educación ambiental", "Ignorar el problema", "Contaminar ríos", "Explotar turberas"],
            "correcta": "Educación ambiental",
            "explicacion": "La educación ambiental enseña a los niños la importancia de cuidar el agua."
        },
        {
            "pregunta": "¿Qué acción ayuda a que haya más árboles en el futuro?",
            "opciones": ["Reforestación", "Deforestación", "Quemar bosques", "Usar químicos sin control"],
            "correcta": "Reforestación",
            "explicacion": "Plantar árboles ayuda a mantener el aire limpio y proteger el agua."
        },
        {
            "pregunta": "¿Qué podemos hacer para que el turismo en Chiloé sea sustentable?",
            "opciones": ["No contaminar playas y ríos", "Botar basura", "Explotar turberas", "Usar químicos sin control"],
            "correcta": "No contaminar playas y ríos",
            "explicacion": "El turismo sustentable cuida los lugares naturales y atrae visitantes responsables."
        },
        {
            "pregunta": "¿Por qué es importante pensar en el futuro del agua?",
            "opciones": ["Porque asegura la vida", "Porque no sirve", "Porque sobra", "Porque es infinita"],
            "correcta": "Porque asegura la vida",
            "explicacion": "El agua es indispensable para la vida presente y futura."
        }
    ]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz10", "inicio/quiz1.html")

def resultado_quiz10(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })
# =========================
# QUIZ 11 (Flora y fauna de Chiloé y su relación con el agua)
# =========================

def quiz11(request, numero):
    preguntas = [
        {
            "pregunta": "¿Qué animal marino de Chiloé necesita aguas limpias para vivir?",
            "opciones": ["Chorito", "Cóndor", "Zorro chilote", "Canguro"],
            "correcta": "Chorito",
            "explicacion": "El chorito es una especie emblemática que depende de aguas limpias."
        },
        {
            "pregunta": "¿Qué ave de Chiloé habita en humedales y zonas costeras?",
            "opciones": ["Cisne de cuello negro", "Pingüino emperador", "Águila", "Gaviota australiana"],
            "correcta": "Cisne de cuello negro",
            "explicacion": "El cisne de cuello negro vive en humedales y depende de agua limpia."
        },
        {
            "pregunta": "¿Qué ecosistema de Chiloé es hogar de muchas aves y anfibios?",
            "opciones": ["Turberas", "Desiertos", "Glaciares", "Volcanes"],
            "correcta": "Turberas",
            "explicacion": "Las turberas son ecosistemas que albergan aves y anfibios únicos."
        },
        {
            "pregunta": "¿Qué mamífero marino se encuentra en las costas de Chiloé?",
            "opciones": ["Lobo marino", "Elefante africano", "Caballo", "Canguro"],
            "correcta": "Lobo marino",
            "explicacion": "Los lobos marinos habitan en las costas de Chiloé y dependen de mares limpios."
        },
        {
            "pregunta": "¿Qué planta típica de Chiloé crece en ambientes húmedos?",
            "opciones": ["Nalca", "Cactus", "Palmera", "Pino del desierto"],
            "correcta": "Nalca",
            "explicacion": "La nalca es una planta típica de Chiloé que crece en zonas húmedas."
        },
        {
            "pregunta": "¿Qué animal chilote está en peligro si se contaminan los ríos?",
            "opciones": ["Ranita de Darwin", "León", "Tigre", "Caballo"],
            "correcta": "Ranita de Darwin",
            "explicacion": "La ranita de Darwin vive en ríos y humedales, y necesita agua limpia."
        },
        {
            "pregunta": "¿Qué ave migratoria visita Chiloé en busca de alimento?",
            "opciones": ["Flamenco chileno", "Águila real", "Cóndor", "Pato mandarín"],
            "correcta": "Flamenco chileno",
            "explicacion": "El flamenco chileno llega a humedales de Chiloé para alimentarse."
        },
        {
            "pregunta": "¿Qué especie de pez se ve afectada por la contaminación salmonera?",
            "opciones": ["Peces nativos", "Ballenas", "Caballos de mar", "Tiburones blancos"],
            "correcta": "Peces nativos",
            "explicacion": "Los peces nativos se ven desplazados por la contaminación de la salmonicultura."
        },
        {
            "pregunta": "¿Qué árbol típico de Chiloé ayuda a mantener el suelo húmedo?",
            "opciones": ["Canelo", "Palmera", "Cactus", "Pino"],
            "correcta": "Canelo",
            "explicacion": "El canelo es un árbol nativo que ayuda a conservar la humedad del suelo."
        },
        {
            "pregunta": "¿Por qué es importante cuidar la fauna y flora de Chiloé?",
            "opciones": ["Porque mantienen el equilibrio de la naturaleza", "Porque no sirven", "Porque son infinitos", "Porque no afectan"],
            "correcta": "Porque mantienen el equilibrio de la naturaleza",
            "explicacion": "La flora y fauna son esenciales para el equilibrio de los ecosistemas."
        }
    ]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz11", "inicio/quiz1.html")

def resultado_quiz11(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })
# =========================
# QUIZ 12 (Acciones diarias para cuidar el agua y el medioambiente)
# =========================

def quiz12(request, numero):
    preguntas = [
        {
            "pregunta": "¿Qué podemos hacer al lavarnos los dientes para ahorrar agua?",
            "opciones": ["Cerrar la llave", "Dejar la llave abierta", "Usar más agua", "Llenar la bañera"],
            "correcta": "Cerrar la llave",
            "explicacion": "Cerrar la llave mientras te cepillas ahorra muchos litros de agua."
        },
        {
            "pregunta": "¿Dónde debemos botar las botellas plásticas?",
            "opciones": ["En el reciclaje", "En el río", "En la playa", "En la turbera"],
            "correcta": "En el reciclaje",
            "explicacion": "Las botellas plásticas deben ir al reciclaje para no contaminar el agua."
        },
        {
            "pregunta": "¿Qué acción ayuda a cuidar los ríos?",
            "opciones": ["No botar basura", "Lavar ropa en el río", "Tirar químicos", "Explotar turberas"],
            "correcta": "No botar basura",
            "explicacion": "Si no botamos basura, los ríos se mantienen limpios y saludables."
        },
        {
            "pregunta": "¿Qué podemos hacer para cuidar la energía en casa?",
            "opciones": ["Apagar la luz cuando no se usa", "Dejar las luces encendidas", "Usar más aparatos eléctricos", "Abrir el refrigerador todo el día"],
            "correcta": "Apagar la luz cuando no se usa",
            "explicacion": "Apagar las luces ahorra energía y ayuda al medioambiente."
        },
        {
            "pregunta": "¿Qué acción ayuda a reducir el uso de plásticos?",
            "opciones": ["Usar bolsas reutilizables", "Botar plásticos al mar", "Usar más desechables", "Quemar plásticos"],
            "correcta": "Usar bolsas reutilizables",
            "explicacion": "Las bolsas reutilizables evitan que los plásticos contaminen ríos y mares."
        },
        {
            "pregunta": "¿Qué podemos hacer para cuidar los árboles?",
            "opciones": ["Plantar más árboles", "Cortarlos sin necesidad", "Quemar bosques", "Ignorarlos"],
            "correcta": "Plantar más árboles",
            "explicacion": "Plantar árboles ayuda a mantener el aire limpio y proteger el agua."
        },
        {
            "pregunta": "¿Qué acción comunitaria ayuda a cuidar el medioambiente?",
            "opciones": ["Participar en limpiezas de playas y ríos", "Botar basura", "Explotar turberas", "Usar químicos sin control"],
            "correcta": "Participar en limpiezas de playas y ríos",
            "explicacion": "Las limpiezas comunitarias reducen la contaminación y protegen los ecosistemas."
        },
        {
            "pregunta": "¿Qué debemos hacer con el aceite usado de la cocina?",
            "opciones": ["Llevarlo a un punto limpio", "Botarlo al río", "Enterrarlo", "Tirarlo en la calle"],
            "correcta": "Llevarlo a un punto limpio",
            "explicacion": "El aceite usado contamina el agua, debe reciclarse en puntos limpios."
        },
        {
            "pregunta": "¿Qué podemos hacer para cuidar el agua al regar plantas?",
            "opciones": ["Regar en la mañana o tarde", "Regar al mediodía con sol fuerte", "Usar mucha agua siempre", "Dejar la manguera abierta"],
            "correcta": "Regar en la mañana o tarde",
            "explicacion": "Regar en horas frescas evita que el agua se evapore rápido."
        },
        {
            "pregunta": "¿Por qué es importante cuidar el agua todos los días?",
            "opciones": ["Porque es vital para la vida", "Porque sobra", "Porque no sirve", "Porque es infinita"],
            "correcta": "Porque es vital para la vida",
            "explicacion": "El agua es indispensable para todos los seres vivos."
        }
    ]
    return manejar_quiz(request, preguntas, numero, "resultado_quiz12", "inicio/quiz1.html")

def resultado_quiz12(request):
    correctas = request.session.get("correctas", 0)
    errores = request.session.get("errores", [])
    return render(request, "inicio/resultado_quiz.html", {
        "correctas": correctas,
        "errores": errores,
        "total": 10
    })

