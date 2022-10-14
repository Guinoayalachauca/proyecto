from PLHL.token import (
    Token,
    TokenType,
)

class Lexer:

    def __init__(self, source: str) -> None:
        self._source: str = source
        
    def next_token(self) -> Token:
        pass
