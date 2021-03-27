from lexer import Lexer
from parser_ import Parser

while True:
	text = input("AM> ")
	lexer = Lexer(text)
	tokens = lexer.generate_tokens()
	parser = Parser(tokens)
	tree = parser.parse()
	if not tree:
		continue
	print(tree)
