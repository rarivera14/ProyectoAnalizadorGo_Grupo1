import ply.lex as lex
 
reserved = {
    'if' : 'IF',
    'package': 'PACKAGE',
    'default': 'DEFAULT',
    'func': 'FUNCTION',
    'return': 'RETURN'
}

 # List of token names.   This is always required
tokens = (
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
  'ID'
) + tuple(reserved.values())
 
 # Regular expression rules for simple tokens
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
#t_VARIABLE = r'[a-z]+'
 
 # Define a rule so we can track line numbers
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_VARIABLE(t):
  r'[a-zA-Z]+'
  t.type = reserved.get(t.value,'VARIABLE')
  return t

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  t.type = reserved.get(t.value,'ID')
  return t

t_ignore  = ' \t'
 
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)
 
if __name__ == '__main__':
  lexer = lex.lex()

  # Test it out
  data = '''package main 
    if 2==4 {
      return true
    } 
    '''
  
  # Give the lexer some input
  lexer.input(data)
  
  # Tokenize
  while True:
    tok = lexer.token()
    if not tok: 
      break    
    print(tok)
