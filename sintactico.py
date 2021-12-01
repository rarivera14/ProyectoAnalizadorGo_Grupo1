import ply.yacc as yacc

from lexer import tokens


# William Venegas
def p_golang(p):
    ''' golang : asignacion
              | expression
              | condicional
              | bucleFor
              | funcion
              | imports
              | array
              | metodosPropiedadesArray
              | print
              | switch
              | map
              | metodosPropiedadesMap
  '''

def p_asignacion(p):
    ''' asignacion : asignacionMate
                  | asignacionOtros
  '''


def p_asignacion_mate(p):
    ''' asignacionMate : VAR VARIABLE TIPODATOS ASIGNADOR expression
                     | VARIABLE DOSPUNTOS ASIGNADOR expression
                     | VAR VARIABLE ASIGNADOR expression
  '''

def p_asignacion_otros(p):
    ''' asignacionOtros : VAR VARIABLE TIPODATOS ASIGNADOR valoresOtros
                     | VARIABLE DOSPUNTOS ASIGNADOR valoresOtros
                     | VAR VARIABLE ASIGNADOR valoresOtros
  '''

def p_asignacion_corta(p):
  ' asigacionCorta : DOSPUNTOS ASIGNADOR'

def p_valores_otros(p):
    ''' valoresOtros : STRING
                    | BOOLEAN
  '''

######## Todo Funciones
def p_funcion_go(p):
  ''' funcion : FUNCTION VARIABLE LPAREN RPAREN LLAVEIZ golang LLAVEDE
              | FUNCTION VARIABLE LPAREN parametros RPAREN LLAVEIZ golang LLAVEDE
  '''

def p_parametros_func(p):
  ''' parametros : valoresPosibles
                  | VARIABLE TIPODATOS
                  | VARIABLE TIPODATOS COMA parametros
  '''
##################

##### Todo importar paquetes
def p_imports(p):
  ''' imports : package
              | import
  '''

def p_paquetes_go(p):
  ' package : PACKAGE VARIABLE'

def p_import_go(p):
  ''' import : IMPORT variosImports 
              | IMPORT LPAREN variosImports RPAREN 
  '''

def p_variosImports(p):
  ''' variosImports : STRING
                    | STRING variosImports
  '''
######## Todo Arrays
def p_array(p):
  ''' array : arrayNoInit
            | arrayInit
  '''

def p_array_noinit(p):
  ' arrayNoInit : VAR VARIABLE CORCHETEIZ NUMBER CORCHETEDER TIPODATOS'

def p_array_init(p): 
  ' arrayInit : VARIABLE asigacionCorta CORCHETEIZ NUMBER CORCHETEDER TIPODATOS LLAVEIZ arrayElementos LLAVEDE'

def p_array_elementos(p):
  ''' arrayElementos : valoresPosibles
                      | valoresPosibles COMA valoresPosibles 
  '''

####### METODOS ARRAY
def p_metodos_propiedades_array(p):
  ''' metodosPropiedadesArray : slice
                              | remove
                              | sliceAsignacion
   '''

def p_remove_array(p):
  ' remove : VARIABLE PUNTO REMOVE LPAREN NUMBER RPAREN'

def p_sliceasignacion_array(p):
  ' sliceAsignacion : slice ASIGNADOR valoresPosibles'

def p_slice_array(p):
  ' slice : VARIABLE CORCHETEIZ valoresPosibles CORCHETEDER'

def p_valores_posibles(p):
  ''' valoresPosibles : NUMBER
                      | BOOLEAN
                      | STRING
                      | FLOTANTE
                      | VARIABLE
  '''

######## Todo Maps
def p_map(p):
  ''' map : mapMake
            | mapnoMake
  '''

def p_map_Make(p):
  ' mapMake : VARIABLE asigacionCorta MAKE LPAREN MAP CORCHETEIZ TIPODATOS CORCHETEDER TIPODATOS RPAREN'

def p_map_noMake(p):
  ' mapnoMake : VARIABLE asigacionCorta MAP CORCHETEIZ TIPODATOS CORCHETEDER TIPODATOS LLAVEIZ mapElementos LLAVEDE'

def p_map_elementos(p):
  ''' mapElementos : valoresPosibles DOSPUNTOS valoresPosibles
                      | valoresPosibles DOSPUNTOS valoresPosibles COMA mapElementos
  '''

####### METODOS MAP
def p_metodos_propiedades_map(p):
  ''' metodosPropiedadesMap : mapAppend
                              | mapDelete
   '''

def p_append_map(p):
  ' mapAppend : CORCHETEIZ valoresPosibles CORCHETEDER ASIGNADOR valoresPosibles'

def p_delete_map(p):
  ' mapDelete : DELETE LPAREN VARIABLE COMA valoresPosibles RPAREN'

#Contribucion Ricardo Rivera: Slice ##############################

####### Todo Slice
def p_slice(p):
  ''' slice : sliceNoInit
            | sliceInit
  '''
def p_slice_noinit(p):
  ' sliceNoInit : VAR VARIABLE CORCHETEIZ NUMBER CORCHETEDER TIPODATOS'

def p_slice_init(p): 
  ' sliceInit : VARIABLE asigacionCorta CORCHETEIZ NUMBER CORCHETEDER TIPODATOS LLAVEIZ sliceElementos LLAVEDE'

