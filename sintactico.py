import ply.yacc as yacc

from lexer import tokens

# William Venegas
def p_golang(p):
  ''' golang : asignacion 
              | expression
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