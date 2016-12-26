import  ply.yacc as yacc
import os
import codecs
import re
from Alexico import tokens
from sys import stdin

precedence = (
    ('right','ASIGNAR') ,
    ('right','UPDATE'),
('left','LPAREN','RPAREN'),
('right',''),


)

