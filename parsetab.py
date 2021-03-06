
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNADOR ASIGNADORDIV ASIGNADORMULT ASIGNADORRESTA ASIGNADORSUM BACKTICK BOOLEAN BREAK CASE CHAN COMA COMILLASDOBLES CONST CONTINUE CORCHETEDER CORCHETEIZ DECREMENTO DEFAULT DEFER DELETE DIFERENTE DIVIDE DOSPUNTOS ELSE EQUIVALENTE FALLTHROUGH FLOTANTE FLOTANTEI FOR FUNCTION GO GOTO ID IF IMPORT INCREMENTO INTERFACE LLAVEDE LLAVEIZ LPAREN MAKE MAP MAS MAYOROIGUALQUE MAYORQUE MENOROIGUALQUE MENORQUE MODULO MULTI NUMBER PACKAGE PRINT PRINTF PRINTLN PUNTO PUNTOCOMA RANGE REMOVE RESTA RETURN RPAREN SELECT STRING STRUCT SWITCH TIPODATOS TYPE VAR VARIABLE golang : asignacion\n              | expression\n              | condicional\n              | bucleFor\n              | funcion\n              | imports\n              | array\n              | metodosPropiedadesArray\n              | print\n              | switch\n              | map\n              | metodosPropiedadesMap \n              | mat_semantica_menos \n              | mat_semantica_multi\n   asignacion : asignacionMate\n                  | asignacionOtros\n\n   asignacionMate : VAR VARIABLE TIPODATOS ASIGNADOR expression\n                     | VARIABLE DOSPUNTOS ASIGNADOR expression\n                     | VAR VARIABLE ASIGNADOR expression\n   asignacionOtros : VAR VARIABLE TIPODATOS ASIGNADOR valoresOtros\n                     | VARIABLE DOSPUNTOS ASIGNADOR valoresOtros\n                     | VAR VARIABLE ASIGNADOR valoresOtros\n                     | asignacionSuma\n                     | asignacionResta\n                     | asignacionMult\n                     | asignacionDiv\n\n   asignacionSuma : VARIABLE ASIGNADORSUM expression asignacionResta : VARIABLE ASIGNADORRESTA expression asignacionMult : VARIABLE ASIGNADORMULT expression asignacionDiv : VARIABLE ASIGNADORDIV expression asigacionCorta : DOSPUNTOS ASIGNADOR valoresOtros : STRING\n                    | BOOLEAN\n   funcion : FUNCTION VARIABLE LPAREN RPAREN LLAVEIZ golang LLAVEDE\n              | FUNCTION VARIABLE LPAREN parametros RPAREN LLAVEIZ golang LLAVEDE\n   parametros : valoresPosibles\n                  | VARIABLE TIPODATOS\n                  | VARIABLE TIPODATOS COMA parametros\n   imports : package\n              | import\n   package : PACKAGE VARIABLE import : IMPORT variosImports \n              | IMPORT LPAREN variosImports RPAREN \n   variosImports : STRING\n                    | STRING variosImports\n   array : arrayNoInit\n            | arrayInit\n   arrayNoInit : VAR VARIABLE CORCHETEIZ NUMBER CORCHETEDER TIPODATOS arrayInit : VARIABLE asigacionCorta CORCHETEIZ NUMBER CORCHETEDER TIPODATOS LLAVEIZ arrayElementos LLAVEDE arrayElementos : valoresPosibles\n                      | valoresPosibles COMA valoresPosibles \n   metodosPropiedadesArray : slice\n                              | remove\n                              | sliceAsignacion\n    remove : VARIABLE PUNTO REMOVE LPAREN NUMBER RPAREN sliceAsignacion : slice ASIGNADOR valoresPosibles slice : VARIABLE CORCHETEIZ valoresPosibles CORCHETEDER map : mapMake\n            | mapnoMake\n   mapMake : VARIABLE asigacionCorta MAKE LPAREN MAP CORCHETEIZ TIPODATOS CORCHETEDER TIPODATOS RPAREN mapnoMake : VARIABLE asigacionCorta MAP CORCHETEIZ TIPODATOS CORCHETEDER TIPODATOS LLAVEIZ mapElementos LLAVEDE mapElementos : valoresPosibles DOSPUNTOS valoresPosibles\n                      | valoresPosibles DOSPUNTOS valoresPosibles COMA mapElementos\n   metodosPropiedadesMap : mapAppend\n                              | mapDelete\n    mapAppend : CORCHETEIZ valoresPosibles CORCHETEDER ASIGNADOR valoresPosibles mapDelete : DELETE LPAREN VARIABLE COMA valoresPosibles RPAREN slice : sliceNoInit\n            | sliceInit\n   sliceNoInit : VAR VARIABLE CORCHETEIZ NUMBER CORCHETEDER TIPODATOS sliceInit : VARIABLE asigacionCorta CORCHETEIZ NUMBER CORCHETEDER TIPODATOS LLAVEIZ sliceElementos LLAVEDE sliceElementos : valoresPosibles\n                      | valoresPosibles COMA valoresPosibles  metodosPropiedadesSlice : slice\n                              | remove\n                              | sliceAsignacion\n    valoresPosibles : NUMBER\n                      | BOOLEAN\n                      | STRING\n                      | FLOTANTE\n                      | VARIABLE\n   condicional : tiposCondicion condicion LLAVEIZ golang LLAVEDE\n                  | condicional ELSE LLAVEIZ golang LLAVEDE\n\n   tiposCondicion : IF\n                      | ELSE IF\n   condicion : expression\n                | LPAREN expression comparadores expression RPAREN\n                | LPAREN expression comparadores expression RPAREN comparadores condicion\n                | expression comparadores condicion\n   comparadores : MAYORQUE\n                  | MENORQUE\n                  | MAYOROIGUALQUE\n                  | MENOROIGUALQUE\n                  | EQUIVALENTE\n                  | DIFERENTE\n   bucleFor : FOR asignacionFOR condicionFOR updateFOR LLAVEIZ golang LLAVEDE asignacionFOR : VARIABLE DOSPUNTOS ASIGNADOR expression PUNTOCOMA  condicionFOR : VARIABLE comparadores expression PUNTOCOMA  updateFOR : VARIABLE incrementoDecremento incrementoDecremento : INCREMENTO\n                            | DECREMENTO\n  \n  print : PRINT LPAREN parametro RPAREN\n          | PRINTLN LPAREN parametro RPAREN\n          | PRINTF LPAREN parametro RPAREN\n   parametro : argumento\n                  | argumento COMA parametro\n  \n  argumento : NUMBER\n          | FLOTANTE\n          | VARIABLE\n          | STRING\n  switch : SWITCH argumento LLAVEIZ casos LLAVEDE casos : CASE argumento DOSPUNTOS golang\n                      | CASE argumento DOSPUNTOS golang casos\n  mat_semantica_plus : NUMBER MAS NUMBERmat_semantica_menos : NUMBER MAS NUMBERmat_semantica_multi : NUMBER MAS NUMBERexpression : expression MAS termexpression : expression RESTA termexpression : termterm : term MULTI factorterm : term DIVIDE factorterm : factor\n  factor : NUMBER \n          | FLOTANTE \n          | VARIABLE\n  factor : LPAREN expression RPAREN'
    