def p_slice_elementos(p):
  ''' sliceElementos : valoresPosibles
                      | valoresPosibles COMA valoresPosibles '''

######## Meotodos slice

def p_metodos_propiedades_slice(p):
  ''' metodosPropiedadesSlice : slice
                              | remove
                              | sliceAsignacion
   '''

def p_remove_slice(p):
  ' remove : VARIABLE PUNTO REMOVE LPAREN NUMBER RPAREN'

def p_sliceasignacion_slice(p):
  ' sliceAsignacion : slice ASIGNADOR valoresPosibles'

def p_slice_slice(p):
  ' slice : VARIABLE CORCHETEIZ valoresPosibles CORCHETEDER'

def p_valores_posibles(p):
  ''' valoresPosibles : NUMBER
                      | BOOLEAN
                      | STRING
                      | FLOTANTE
                      | VARIABLE
  '''

#Fin de contribucion Ricardo Rivera: Slice ##############################

######## Todo condicionales
def p_condicional(p):
  ''' condicional : tiposCondicion condicion LLAVEIZ golang LLAVEDE 
                  | condicional ELSE LLAVEIZ golang LLAVEDE

  '''

def p_tipos_condicion(p):
  ''' tiposCondicion : IF
                      | ELSE IF
  '''

def p_condicion(p):
  ''' condicion : expression
                | LPAREN expression comparadores expression RPAREN
                | LPAREN expression comparadores expression RPAREN comparadores condicion
                | expression comparadores condicion
  '''

def p_comparadores(p):
  ''' comparadores : MAYORQUE
                  | MENORQUE
                  | MAYOROIGUALQUE
                  | MENOROIGUALQUE
                  | EQUIVALENTE
                  | DIFERENTE
  '''
########################

##### Todo FOR
def p_bucle_for(p):
  ' bucleFor : FOR asignacionFOR condicionFOR updateFOR LLAVEIZ golang LLAVEDE'

def p_asignacion_for(p):
  ' asignacionFOR : VARIABLE DOSPUNTOS ASIGNADOR expression PUNTOCOMA '

def p_condicion_for(p):
  ' condicionFOR : VARIABLE comparadores expression PUNTOCOMA '

def p_update_for(p):
  ' updateFOR : VARIABLE incrementoDecremento'

def p_incrementos_decrementos(p):
  ''' incrementoDecremento : INCREMENTO
                            | DECREMENTO
  '''
###################


## Todo condicionales
def p_condicional(p):
    ''' condicional : tiposCondicion condicion LLAVEIZ golang LLAVEDE
                  | condicional ELSE LLAVEIZ golang LLAVEDE

  '''


def p_tipos_condicion(p):
    ''' tiposCondicion : IF
                      | ELSE IF
  '''


def p_condicion(p):
    ''' condicion : expression
                | LPAREN expression comparadores expression RPAREN
                | LPAREN expression comparadores expression RPAREN comparadores condicion
                | expression comparadores condicion
  '''


def p_comparadores(p):
    ''' comparadores : MAYORQUE
                  | MENORQUE
                  | MAYOROIGUALQUE
                  | MENOROIGUALQUE
                  | EQUIVALENTE
                  | DIFERENTE
  '''


########################

#Contribucion Ricardo Rivera#
#Inicio###########################################
def p_bucle_for(p):
    ' bucleFor : FOR asignacionFOR condicionFOR updateFOR LLAVEIZ golang LLAVEDE'


def p_asignacion_for(p):
    ' asignacionFOR : VARIABLE DOSPUNTOS ASIGNADOR expression PUNTOCOMA '


def p_condicion_for(p):
    ' condicionFOR : VARIABLE comparadores expression PUNTOCOMA '


def p_update_for(p):
    ' updateFOR : VARIABLE incrementoDecremento'


def p_incrementos_decrementos(p):
    ''' incrementoDecremento : INCREMENTO
                            | DECREMENTO
  '''


#Fin###############################################

#Contribucion Ricardo Zevallos#
#Inicio###########################################

def p_print(p):
  '''
  print : PRINT LPAREN parametro RPAREN
          | PRINTLN LPAREN parametro RPAREN
          | PRINTF LPAREN parametro RPAREN
  '''

def p_parametro_print(p):
  ''' parametro : argumento
                  | argumento COMA parametro
  '''

def p_argumento(p):
    '''
  argumento : NUMBER
          | FLOTANTE
          | VARIABLE
          | STRING
  '''

##switch

def p_switch(p):
  'switch : SWITCH argumento LLAVEIZ casos LLAVEDE'

def p_casos(p):
  ''' casos : CASE argumento DOSPUNTOS golang
                      | CASE argumento DOSPUNTOS golang casos
  '''



#######################


def p_expression_plus(p):
    'expression : expression MAS term'


def p_expression_minus(p):
    'expression : expression RESTA term'


def p_expression_term(p):
    'expression : term'


def p_term_times(p):
    'term : term MULTI factor'


def p_term_div(p):
    'term : term DIVIDE factor'


def p_term_factor(p):
    'term : factor'


def p_factor_num(p):
    '''
  factor : NUMBER 
          | FLOTANTE 
          | VARIABLE
  '''


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'


#######################
# Funcion de error
def p_error(p):
    print("Error de sintaxis!")


parser = yacc.yacc()

while True:
    try:
        s = input('go > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)