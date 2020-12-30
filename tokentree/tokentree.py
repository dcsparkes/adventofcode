"""
Interpret a token definition and use it to validate tokens
https://adventofcode.com/2020/day/19
"""
import inspect
import logging
from base import base

logging.basicConfig(filename='../log/{}.log'.format(__name__), level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TokenTrie:
    """
    Is this a trie?  I think so.
    """

    def __init__(self, token=None):
        self.isTerminal = False
        self.branches = {}
        if token is not None:
            self.insert(token)

    def __bool__(self):
        return self.isTerminal or bool(self.branches)

    def __contains__(self, token):
        if not len(token):
            retVal = self.isTerminal
        else:
            head = token[0]
            tail = token[1:]
            if head not in self.branches:
                retVal = False
            else:
                retVal = tail in self.branches[head]
        logger.debug(
            "{}.{}: token = {}, retVal = {}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name,
                                                    token, retVal))
        return retVal

    def __iadd__(self, other):
        """
        Append all the tokens from other in self as a sequence.  Leave other unchanged.
        :param other:
        :return:
        """

        if type(other) is str:
            self += TokenTrie(other)
            return self
        elif other is self:
            other = TokenTrie()
            other |= self
        elif type(other) is not TokenTrie:
            return NotImplemented

        for key in self.branches.keys():
            self.branches[key] += other

        if self.isTerminal:
            self.isTerminal = False
            self |= other
        return self

    def __ior__(self, other):
        """
        Include all the valid tokens from other in self.  Leave other unchanged.
        :param other:
        :return:
        """
        if type(other) is str:
            self.insert(other)
        elif type(other) is not TokenTrie:
            return NotImplemented
        else:  # type(other) is TokenTree
            self.isTerminal |= other.isTerminal
            for key in other.branches.keys():
                if key not in self.branches:
                    self.branches[key] = TokenTrie()
                self.branches[key] |= other.branches[key]
        return self

    def __len__(self):
        return 1 + sum([len(v) for k, v in self.branches.items()])

    def __repr__(self):
        return "{}(branches={}, isTerminal={})".format(self.__class__.__name__, list(self.branches.keys()),
                                                       self.isTerminal)

    def insert(self, token):
        """
        Insert the token into the tree as a valid terminal.
        :param token:
        :return:
        """
        if not len(token):
            self.isTerminal = True
        else:
            head = token[0]
            tail = token[1:]
            if head in self.branches:
                self.branches[head].insert(tail)

            else:
                self.branches[head] = TokenTrie(tail)


class RuleSet:
    """
    Was a tree, but now a container for unresolved rules and a temporary container for resolved rules
    """

    def __init__(self, text=None, ruleID=None):
        self.waiting = set()
        self.id = ruleID
        self.terminals = None
        self.nonTerminals = []
        if text:
            self._parse(text)
            logger.debug(
                "{}.{}: {}\n{}\n{}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name, text,
                                           self, repr(self)))

    def __repr__(self):
        params = ', '.join(
            sorted(["{}={}: {}".format(key, value, type(value)) for key, value in vars(self).items()]))
        return "{}({})".format(self.__class__.__name__, params)

    def __str__(self):
        params = ', '.join(
            sorted(["{}={}".format(key, value) for key, value in vars(self).items() if key != "terminals" and value]))
        return "{}({})".format(self.__class__.__name__, params)

    def _parse(self, line):
        # print(line)
        if line and ':' in line:
            self.id, rules = line.split(': ')
            if '\"' in rules:
                self.terminals = TokenTrie(rules.strip(' \"'))
            else:
                self.nonTerminals = [tuple(r.split(' ')) for r in rules.split(' | ')]
                self.terminals = TokenTrie()
                self.waiting |= set([ruleID for ruleSeq in self.nonTerminals for ruleID in ruleSeq])

    def isStillWaiting(self, listFinished):
        self.waiting -= set(listFinished)
        return self.waiting