_lr_action_items = {'FOR':([0,102,105,180,187,207,212,],[21,21,21,21,21,21,21,]),'FUNCTION':([0,102,105,180,187,207,212,],[22,22,22,22,22,22,22,]),'PRINT':([0,102,105,180,187,207,212,],[32,32,32,32,32,32,32,]),'PRINTLN':([0,102,105,180,187,207,212,],[33,33,33,33,33,33,33,]),'PRINTF':([0,102,105,180,187,207,212,],[34,34,34,34,34,34,34,]),'SWITCH':([0,102,105,180,187,207,212,],[35,35,35,35,35,35,35,]),'NUMBER':([0,19,24,35,47,50,55,56,58,59,62,65,71,73,74,75,76,78,79,80,81,87,102,105,106,107,108,109,110,111,112,117,118,119,137,138,146,149,150,163,165,169,170,175,176,180,187,205,207,212,215,220,230,234,241,243,],[40,63,63,83,-84,94,63,63,63,63,63,-85,94,63,63,63,63,94,83,83,83,135,40,40,63,-90,-91,-92,-93,-94,-95,94,63,159,63,173,63,63,63,192,83,83,63,94,94,40,40,94,40,40,63,94,94,94,94,94,]),'VAR':([0,102,105,180,187,207,212,],[41,41,41,41,41,41,41,]),'VARIABLE':([0,19,21,22,24,35,41,47,48,50,55,56,58,59,62,65,66,71,73,74,75,76,78,79,80,81,99,102,105,106,107,108,109,110,111,112,114,117,118,137,146,149,150,165,169,170,175,176,180,187,203,204,205,207,212,215,220,230,234,241,243,],[23,64,67,68,64,85,88,-84,89,98,64,64,64,64,64,-85,115,98,64,64,64,64,98,85,85,85,142,23,23,64,-90,-91,-92,-93,-94,-95,148,151,64,64,64,64,64,85,85,64,98,98,23,23,-98,-97,151,23,23,64,98,98,98,98,98,]),'IF':([0,20,102,105,180,187,207,212,],[47,65,47,47,47,47,47,47,]),'ELSE':([0,4,102,105,177,178,180,187,207,212,],[20,57,20,20,-83,-82,20,20,20,20,]),'PACKAGE':([0,102,105,180,187,207,212,],[48,48,48,48,48,48,48,]),'IMPORT':([0,102,105,180,187,207,212,],[49,49,49,49,49,49,49,]),'CORCHETEIZ':([0,23,70,88,102,105,118,121,180,187,190,207,212,],[50,71,119,138,50,50,-31,161,50,50,209,50,50,]),'DELETE':([0,102,105,180,187,207,212,],[53,53,53,53,53,53,53,]),'FLOTANTE':([0,19,24,35,47,50,55,56,58,59,62,65,71,73,74,75,76,78,79,80,81,102,105,106,107,108,109,110,111,112,117,118,137,146,149,150,165,169,170,175,176,180,187,205,207,212,215,220,230,234,241,243,],[54,54,54,84,-84,97,54,54,54,54,54,-85,97,54,54,54,54,97,84,84,84,54,54,54,-90,-91,-92,-93,-94,-95,97,54,54,54,54,54,84,84,54,97,97,54,54,97,54,54,54,97,97,97,97,97,]),'LPAREN':([0,19,24,32,33,34,47,49,53,55,56,58,59,62,65,68,73,74,75,76,102,105,106,107,108,109,110,111,112,118,120,123,137,146,149,150,170,180,187,207,212,215,],[24,62,24,79,80,81,-84,91,99,24,24,24,24,24,-85,117,24,24,24,24,24,24,62,-90,-91,-92,-93,-94,-95,24,160,163,24,24,24,24,24,24,24,24,24,62,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,23,25,26,27,28,29,30,31,36,37,38,39,40,42,43,44,45,46,51,52,54,63,64,89,90,92,94,95,96,97,98,100,101,103,104,124,125,126,127,128,129,135,140,155,156,157,158,162,164,166,167,171,172,174,177,178,194,196,197,199,211,213,214,216,218,225,232,233,239,240,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-119,-125,-39,-40,-46,-47,-52,-53,-54,-58,-59,-64,-65,-123,-23,-24,-25,-26,-122,-68,-69,-124,-123,-125,-41,-42,-44,-77,-78,-79,-80,-81,-117,-118,-120,-121,-27,-28,-29,-30,-126,-56,-115,-45,-18,-21,-32,-33,-57,-102,-103,-104,-19,-22,-43,-83,-82,-111,-17,-20,-66,-55,-48,-67,-96,-34,-35,-49,-71,-60,-61,]),'LLAVEDE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,23,25,26,27,28,29,30,31,36,37,38,39,40,42,43,44,45,46,51,52,54,63,64,89,90,92,94,95,96,97,98,100,101,103,104,124,125,126,127,128,129,135,140,143,144,155,156,157,158,162,164,166,167,168,171,172,174,177,178,194,196,197,199,202,206,211,213,214,216,218,219,223,225,226,227,228,231,232,233,236,238,239,240,242,244,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-119,-125,-39,-40,-46,-47,-52,-53,-54,-58,-59,-64,-65,-123,-23,-24,-25,-26,-122,-68,-69,-124,-123,-125,-41,-42,-44,-77,-78,-79,-80,-81,-117,-118,-120,-121,-27,-28,-29,-30,-126,-56,-115,-45,177,178,-18,-21,-32,-33,-57,-102,-103,-104,194,-19,-22,-43,-83,-82,-111,-17,-20,-66,216,218,-55,-48,-67,-96,-34,225,-112,-35,232,233,-50,-113,-49,-71,240,-51,-60,-61,-62,-63,]),'CASE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,23,25,26,27,28,29,30,31,36,37,38,39,40,42,43,44,45,46,51,52,54,63,64,89,90,92,94,95,96,97,98,100,101,103,104,124,125,126,127,128,129,134,135,140,155,156,157,158,162,164,166,167,171,172,174,177,178,194,196,197,199,211,213,214,216,218,223,225,232,233,239,240,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-119,-125,-39,-40,-46,-47,-52,-53,-54,-58,-59,-64,-65,-123,-23,-24,-25,-26,-122,-68,-69,-124,-123,-125,-41,-42,-44,-77,-78,-79,-80,-81,-117,-118,-120,-121,-27,-28,-29,-30,-126,-56,169,-115,-45,-18,-21,-32,-33,-57,-102,-103,-104,-19,-22,-43,-83,-82,-111,-17,-20,-66,-55,-48,-67,-96,-34,169,-35,-49,-71,-60,-61,]),'MAS':([3,18,23,40,46,54,61,63,64,77,100,101,103,104,113,124,125,126,127,128,155,171,179,184,185,196,],[55,-119,-125,87,-122,-124,55,-123,-125,55,-117,-118,-120,-121,55,55,55,55,55,-126,55,55,55,55,55,55,]),'RESTA':([3,18,23,40,46,54,61,63,64,77,100,101,103,104,113,124,125,126,127,128,155,171,179,184,185,196,],[56,-119,-125,-123,-122,-124,56,-123,-125,56,-117,-118,-120,-121,56,56,56,56,56,-126,56,56,56,56,56,56,]),'MAYORQUE':([18,46,54,61,63,64,100,101,103,104,113,115,128,201,],[-119,-122,-124,107,-123,-125,-117,-118,-120,-121,107,107,-126,107,]),'MENORQUE':([18,46,54,61,63,64,100,101,103,104,113,115,128,201,],[-119,-122,-124,108,-123,-125,-117,-118,-120,-121,108,108,-126,108,]),'MAYOROIGUALQUE':([18,46,54,61,63,64,100,101,103,104,113,115,128,201,],[-119,-122,-124,109,-123,-125,-117,-118,-120,-121,109,109,-126,109,]),'MENOROIGUALQUE':([18,46,54,61,63,64,100,101,103,104,113,115,128,201,],[-119,-122,-124,110,-123,-125,-117,-118,-120,-121,110,110,-126,110,]),'EQUIVALENTE':([18,46,54,61,63,64,100,101,103,104,113,115,128,201,],[-119,-122,-124,111,-123,-125,-117,-118,-120,-121,111,111,-126,111,]),'DIFERENTE':([18,46,54,61,63,64,100,101,103,104,113,115,128,201,],[-119,-122,-124,112,-123,-125,-117,-118,-120,-121,112,112,-126,112,]),'LLAVEIZ':([18,46,54,57,60,61,63,64,82,83,84,85,86,100,101,103,104,128,145,147,152,181,182,183,188,201,208,222,224,],[-119,-122,-124,102,105,-86,-123,-125,134,-107,-108,-109,-110,-117,-118,-120,-121,-126,-89,180,187,-99,-100,-101,207,-87,220,230,-88,]),'RPAREN':([18,46,54,63,64,77,83,84,85,86,92,94,95,96,97,98,100,101,103,104,113,117,128,130,131,132,133,139,140,151,153,154,179,186,192,193,200,217,235,],[-119,-122,-124,-123,-125,128,-107,-108,-109,-110,-44,-77,-78,-79,-80,-81,-117,-118,-120,-121,128,152,-126,164,-105,166,167,174,-45,-81,188,-36,201,-37,211,-106,214,-38,239,]),'PUNTOCOMA':([18,46,54,63,64,100,101,103,104,128,184,185,],[-119,-122,-124,-123,-125,-117,-118,-120,-121,-126,203,204,]),'MULTI':([18,23,40,46,54,63,64,100,101,103,104,128,],[58,-125,-123,-122,-124,-123,-125,58,58,-120,-121,-126,]),'DIVIDE':([18,23,40,46,54,63,64,100,101,103,104,128,],[59,-125,-123,-122,-124,-123,-125,59,59,-120,-121,-126,]),'DOSPUNTOS':([23,67,83,84,85,86,94,95,96,97,98,195,237,],[69,116,-107,-108,-109,-110,-77,-78,-79,-80,-81,212,241,]),'PUNTO':([23,],[72,]),'ASIGNADORSUM':([23,],[73,]),'ASIGNADORRESTA':([23,],[74,]),'ASIGNADORMULT':([23,],[75,]),'ASIGNADORDIV':([23,],[76,]),'ASIGNADOR':([29,51,52,69,88,116,136,141,162,213,233,],[78,-68,-69,118,137,150,170,175,-57,-70,-71,]),'STRING':([35,49,50,71,78,79,80,81,91,92,117,118,137,165,169,170,175,176,205,220,230,234,241,243,],[86,92,96,96,96,86,86,86,92,92,96,157,157,86,86,157,96,96,96,96,96,96,96,96,]),'BOOLEAN':([50,71,78,117,118,137,170,175,176,205,220,230,234,241,243,],[95,95,95,95,158,158,158,95,95,95,95,95,95,95,95,]),'MAKE':([70,118,],[120,-31,]),'MAP':([70,118,160,],[121,-31,190,]),'REMOVE':([72,],[123,]),'COMA':([83,84,85,86,94,95,96,97,98,131,142,186,228,242,],[-107,-108,-109,-110,-77,-78,-79,-80,-81,165,176,205,234,243,]),'TIPODATOS':([88,151,161,189,198,209,210,229,],[136,186,191,208,213,221,222,235,]),'CORCHETEDER':([93,94,95,96,97,98,122,159,173,191,221,],[141,-77,-78,-79,-80,-81,162,189,198,210,229,]),'INCREMENTO':([148,],[182,]),'DECREMENTO':([148,],[183,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'golang':([0,102,105,180,187,207,212,],[1,143,144,202,206,219,223,]),'asignacion':([0,102,105,180,187,207,212,],[2,2,2,2,2,2,2,]),'expression':([0,19,24,62,73,74,75,76,102,105,106,118,137,146,149,150,170,180,187,207,212,215,],[3,61,77,113,124,125,126,127,3,3,61,155,171,179,184,185,196,3,3,3,3,61,]),'condicional':([0,102,105,180,187,207,212,],[4,4,4,4,4,4,4,]),'bucleFor':([0,102,105,180,187,207,212,],[5,5,5,5,5,5,5,]),'funcion':([0,102,105,180,187,207,212,],[6,6,6,6,6,6,6,]),'imports':([0,102,105,180,187,207,212,],[7,7,7,7,7,7,7,]),'array':([0,102,105,180,187,207,212,],[8,8,8,8,8,8,8,]),'metodosPropiedadesArray':([0,102,105,180,187,207,212,],[9,9,9,9,9,9,9,]),'print':([0,102,105,180,187,207,212,],[10,10,10,10,10,10,10,]),'switch':([0,102,105,180,187,207,212,],[11,11,11,11,11,11,11,]),'map':([0,102,105,180,187,207,212,],[12,12,12,12,12,12,12,]),'metodosPropiedadesMap':([0,102,105,180,187,207,212,],[13,13,13,13,13,13,13,]),'mat_semantica_menos':([0,102,105,180,187,207,212,],[14,14,14,14,14,14,14,]),'mat_semantica_multi':([0,102,105,180,187,207,212,],[15,15,15,15,15,15,15,]),'asignacionMate':([0,102,105,180,187,207,212,],[16,16,16,16,16,16,16,]),'asignacionOtros':([0,102,105,180,187,207,212,],[17,17,17,17,17,17,17,]),'term':([0,19,24,55,56,62,73,74,75,76,102,105,106,118,137,146,149,150,170,180,187,207,212,215,],[18,18,18,100,101,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'tiposCondicion':([0,102,105,180,187,207,212,],[19,19,19,19,19,19,19,]),'package':([0,102,105,180,187,207,212,],[25,25,25,25,25,25,25,]),'import':([0,102,105,180,187,207,212,],[26,26,26,26,26,26,26,]),'arrayNoInit':([0,102,105,180,187,207,212,],[27,27,27,27,27,27,27,]),'arrayInit':([0,102,105,180,187,207,212,],[28,28,28,28,28,28,28,]),'slice':([0,102,105,180,187,207,212,],[29,29,29,29,29,29,29,]),'remove':([0,102,105,180,187,207,212,],[30,30,30,30,30,30,30,]),'sliceAsignacion':([0,102,105,180,187,207,212,],[31,31,31,31,31,31,31,]),'mapMake':([0,102,105,180,187,207,212,],[36,36,36,36,36,36,36,]),'mapnoMake':([0,102,105,180,187,207,212,],[37,37,37,37,37,37,37,]),'mapAppend':([0,102,105,180,187,207,212,],[38,38,38,38,38,38,38,]),'mapDelete':([0,102,105,180,187,207,212,],[39,39,39,39,39,39,39,]),'asignacionSuma':([0,102,105,180,187,207,212,],[42,42,42,42,42,42,42,]),'asignacionResta':([0,102,105,180,187,207,212,],[43,43,43,43,43,43,43,]),'asignacionMult':([0,102,105,180,187,207,212,],[44,44,44,44,44,44,44,]),'asignacionDiv':([0,102,105,180,187,207,212,],[45,45,45,45,45,45,45,]),'factor':([0,19,24,55,56,58,59,62,73,74,75,76,102,105,106,118,137,146,149,150,170,180,187,207,212,215,],[46,46,46,46,46,103,104,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'sliceNoInit':([0,102,105,180,187,207,212,],[51,51,51,51,51,51,51,]),'sliceInit':([0,102,105,180,187,207,212,],[52,52,52,52,52,52,52,]),'condicion':([19,106,215,],[60,145,224,]),'asignacionFOR':([21,],[66,]),'asigacionCorta':([23,],[70,]),'argumento':([35,79,80,81,165,169,],[82,131,131,131,131,195,]),'variosImports':([49,91,92,],[90,139,140,]),'valoresPosibles':([50,71,78,117,175,176,205,220,230,234,241,243,],[93,122,129,154,199,200,154,228,237,238,242,237,]),'comparadores':([61,113,115,201,],[106,146,149,215,]),'condicionFOR':([66,],[114,]),'parametro':([79,80,81,165,],[130,132,133,193,]),'updateFOR':([114,],[147,]),'parametros':([117,205,],[153,217,]),'valoresOtros':([118,137,170,],[156,172,197,]),'casos':([134,223,],[168,231,]),'incrementoDecremento':([148,],[181,]),'arrayElementos':([220,],[226,]),'sliceElementos':([220,],[227,]),'mapElementos':([230,243,],[236,244,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> golang","S'",1,None,None,None),
  ('golang -> asignacion','golang',1,'p_golang','sintactico.py',8),
  ('golang -> expression','golang',1,'p_golang','sintactico.py',9),
  ('golang -> condicional','golang',1,'p_golang','sintactico.py',10),
  ('golang -> bucleFor','golang',1,'p_golang','sintactico.py',11),
  ('golang -> funcion','golang',1,'p_golang','sintactico.py',12),
  ('golang -> imports','golang',1,'p_golang','sintactico.py',13),
  ('golang -> array','golang',1,'p_golang','sintactico.py',14),
  ('golang -> metodosPropiedadesArray','golang',1,'p_golang','sintactico.py',15),
  ('golang -> print','golang',1,'p_golang','sintactico.py',16),
  ('golang -> switch','golang',1,'p_golang','sintactico.py',17),
  ('golang -> map','golang',1,'p_golang','sintactico.py',18),
  ('golang -> metodosPropiedadesMap','golang',1,'p_golang','sintactico.py',19),
  ('golang -> mat_semantica_menos','golang',1,'p_golang','sintactico.py',20),
  ('golang -> mat_semantica_multi','golang',1,'p_golang','sintactico.py',21),
  ('asignacion -> asignacionMate','asignacion',1,'p_asignacion','sintactico.py',25),
  ('asignacion -> asignacionOtros','asignacion',1,'p_asignacion','sintactico.py',26),
  ('asignacionMate -> VAR VARIABLE TIPODATOS ASIGNADOR expression','asignacionMate',5,'p_asignacion_mate','sintactico.py',32),
  ('asignacionMate -> VARIABLE DOSPUNTOS ASIGNADOR expression','asignacionMate',4,'p_asignacion_mate','sintactico.py',33),
  ('asignacionMate -> VAR VARIABLE ASIGNADOR expression','asignacionMate',4,'p_asignacion_mate','sintactico.py',34),
  ('asignacionOtros -> VAR VARIABLE TIPODATOS ASIGNADOR valoresOtros','asignacionOtros',5,'p_asignacion_otros','sintactico.py',38),
  ('asignacionOtros -> VARIABLE DOSPUNTOS ASIGNADOR valoresOtros','asignacionOtros',4,'p_asignacion_otros','sintactico.py',39),
  ('asignacionOtros -> VAR VARIABLE ASIGNADOR valoresOtros','asignacionOtros',4,'p_asignacion_otros','sintactico.py',40),
  ('asignacionOtros -> asignacionSuma','asignacionOtros',1,'p_asignacion_otros','sintactico.py',41),
  ('asignacionOtros -> asignacionResta','asignacionOtros',1,'p_asignacion_otros','sintactico.py',42),
  ('asignacionOtros -> asignacionMult','asignacionOtros',1,'p_asignacion_otros','sintactico.py',43),
  ('asignacionOtros -> asignacionDiv','asignacionOtros',1,'p_asignacion_otros','sintactico.py',44),
  ('asignacionSuma -> VARIABLE ASIGNADORSUM expression','asignacionSuma',3,'p_asignacion_suma','sintactico.py',50),
  ('asignacionResta -> VARIABLE ASIGNADORRESTA expression','asignacionResta',3,'p_asignacion_resta','sintactico.py',53),
  ('asignacionMult -> VARIABLE ASIGNADORMULT expression','asignacionMult',3,'p_asignacion_mult','sintactico.py',56),
  ('asignacionDiv -> VARIABLE ASIGNADORDIV expression','asignacionDiv',3,'p_asignacion_div','sintactico.py',59),
  ('asigacionCorta -> DOSPUNTOS ASIGNADOR','asigacionCorta',2,'p_asignacion_corta','sintactico.py',62),
  ('valoresOtros -> STRING','valoresOtros',1,'p_valores_otros','sintactico.py',65),
  ('valoresOtros -> BOOLEAN','valoresOtros',1,'p_valores_otros','sintactico.py',66),
  ('funcion -> FUNCTION VARIABLE LPAREN RPAREN LLAVEIZ golang LLAVEDE','funcion',7,'p_funcion_go','sintactico.py',71),
  ('funcion -> FUNCTION VARIABLE LPAREN parametros RPAREN LLAVEIZ golang LLAVEDE','funcion',8,'p_funcion_go','sintactico.py',72),
  ('parametros -> valoresPosibles','parametros',1,'p_parametros_func','sintactico.py',76),
  ('parametros -> VARIABLE TIPODATOS','parametros',2,'p_parametros_func','sintactico.py',77),
  ('parametros -> VARIABLE TIPODATOS COMA parametros','parametros',4,'p_parametros_func','sintactico.py',78),
  ('imports -> package','imports',1,'p_imports','sintactico.py',84),
  ('imports -> import','imports',1,'p_imports','sintactico.py',85),
  ('package -> PACKAGE VARIABLE','package',2,'p_paquetes_go','sintactico.py',89),
  ('import -> IMPORT variosImports','import',2,'p_import_go','sintactico.py',92),
  ('import -> IMPORT LPAREN variosImports RPAREN','import',4,'p_import_go','sintactico.py',93),
  ('variosImports -> STRING','variosImports',1,'p_variosImports','sintactico.py',97),
  ('variosImports -> STRING variosImports','variosImports',2,'p_variosImports','sintactico.py',98),
  ('array -> arrayNoInit','array',1,'p_array','sintactico.py',102),
  ('array -> arrayInit','array',1,'p_array','sintactico.py',103),
  ('arrayNoInit -> VAR VARIABLE CORCHETEIZ NUMBER CORCHETEDER TIPODATOS','arrayNoInit',6,'p_array_noinit','sintactico.py',107),
  ('arrayInit -> VARIABLE asigacionCorta CORCHETEIZ NUMBER CORCHETEDER TIPODATOS LLAVEIZ arrayElementos LLAVEDE','arrayInit',9,'p_array_init','sintactico.py',110),
  ('arrayElementos -> valoresPosibles','arrayElementos',1,'p_array_elementos','sintactico.py',113),
  ('arrayElementos -> valoresPosibles COMA valoresPosibles','arrayElementos',3,'p_array_elementos','sintactico.py',114),
  ('metodosPropiedadesArray -> slice','metodosPropiedadesArray',1,'p_metodos_propiedades_array','sintactico.py',119),
  ('metodosPropiedadesArray -> remove','metodosPropiedadesArray',1,'p_metodos_propiedades_array','sintactico.py',120),
  ('metodosPropiedadesArray -> sliceAsignacion','metodosPropiedadesArray',1,'p_metodos_propiedades_array','sintactico.py',121),
  ('remove -> VARIABLE PUNTO REMOVE LPAREN NUMBER RPAREN','remove',6,'p_remove_array','sintactico.py',125),
  ('sliceAsignacion -> slice ASIGNADOR valoresPosibles','sliceAsignacion',3,'p_sliceasignacion_array','sintactico.py',128),
  ('slice -> VARIABLE CORCHETEIZ valoresPosibles CORCHETEDER','slice',4,'p_slice_array','sintactico.py',131),
  ('map -> mapMake','map',1,'p_map','sintactico.py',143),
  ('map -> mapnoMake','map',1,'p_map','sintactico.py',144),
  ('mapMake -> VARIABLE asigacionCorta MAKE LPAREN MAP CORCHETEIZ TIPODATOS CORCHETEDER TIPODATOS RPAREN','mapMake',10,'p_map_Make','sintactico.py',148),
  ('mapnoMake -> VARIABLE asigacionCorta MAP CORCHETEIZ TIPODATOS CORCHETEDER TIPODATOS LLAVEIZ mapElementos LLAVEDE','mapnoMake',10,'p_map_noMake','sintactico.py',151),
  ('mapElementos -> valoresPosibles DOSPUNTOS valoresPosibles','mapElementos',3,'p_map_elementos','sintactico.py',154),
  ('mapElementos -> valoresPosibles DOSPUNTOS valoresPosibles COMA mapElementos','mapElementos',5,'p_map_elementos','sintactico.py',155),
  ('metodosPropiedadesMap -> mapAppend','metodosPropiedadesMap',1,'p_metodos_propiedades_map','sintactico.py',160),
  ('metodosPropiedadesMap -> mapDelete','metodosPropiedadesMap',1,'p_metodos_propiedades_map','sintactico.py',161),
  ('mapAppend -> CORCHETEIZ valoresPosibles CORCHETEDER ASIGNADOR valoresPosibles','mapAppend',5,'p_append_map','sintactico.py',165),
  ('mapDelete -> DELETE LPAREN VARIABLE COMA valoresPosibles RPAREN','mapDelete',6,'p_delete_map','sintactico.py',168),
  ('slice -> sliceNoInit','slice',1,'p_slice','sintactico.py',174),
  ('slice -> sliceInit','slice',1,'p_slice','sintactico.py',175),
  ('sliceNoInit -> VAR VARIABLE CORCHETEIZ NUMBER CORCHETEDER TIPODATOS','sliceNoInit',6,'p_slice_noinit','sintactico.py',178),
  ('sliceInit -> VARIABLE asigacionCorta CORCHETEIZ NUMBER CORCHETEDER TIPODATOS LLAVEIZ sliceElementos LLAVEDE','sliceInit',9,'p_slice_init','sintactico.py',181),
  ('sliceElementos -> valoresPosibles','sliceElementos',1,'p_slice_elementos','sintactico.py',184),
  ('sliceElementos -> valoresPosibles COMA valoresPosibles','sliceElementos',3,'p_slice_elementos','sintactico.py',185),
  ('metodosPropiedadesSlice -> slice','metodosPropiedadesSlice',1,'p_metodos_propiedades_slice','sintactico.py',190),
  ('metodosPropiedadesSlice -> remove','metodosPropiedadesSlice',1,'p_metodos_propiedades_slice','sintactico.py',191),
  ('metodosPropiedadesSlice -> sliceAsignacion','metodosPropiedadesSlice',1,'p_metodos_propiedades_slice','sintactico.py',192),
  ('valoresPosibles -> NUMBER','valoresPosibles',1,'p_valores_posibles','sintactico.py',196),
  ('valoresPosibles -> BOOLEAN','valoresPosibles',1,'p_valores_posibles','sintactico.py',197),
  ('valoresPosibles -> STRING','valoresPosibles',1,'p_valores_posibles','sintactico.py',198),
  ('valoresPosibles -> FLOTANTE','valoresPosibles',1,'p_valores_posibles','sintactico.py',199),
  ('valoresPosibles -> VARIABLE','valoresPosibles',1,'p_valores_posibles','sintactico.py',200),
  ('condicional -> tiposCondicion condicion LLAVEIZ golang LLAVEDE','condicional',5,'p_condicional','sintactico.py',256),
  ('condicional -> condicional ELSE LLAVEIZ golang LLAVEDE','condicional',5,'p_condicional','sintactico.py',257),
  ('tiposCondicion -> IF','tiposCondicion',1,'p_tipos_condicion','sintactico.py',263),
  ('tiposCondicion -> ELSE IF','tiposCondicion',2,'p_tipos_condicion','sintactico.py',264),
  ('condicion -> expression','condicion',1,'p_condicion','sintactico.py',269),
  ('condicion -> LPAREN expression comparadores expression RPAREN','condicion',5,'p_condicion','sintactico.py',270),
  ('condicion -> LPAREN expression comparadores expression RPAREN comparadores condicion','condicion',7,'p_condicion','sintactico.py',271),
  ('condicion -> expression comparadores condicion','condicion',3,'p_condicion','sintactico.py',272),
  ('comparadores -> MAYORQUE','comparadores',1,'p_comparadores','sintactico.py',277),
  ('comparadores -> MENORQUE','comparadores',1,'p_comparadores','sintactico.py',278),
  ('comparadores -> MAYOROIGUALQUE','comparadores',1,'p_comparadores','sintactico.py',279),
  ('comparadores -> MENOROIGUALQUE','comparadores',1,'p_comparadores','sintactico.py',280),
  ('comparadores -> EQUIVALENTE','comparadores',1,'p_comparadores','sintactico.py',281),
  ('comparadores -> DIFERENTE','comparadores',1,'p_comparadores','sintactico.py',282),
  ('bucleFor -> FOR asignacionFOR condicionFOR updateFOR LLAVEIZ golang LLAVEDE','bucleFor',7,'p_bucle_for','sintactico.py',291),
  ('asignacionFOR -> VARIABLE DOSPUNTOS ASIGNADOR expression PUNTOCOMA','asignacionFOR',5,'p_asignacion_for','sintactico.py',295),
  ('condicionFOR -> VARIABLE comparadores expression PUNTOCOMA','condicionFOR',4,'p_condicion_for','sintactico.py',299),
  ('updateFOR -> VARIABLE incrementoDecremento','updateFOR',2,'p_update_for','sintactico.py',303),
  ('incrementoDecremento -> INCREMENTO','incrementoDecremento',1,'p_incrementos_decrementos','sintactico.py',307),
  ('incrementoDecremento -> DECREMENTO','incrementoDecremento',1,'p_incrementos_decrementos','sintactico.py',308),
  ('print -> PRINT LPAREN parametro RPAREN','print',4,'p_print','sintactico.py',319),
  ('print -> PRINTLN LPAREN parametro RPAREN','print',4,'p_print','sintactico.py',320),
  ('print -> PRINTF LPAREN parametro RPAREN','print',4,'p_print','sintactico.py',321),
  ('parametro -> argumento','parametro',1,'p_parametro_print','sintactico.py',325),
  ('parametro -> argumento COMA parametro','parametro',3,'p_parametro_print','sintactico.py',326),
  ('argumento -> NUMBER','argumento',1,'p_argumento','sintactico.py',331),
  ('argumento -> FLOTANTE','argumento',1,'p_argumento','sintactico.py',332),
  ('argumento -> VARIABLE','argumento',1,'p_argumento','sintactico.py',333),
  ('argumento -> STRING','argumento',1,'p_argumento','sintactico.py',334),
  ('switch -> SWITCH argumento LLAVEIZ casos LLAVEDE','switch',5,'p_switch','sintactico.py',340),
  ('casos -> CASE argumento DOSPUNTOS golang','casos',4,'p_casos','sintactico.py',343),
  ('casos -> CASE argumento DOSPUNTOS golang casos','casos',5,'p_casos','sintactico.py',344),
  ('mat_semantica_plus -> NUMBER MAS NUMBER','mat_semantica_plus',3,'p_mat_semantica_plus','sintactico.py',352),
  ('mat_semantica_menos -> NUMBER MAS NUMBER','mat_semantica_menos',3,'p_mat_semantica_menos','sintactico.py',357),
  ('mat_semantica_multi -> NUMBER MAS NUMBER','mat_semantica_multi',3,'p_mat_semantica_multi','sintactico.py',362),
  ('expression -> expression MAS term','expression',3,'p_expression_plus','sintactico.py',368),
  ('expression -> expression RESTA term','expression',3,'p_expression_minus','sintactico.py',372),
  ('expression -> term','expression',1,'p_expression_term','sintactico.py',376),
  ('term -> term MULTI factor','term',3,'p_term_times','sintactico.py',380),
  ('term -> term DIVIDE factor','term',3,'p_term_div','sintactico.py',384),
  ('term -> factor','term',1,'p_term_factor','sintactico.py',388),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactico.py',393),
  ('factor -> FLOTANTE','factor',1,'p_factor_num','sintactico.py',394),
  ('factor -> VARIABLE','factor',1,'p_factor_num','sintactico.py',395),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','sintactico.py',400),
]
