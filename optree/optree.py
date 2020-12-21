"""
A tree of operations, The output goes up the tree, inputs are down
"""
import inspect
import logging
import operator
import re
from base import base

logging.basicConfig(filename='../log/{}.log'.format(__name__), level=logging.DEBUG)
logger = logging.getLogger(__name__)


class Optree:
    """
    Apply operations across a binary tree.
    """
    opLookUp = {}
    resolver = None
    evaluatedOutputs = {}
    unevaluatedWaiting = {}

    def __init__(self, operation=None, output=None, branches=[], leaf=None):
        self.unresolvedInputs = branches
        self.branches = branches
        self.leaf = leaf
        self.operation = operation
        self.output = output
        if not self.unresolvedInputs:  # Resolvable
            self.evaluate()

    def __repr__(self):
        params = ', '.join(sorted(["{}={}".format(key, value) for key, value in vars(self).items() if value]))
        return "{}({})".format(self.__class__.__name__, params)

    def __str__(self):
        params = ', '.join(sorted(["{}={}".format(key, value) for key, value in vars(self).items() if value]))
        return "{}({})".format(self.__class__.__name__, params)

    def evaluate(self):
        # print("Evaluating: ", self)
        self.unresolvedInputs = [input for input in self.branches if input not in self.evaluatedOutputs]

        if self.unresolvedInputs or not self.operation:  # Unresolved
            for ip in self.unresolvedInputs:
                if ip not in self.unevaluatedWaiting:
                    self.unevaluatedWaiting[ip] = [self]
                elif self not in self.unevaluatedWaiting[ip]: # and ip in self.unevaluatedWaiting
                    self.unevaluatedWaiting[ip].append(self)
            return

        elif not self.branches:  # Unary operator
            self.evaluatedOutputs[self.output] = self.operation(self.leaf)

        elif self.leaf:  # Non-commutative
            # print(self.operation)
            self.evaluatedOutputs[self.output] = self.operation(self.evaluatedOutputs[self.branches[0]], self.leaf)

        elif self.operation:  # Commutative
            args = [self.evaluatedOutputs[branch] for branch in self.branches]
            self.evaluatedOutputs[self.output] = self.operation(*args)

        else:
            logger.critical("{}.{}: Unmatched evaluation\"{}\"".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, self))
            return None

        logger.debug("{}.{}: Evaluated \"{}\"".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, self.evaluatedOutputs[self.output]))

        if self.output in self.unevaluatedWaiting:
            waitingNodes = self.unevaluatedWaiting.pop(self.output)
            for node in waitingNodes:
                node.evaluate()
        return self.evaluatedOutputs[self.output]


class DummyOpTree(Optree):
    opLookUp = {"EMPTYish": True}


def _invert(x):
    return x ^ 65535


class BooleanOpTree(Optree):
    """
    operator.and_, operator.or_, operator.lshift, operator.rshift, operator.not_
    """
    opLookUp = {"NOT": _invert, "LSHIFT": operator.lshift, "RSHIFT": operator.rshift,
                "AND": operator.and_, "OR": operator.or_, "ID": int}

    evaluatedOutputs = {}


class BinaryTreePlanter():
    def __init__(self, fileName=None):
        if fileName:
            self.evaluatedOutputs = {}
            self._populateTree(fileName)

    def _invert(self, x):
        return x ^ 65535

    def _turnDefinitionIntoTreeNode(self, definition):
        output = None
        inputDef = None

        if not definition:  # Empty line
            return None
        else:
            inputDef, output = definition.split(' -> ')
            logger.debug("{}.{}: definition \"{}\": IPs \"{}\": OP: \'{}\'".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, definition, inputDef, output))

        # Task 2 hack
        if output == 'b':
            inputDef = "46065"


        match = re.match("(\d+)$", inputDef)
        if match:  # Leaf Node
            node = BooleanOpTree(operation=BooleanOpTree.opLookUp["ID"], output=output, leaf=int(match.group(0)))
            logger.debug("{}.{}: Matched & returned leaf node:\n{}.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, node))
            return node

        match = re.match("([a-z]+)$", inputDef)
        if match:  # Passthrough
            node = BooleanOpTree(operation=BooleanOpTree.opLookUp["ID"], output=output, branches=[match.group(0)])
            logger.debug("{}.{}: Matched & returned passthrough node:\n{}.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, node))
            return node

        match = re.match("([a-z]+) ([A-Z]+) (\d+)", definition)
        if match:  # Commutative 2 Parameter Boolean
            node = BooleanOpTree(operation=BooleanOpTree.opLookUp[match.group(2)], output=output,
                                 branches=[match.group(1)], leaf=int(match.group(3)))
            logger.debug("{}.{}: Matched & returned non-commutative node:\n{}.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, node))
            return node

        match = re.match("([a-z]+) ([A-Z]+) ([a-z]+)", definition)
        if match:  # Commutative 2 Parameter Boolean
            node = BooleanOpTree(operation=BooleanOpTree.opLookUp[match.group(2)], output=output,
                                 branches=[match.group(1), match.group(3)])
            logger.debug("{}.{}: Matched & returned commutative node:\n{}.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, node))
            return node

        match = re.match("(\d+) ([A-Z]+) ([a-z]+)", definition)
        if match:  # Commutative 2 Parameter Boolean treated as non-commutative
            node = BooleanOpTree(operation=BooleanOpTree.opLookUp[match.group(2)], output=output,
                                 branches=[match.group(3)], leaf=int(match.group(1)))
            logger.debug("{}.{}: Matched & returned commutative node:\n{}.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, node))
            return node

        match = re.match("([A-Z]+) ([a-z]+)", definition)
        if match:
            node = BooleanOpTree(operation=BooleanOpTree.opLookUp[match.group(1)], output=output,
                                 branches=[match.group(2)])
            logger.debug("{}.{}: Matched & returned unary operator node:\n{}.".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, node))
            return node

        print("UNMATCHED \"{}\".".format(inputDef))
        logger.critical("{}.{}: Unmatched \"{}\"".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, inputDef))

    def _populateTree(self, fileName):
        BooleanOpTree.evaluatedOutputs.clear()

        nodes = []
        for definition in base.getInputLines(fileName):
            node = self._turnDefinitionIntoTreeNode(definition)
            if node and node.unresolvedInputs:
                nodes.append(node)

        nodeCount = len(nodes) + 1
        while nodeCount > len(nodes):
            nodeCount = len(nodes)
            print("Starting loop: {} nodes.".format(nodeCount))
            activeNodes = nodes[:]
            nodes = []
            for node in activeNodes:
                node.evaluate()
                if node.unresolvedInputs:
                    nodes.append(node)

        self.evaluatedOutputs = {k: v for k, v in BooleanOpTree.evaluatedOutputs.items()}

        print("evaluatedOutputs: ", sorted(BooleanOpTree.evaluatedOutputs))
