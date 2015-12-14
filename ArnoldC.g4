grammar ArnoldC;

program
    : main_function
    ;
   
main_function
    : BEGINMAIN statements ENDMAIN
    | BEGINMAIN ENDMAIN
    ;
   
statements
    : statement | statements statement
    ;

statement
    : var_decl_stmt
    | var_assign_stmt
    | print_stmt
    ;
 
print_stmt
    : print_var_stmt
    | print_sconst_stmt
    ;

print_sconst_stmt
    : PRINT STRING_LITERAL
    ;
    
print_var_stmt
    : PRINT IDENTIFIER
    ;

var_decl_stmt 
    : DECLAREINT IDENTIFIER SETINITIALVALUE expression 
    ;

expression
    : IDENTIFIER #varexpr
    | NUMBER     #numberexpr
    | AT TRUE    #trueexpr
    | AT FALSE   #falseexpr
    ;

var_assign_stmt
    : ASSIGNVARIABLE IDENTIFIER SETVALUE expression operations ENDASSIGNVARIABLE
    ;
    
operations
    : operation | operations operation
    ;
    
operation
    : PLUSOPERATOR expression           #plusop
    | MINUSOPERATOR expression          #minusop
    | MULTIPLICATIONOPERATOR expression #multiplicationop
    | DIVISIONOPERATOR expression       #divisionop
    | EQUALTO expression                #equalop
    | GREATERTHAN expression            #greaterop
    | OR expression                     #orop
    | AND expression                    #andop
    ;


BEGINMAIN
    : 'IT\'S SHOWTIME'
    ;
    
ENDMAIN
    : 'YOU HAVE BEEEN TERMINATED'
    ;

AT
    : '@'
    ;
    
TRUE
    : 'NO PROBLEMO'
    ;

FALSE
    : 'I LIED'
    ;
    
PLUSOPERATOR
    : 'GET UP'
    ;
    
MINUSOPERATOR
    : 'GET DOWN'
    ;
    
MULTIPLICATIONOPERATOR
    : 'YOU\'RE FIRED'
    ;
    
DIVISIONOPERATOR
    : 'HE HAD TO SPLIT'
    ;
    
EQUALTO
    : 'YOU ARE NOT YOU YOU ARE ME'
    ;
    
GREATERTHAN
    : 'LET OFF SOME STEAM BENNET'
    ;

OR
    : 'CONSIDER THAT A DIVORCE'
    ;
    
AND
    : 'KNOCK KNOCK'
    ;

PRINT
    : 'TALK TO THE HAND'
    ;

DECLAREINT
    : 'HEY CHRISTMAS TREE'
    ;
    
SETINITIALVALUE
    : 'YOU SET US UP'
    ;
    
ASSIGNVARIABLE
    : 'GET TO THE CHOPPER'
    ;

SETVALUE
    : 'HERE IS MY INVITATION'
    ;
    
ENDASSIGNVARIABLE
    : 'ENOUGH TALK'
    ;
    
IDENTIFIER
    : [a-zA-Z]+
    ;

NUMBER
    : DIGIT+
    ;
    
STRING_LITERAL
 : ( SHORT_STRING | LONG_STRING )
 ;
   
WS 
    : [ \r\n\t]+ -> channel(HIDDEN)
    ;

/*
 * fragments
 */

fragment DIGIT
    : ('0'..'9')
    ;
 
fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"'
 ;

fragment LONG_STRING
 : '\'\'\'' LONG_STRING_ITEM*? '\'\'\''
 | '"""' LONG_STRING_ITEM*? '"""'
 ;

fragment LONG_STRING_ITEM
 : LONG_STRING_CHAR
 | STRING_ESCAPE_SEQ
 ;

fragment LONG_STRING_CHAR
 : ~'\\'
 ;
 
fragment STRING_ESCAPE_SEQ
 : '\\' .
 ;