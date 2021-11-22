import ply.lex as lex

# Ricardo Contribution -Reserved Keywords
reserved = {
    'break' : 'BREAK',
    'default': 'DEFAULT',
    'func': 'FUNCTION',
    'interface': 'INTERFACE',
    'select': 'SELECT',
    'if' : 'IF',
    'package': 'PACKAGE',
    'return': 'RETURN',
    'case': 'CASE',
    'defer': 'DEFER',
    'go': 'GO',
    'map': 'MAP',
    'struct': 'STRUCT',
    'chan': 'CHAN',
    'else': 'ELSE',
    'goto': 'GOTO',
    'const': 'CONST',
    'fallthrough': 'FALLTHROUGH',
    'range': 'RANGE',
    'type': 'TYPE',
    'continue': 'CONTINUE',
    'for': 'FOR',
    'import': 'IMPORT',
    'var': 'VAR',

}
##############################

 # List of token names.   This is always required
tokens = (
  # William Venegas
  'NUMBER',
  'MAS',
  'RESTA',
  'MULTI',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
  'FLOTANTE',
  'MODULO',
  'DIFERENTE',
  'LLAVEIZ',
  'LLAVEDE',
  'EQUIVALENTE',
  'VARIABLE',
  'BOOLEAN',
  'BACKTICK',
  'COMILLASDOBLES',
  'INCREMENTO',
  'DECREMENTO',
  'ID',
  # William Venegas

  # Ricardo Zevallos
  'ASIGNADOR',
  'ASIGNADORSUM',
  'ASIGNADORRESTA',
  'ASIGNADORMULT',
  'ASIGNADORDIV',
  'MAYORQUE',
  'MENORQUE',
  'MAYOROIGUALQUE',
  'MENOROIGUALQUE',
  'FLOTANTEI',
  'STRING',
  'DOSPUNTOS',
  'TIPODATOS'
 # Ricardo Zevallos
) + tuple(reserved.values())
 
# Regular expression rules for simple tokens
# William Venegas
t_MAS    = r'\+'
t_RESTA   = r'-'
t_MULTI   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NUMBER = r'\d+'
t_FLOTANTE = r'\d+\.\d+'
t_MODULO = r'%'
t_EQUIVALENTE = r'=='
t_DIFERENTE = r'!='
t_LLAVEIZ = r'\{'
t_LLAVEDE = r'\}'
t_COMILLASDOBLES = r'\"'
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'\-\-'
t_DOSPUNTOS = r':'
# William Venegas
#t_VARIABLE = r'[a-z]+'

# Ricardo Zevallos
t_BOOLEAN = r'true|false'
t_STRING = r'".*"'
t_FLOTANTEI = r'(\d+\.\d+i)|(\d+i)'
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYOROIGUALQUE = r'>='
t_MENOROIGUALQUE = r'<='
t_ASIGNADOR = r'='
t_ASIGNADORSUM = r'\+='
t_ASIGNADORRESTA = r'-='
t_ASIGNADORMULT = r'\*='
t_ASIGNADORDIV = r'/='
# Ricardo Zevallos1
 
# William Venegas
def t_TIPODATOS(t):
    r'int | string | float64 | bool'
    return t

def t_BOOL(t):
  r'(true|false)'
  t.type = reserved.get(t.value, 'BOOLEAN')
  return t
# William Venegas
def t_BACKTICK(t):
  r'`'
  t.type = reserved.get(t.value, 'BACKTICK')
  return t

def t_VARIABLE(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

t_ignore  = ' \t'
 
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)
 
def menu():
  print("-"*8+"MENU"+"-"*8)
  print("1. Test auto\n2. Test Manual\n3. Cancelar")

lexer = lex.lex()

def test(opcion):
  if opcion == 1:
  # Data de prueba
    data = '''package main 
    func main() {
      if 2==4 {
        5+2
        4.567 * 2
        4.567 <= 3
        `hola`
        "test"
        count++
        i--
        return true 
      }else{
        return false
      }
    }
    '''

  if opcion == 2:
    data = input("Ingrese su test: ")  
  
  if opcion == 3:
    print("Cancelando...")
    return
  # Pasando la data como entrada en el lexer
  lexer.input(data)

  # Probando la data
  while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)

if __name__ == '__main__':
  # Principal
  opcion = 0
  while opcion != 3:
    menu()  
    opcion = int(input("Ingrese una opción: "))
    test(opcion)

    