# lexer.py

class TokenType:
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    OPERATOR = 'OPERATOR'
    COMMENT = 'COMMENT'
    WHITESPACE = 'WHITESPACE'

KEYWORDS = {"si", "ou", "ak", "mwen", "li", "pou", "nan"}

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.position = 0
        self.current_char = self.source[self.position]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.position += 1
        if self.position >= len(self.source):
            self.current_char = None
        else:
            self.current_char = self.source[self.position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        token_type = TokenType.KEYWORD if result in KEYWORDS else TokenType.IDENTIFIER
        return Token(token_type, result)

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result))

    def string(self):
        result = ''
        self.advance()  # skip starting quote
        while self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # skip ending quote
        return Token(TokenType.STRING, result)

    def comment(self):
        result = ''
        self.advance()  # skip starting #
        while self.current_char is not None and self.current_char != '\n':
            result += self.current_char
            self.advance()
        return Token(TokenType.COMMENT, result)

    def next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isalpha():
                return self.identifier()
            if self.current_char.isdigit():
                return self.number()
            if self.current_char == '"':
                return self.string()
            if self.current_char == '#':
                return self.comment()
            if self.current_char in '+-*/=<>':
                token = Token(TokenType.OPERATOR, self.current_char)
                self.advance()
                return token

            self.error()

        return None  # EOF

# Example usage
if __name__ == '__main__':
    source_code = 'mwen si ou ak li # sa a se yon komantè'
    lexer = Lexer(source_code)
    token = lexer.next_token()
    while token is not None:
        print(token)
        token = lexer.next_token()