"""
Interpret a token definition and use it to validate tokens
"""
import inspect
import logging
from base import base

logging.basicConfig(filename='../log/{}.log'.format(__name__), level=logging.DEBUG)
logger = logging.getLogger(__name__)

class TokenTree:
    

class RuleTree:
    def __init__(self, text=None, id=None):
        if text:
            self.id = id
            self.terminal = False
            self.nonTerminals = []
            if text:
                self._parse(text)
                logger.debug(
                    "{}.{}: {}\n{}\n{}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name, text,
                                               self, repr(self)))

    def __repr__(self):
        params = ', '.join(
            sorted(["{}={}: {}".format(key, value, type(value)) for key, value in vars(self).items() if value]))
        return "{}({})".format(self.__class__.__name__, params)

    def __str__(self):
        params = ', '.join(sorted(["{}={}".format(key, value) for key, value in vars(self).items() if value]))
        return "{}({})".format(self.__class__.__name__, params)

    def _parse(self, line):
        # print(line)
        if line and ':' in line:
            self.id, rules = line.split(': ')
            if '\"' in rules:
                self.terminal = rules.strip(' \"')
            else:
                self.nonTerminals = [tuple(r.split(' ')) for r in rules.split(' | ')]


class Planter:
    def __init__(self, fileName):
        self._parseFile(fileName)

    def _parseFile(self, fileName):
        self.nodes = {}
        tokens = []
        for definition in base.getInputLines(fileName):
            if ':' in definition:
                node = RuleTree(definition)
                if node.id:
                    self.nodes[node.id] = node

            elif definition:
                tokens.append(definition)

        print(self.nodes)
        validTokens = [token for token in tokens if self._tokenIsValid(token)]

    def _tokenIsValid(self, token):