class Planter:
    """
    Creates trees
    """

    def __init__(self, fileName, rootRule="0"):
        self.tokensUnvalidated = []
        self.tokensValid = []
        self.tokenValidator = None
        self.nodesEvaluated = {}
        self.nodesUnevaluated = {}
        self.waitingLists = {}
        self._parseFile(fileName)
        self.translateRules(str(rootRule))
        self.validateTokens()

    def _addToWaitingLists(self, nodeID, rules):
        for rule in rules:
            for match in rule:
                if match not in self.waitingLists:
                    self.waitingLists[match] = set([nodeID])
                else:
                    self.waitingLists[match].add(nodeID)

    def _parseFile(self, fileName):
        """
        Read section one of the file into a RuleTree and section two into a list of tokens to be validated
        :param fileName:
        :return:
        """
        for definition in base.getInputLines(fileName):
            if ':' in definition:
                node = RuleSet(definition)
                if not node:
                    pass
                elif node.terminals:
                    self.nodesEvaluated[node.id] = node.terminals
                else:
                    self.nodesUnevaluated[node.id] = node
                    self._addToWaitingLists(node.id, node.nonTerminals)
            elif definition:
                self.tokensUnvalidated.append(definition)

    def translateRules(self, rootRule="0"):
        """
        Convert RuleSets into trie
        :param rootRule: root id of trie
        :return: None?
        """
        # Initiate newlyEvaluated with the evaluated RuleSets: i.e. rules from _parseFile that are terminals.
        newlyEvaluated = set(self.nodesEvaluated.keys())  # Should contain all the 'leaves'.

        while newlyEvaluated and rootRule not in self.nodesEvaluated:
            logger.debug("{}.{}: Starting while loop: newlyEvaluated = {}: self.nodesEvaluated = {}: "
                         "self.nodesUnevaluated{}".format(self.__class__.__name__,
                                                          inspect.currentframe().f_code.co_name, newlyEvaluated,
                                                          sorted(self.nodesEvaluated.keys()),
                                                          sorted(self.nodesUnevaluated.keys())))
            # candidates = set(self.nodesUnevaluated.keys())
            candidates = set()
            for nodeID in newlyEvaluated:
                if nodeID in self.waitingLists:
                    candidates |= self.waitingLists.pop(nodeID)
                else:
                    logger.warning(
                        "{}.{}: {} not in {}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name,
                                                     nodeID, self.waitingLists))
            # Winnow candidates down to those waiting for newly evaluated/not waiting for unevaluated.
            for candidate in candidates:
                self.nodesUnevaluated[candidate].waiting -= newlyEvaluated

            candidates = [c for c in candidates if not self.nodesUnevaluated[c].waiting]

            newlyEvaluated.clear()
            logger.info("{}.{}: Starting while loop: , candidates not in nodesUnevaluated: {}, candidates = {}".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name,
                [c for c in candidates if c not in self.nodesUnevaluated], candidates))

            # for idCandidate in [c for c in candidates if c in self.nodesUnevaluated]:
            for candidate in candidates:
                node = self.nodesUnevaluated.pop(candidate)
                logger.debug(
                    "{}.{}: node = {}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name, node))
                for rule in node.nonTerminals:
                    treeTmp = None
                    for nodeID in rule:
                        if nodeID not in self.nodesEvaluated:
                            raise ValueError("{}: nodeID {} not in self.nodesEvaluated.".format(candidate, nodeID))
                        elif treeTmp is None:
                            treeTmp = TokenTrie()
                            treeTmp |= self.nodesEvaluated[nodeID]
                        else:
                            treeTmp += self.nodesEvaluated[nodeID]  # This is inordinately slow.

                    if treeTmp:
                        node.terminals |= treeTmp

                newlyEvaluated.add(node.id)
                self.nodesEvaluated[node.id] = node.terminals

                node.nonTerminals.clear()


        if rootRule not in self.nodesEvaluated:
            logger.warning("{}.{}: rootRule not evaluated. Waiting Lists:\n{}\nUnevaluated:\n{}".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, sorted(self.waitingLists),
                sorted(self.nodesUnevaluated.keys())))
        else:
            logger.debug(
                "{}.{}: node = {}".format(self.__class__.__name__, inspect.currentframe().f_code.co_name,
                                          self.nodesEvaluated[rootRule]))
            self.tokenValidator = self.nodesEvaluated[rootRule]

    def _tokenIsValid(self, token):
        return self.tokenValidator and token in self.tokenValidator

    def validateTokens(self):
        if self.tokenValidator:
            self.tokensValid = [t for t in self.tokensUnvalidated if t in self.tokenValidator]


