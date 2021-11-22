import ply.yacc as yacc

from lexer import tokens


# William Venegas
def p_golang(p):
    ''' golang : asignacion
              | expression
              | condicional
              | bucleFor
              | funcion
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
  ''' parametros : VARIABLE TIPODATOS
                  | VARIABLE TIPODATOS COMA parametros
  '''
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