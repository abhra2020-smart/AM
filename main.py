from lexer import Lexer

while True:
    try:
        text = input("AM> ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        print(list(tokens))
    except Exception as e:
        print(e)
