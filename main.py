from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser

print('Starting Shell...')

while True:
	try:
		text = input("FlowLang Shell> ")
		lexer = Lexer(text)
		tokens = lexer.generate_tokens()
		parser = Parser(tokens)
		tree = parser.parse()
		if not tree: continue
		interpreter = Interpreter()
		value = interpreter.visit(tree)
		print(value)
	except Exception as e:
		print('\033[31m' + str(e))
		print('\033[0m', end='')
