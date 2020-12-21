"""
State-based string processing
"""
import inspect
import logging
from base import base

logging.basicConfig(filename='../log/{}.log'.format(__name__), level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class StringProcessor:
    def _id(self, char):
        return char

    def __init__(self) -> None:
        self.currentState = "INIT"
        self.Buffer = []

    def _runStateMachine(self, source):
        outputText = []
        self.currentState = "INIT"
        self.Buffer = []
        for char in source:
            index = char
            if char not in self.stateTransitions[self.currentState]:
                index = '*'
            nextState, action = self.stateTransitions[self.currentState][index]

            if action is SyntaxError:
                raise action
            elif callable(action):
                action = action(self, char)

            if action is not None:
                outputText.append(action)
            self.currentState = nextState

        if self.currentState != "END_OF_STRING":
            raise SyntaxError("String <{}> unterminated".format(source))
        return ''.join(outputText)

    processLine = _runStateMachine


class StringDecoder(StringProcessor):
    def _store(self, char):
        self.Buffer.append(char)
        if len(self.Buffer) > 1:
            # print("hex = {}. Ascii = {}".format(bytearray.fromhex(''.join(self.Buffer)).decode()))
            self.Buffer = []
            return 'A'
        else:
            return None

    # stateNames = ["INIT", "RUNNING", "SINGLE_BACKSLASH", "END_OF_STRING", "SYNTAX_ERROR"]
    # stateIDs = {name: id + 1 for id in range(len(stateNames))}
    # stateLookup = {id: name for name, id in stateIDs.items()}
    stateTransitions = {
        "INIT": {'\"': ("RUNNING", None), '*': ("SYNTAX_ERROR", SyntaxError("Unexpected char before open quote."))},
        "RUNNING": {'\"': ("END_OF_STRING", None), '\\': ("SINGLE_BACKSLASH", None),
                    '*': ("RUNNING", StringProcessor._id)},
        "SINGLE_BACKSLASH": {'\"': ("RUNNING", '\"'), '\\': ("RUNNING", '\\'), 'x': ("HEX_FIRST", None),
                             '*': ("SYNTAX_ERROR", SyntaxError("Unexpected char in escape sequence."))},
        "HEX_FIRST": {'*': ("SYNTAX_ERROR", SyntaxError("Unexpected char in escape sequence."))},
        "HEX_SECOND": {'*': ("SYNTAX_ERROR", SyntaxError("Unexpected char in escape sequence."))},
        "END_OF_STRING": {'*': ("SYNTAX_ERROR", SyntaxError("Unexpected char after close quote."))}
    }

    for c in "0123456789abcdefABCDEF":
        stateTransitions["HEX_FIRST"][c] = ("HEX_SECOND", _store)
        stateTransitions["HEX_SECOND"][c] = ("RUNNING", _store)
    del c


class StringEncoder(StringProcessor):
    """
    """
    stateTransitions = {
        "INIT": { '\\': ("INIT", "\\\\"), '"': ("INIT", "\\\""), '*': ("INIT", StringProcessor._id)}
    }
    stateTransitions = {
        "INIT": {'\"': ("RUNNING", "\"\\\""), '*': ("SYNTAX_ERROR", SyntaxError("Unexpected char before open quote."))},
        "RUNNING": {'\"': ("END_OF_STRING", "\\\"\""), '\\': ("SINGLE_BACKSLASH", r"\\"),
                    '*': ("RUNNING", StringProcessor._id)},
        "SINGLE_BACKSLASH": {'\"': ("RUNNING", '\\\"'), '\\': ("RUNNING", '\\\\'), 'x': ("RUNNING", 'x'),
                             '*': ("SYNTAX_ERROR", SyntaxError("Unexpected char in escape sequence."))},
        "END_OF_STRING": {'*': ("SYNTAX_ERROR", SyntaxError("Unexpected char after close quote."))}
    }
