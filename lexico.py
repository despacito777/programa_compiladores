# funciones de identificaciones
# indentificador reservadas
def indf_reservadas(palabra):
  if(palabra == 'print'):
    return True
  elif(palabra == 'write'):
    return True
  elif(palabra == 'while'):
    return True
  elif(palabra == 'for'):
    return True
  elif(palabra == 'string'):
    return True
  elif(palabra == 'int'):
    return True
  elif(palabra == 'float'):
    return True
  elif(palabra == 'char'):
    return True
  else:
    return False

# identificador numero
def indf_numero(palabra):
  try:
    val = int(palabra)
    return True
  except ValueError:
    return False

# identificador general
def indf_general(palabra):
  if(indf_numero(palabra)): # puede ser n caracteres (terminado)
    return 'numero'
  elif(indf_reservadas(palabra)): # puede ser n caracteres (terminado)
    return 'reservada'
  elif(palabra == ' '): # debe ser de 1 caracter (terminado)
    return 'espacio'
  elif(palabra == ';'): # debe ser de 1 caracter (terminado)
    return 'separador'
  elif(palabra == ''): # valores invalidos (terminado)
    return 'vacio'
  else: # puede ser n caracteres (terminado)
    return 'palabra'


# programa
while(True):
  oracion = raw_input("Ingresa una sentencia: ")

  # variables acumuladores, registros
  # listados de simbolos, operadores, y otros
  list_reservadas = []
  list_numeros = []
  list_palabras = []

  # listado de tipos de datos
  list_string = []
  list_int = []
  list_char = []
  list_float = []

  # contadores
  no_espacios = 0
  no_separadores = 0

  # registros
  reg_palabra = ''
  reg_tipodato = ''
  reg_infdato = ''

  #estados
  estado_dato = '0'
  estado_palabra = ''

  long_oracion = len(oracion)

  # separacion de letras
  for letra in oracion:
    reg_palabra = reg_palabra + letra
    estado_palabra = 'completa'

    # ---------------------------------------------- reservadas seccion (terminada)
    if((indf_general(reg_palabra) == 'reservada') and estado_palabra != 'total'):
      list_reservadas.append(reg_palabra)

      if(reg_palabra == 'string'):
        reg_tipodato = reg_palabra
        estado_dato = '1'
      elif(reg_palabra == 'int'):
        reg_tipodato = reg_palabra
        estado_dato = '1'
      elif(reg_palabra == 'float'):
        reg_tipodato = reg_palabra
        estado_dato = '1'
      elif(reg_palabra == 'char'):
        reg_tipodato = reg_palabra
        estado_dato = '1'

      reg_palabra = ''
      estado_palabra = 'total'
    
    # ---------------------------------------------- tipodato seccion (terminada)
    if(reg_tipodato and estado_dato == '1'):
      if(letra == "="):
        if(reg_infdato):
          estado_dato = '2'
        else:
          estado_dato = '2'
          reg_palabra = reg_palabra[:-1]
          
          if (indf_general(reg_palabra) == 'palabra'):
            list_palabras.append(reg_palabra)
            reg_infdato = reg_palabra

      if(letra == ";"):
        estado_dato = '0'

    # ---------------------------------------------- espacio seccion (terminada)
    if((indf_general(letra) == 'espacio') and estado_palabra != 'total'):
      no_espacios = no_espacios + 1

      reg_palabra = reg_palabra[:-1]

      # asignar separacion
      if(indf_general(reg_palabra) == 'numero'):
        list_numeros.append(reg_palabra)
      elif (indf_general(reg_palabra) == 'palabra'):
        list_palabras.append(reg_palabra)
      
      # tipos de datos
      if(estado_dato == '1' and (not indf_general(reg_palabra) == 'vacio' or not indf_general(reg_palabra) == 'espacio')):
        reg_infdato = reg_palabra
      
      estado_palabra = 'total'
      reg_palabra = ''

    # ---------------------------------------------- separador seccion (terminada)
    if((indf_general(letra) == 'separador') and estado_palabra != 'total'):
      no_separadores = no_separadores + 1

      reg_palabra = reg_palabra[:-1]

      # asignar separacion
      if(indf_general(reg_palabra) == 'numero'):
        list_numeros.append(reg_palabra)
      elif (indf_general(reg_palabra) == 'palabra'):
        list_palabras.append(reg_palabra)

      # tipos de datos
      if(estado_dato == '2'):
        if(reg_tipodato == 'string'):
          list_string.append(reg_infdato+" = "+reg_palabra)
        elif(reg_tipodato == 'int'):
          list_int.append(reg_infdato+" = "+reg_palabra)
        elif(reg_tipodato == 'float'):
          list_float.append(reg_infdato+" = "+reg_palabra)
        elif(reg_tipodato == 'char'):
          list_char.append(reg_infdato+" = "+reg_palabra)

      estado_palabra = 'total'
      reg_palabra = ''
      
  #cuando se acaba la iteracion
  if(indf_general(reg_palabra) == 'numero'):
    list_numeros.append(reg_palabra)
  elif(indf_general(reg_palabra) == 'palabra'):
    list_palabras.append(reg_palabra)

  # mostrar datos
  if(len(list_reservadas) > 0):
    print('')
    print('Reservadas')
    for item in list_reservadas:
      print(item)

  if(len(list_numeros) > 0):
    print('')
    print('Numeros')
    for item in list_numeros:
      print(item)

  if(len(list_palabras) > 0):
    print('')
    print('Palabras')
    for item in list_palabras:
      print(item)
  
  if(no_espacios > 0):
    print('')
    print('No. de espacios: '+str(no_espacios))
  
  if(no_separadores > 0):
    print('')
    print('No. de (;): '+str(no_separadores))
  
  # mostrar listado tipos de datos
  if(len(list_float) > 0):
    print('')
    print('Float')
    for item in list_float:
      print(item)
  
  if(len(list_char) > 0):
    print('')
    print('Char')
    for item in list_char:
      print(item)
  
  if(len(list_int) > 0):
    print('')
    print('Int')
    for item in list_int:
      print(item)
  
  if(len(list_string) > 0):
    print('')
    print('String')
    for item in list_string:
      print(item)
  
  print('')
    