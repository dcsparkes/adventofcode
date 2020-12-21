import inspect
import logging

class Risc():
    def __init__(self, fileName):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("{}.{}(\"{}\")".format(self.__class__.__name__,
                                                                        inspect.currentframe().f_code.co_name,
                                                                        fileName))
        self.acc = 0
        self.haltPos = None
        self.riscInstructions = {}

        if fileName:
            self.readASM(fileName)
            # self.runRisc(dict(self.riscInstructions))

    def throughtrace(self):
        """Run from start (0) to find loop.  Run from next lowest pos.  Identify group loops until haltPos is reached.
        Then work through original run trying possible switches until final group is reached.
        Refinement: The only interesting paths are the halting ones.  Looping ones can be discarded."""
        groupCurrent = {} # currentGroup
        groupHalting = {} # haltingGroup
        instructions = dict(self.riscInstructions)

        while instructions:
            endPos = self.runRisc(instructions, min(instructions.keys()), groupCurrent)
            if endPos == self.haltPos or endPos in groupHalting:
                groupHalting |= groupCurrent
            groupCurrent = {}

        self.runRisc(dict(self.riscInstructions), start=0, bin=None, dests=list(groupHalting.keys()))

    # def backtrace(self):
    #     """Options:
    #     1. bruteforce sequentially switch each nop to jmp or vice versa and re-evaluate
    #     2. trackback.  Find every instruction that terminates e.g jmp + pos = haltPos
    #         a: Any jump/nop that jumps off the end must be a nop
    #         b: any jump that jumps to a terminable must stay a jump (because changing it wouldn't fix the flow).
    #         c: any negative jump that precedes a terminable would become terminable as a nop (but might be inaccessible)
    #     3. Some kind of vector analysis
    #
    #     Solution:   track backwards mark any that connect to terminal or terminables as same group (1)
    #                 Next group = 2 and so on, with possibility of having to renumber with jumps
    #                 Is it worth tracking whether alternatives are possible with switch?  Tuple for second value?
    #     """
    #     self.logger.debug("{}.{}()".format(self.__class__.__name__, inspect.currentframe().f_code.co_name))
    #     possiblePivots = [] # Keep track of possible alterations or calculate afterward?
    #     cGroup = 1 # current group
    #     terminableGroups = [None] * self.haltPos + [cGroup]
    #
    #     for i in range(self.haltPos-1, -1, -1):
    #         curJump = self.riscInstructions[i][1]
    #         self.logger.debug("{}.{}: i:{}, group:{}, risc:{}, curJump:{}, altJump:{}".format(
    #             self.__class__.__name__, inspect.currentframe().f_code.co_name, i, terminableGroups[i],
    #             self.riscInstructions[i], curJump, self.altJumps[i]))
    #         # print("\ni:{}, group:{}, risc:{}, curJump:{}, altJump:{}".format(
    #         #     i, terminableGroups[i], self.riscInstructions[i], curJump, self.altJumps[i]))
    #
    #         if curJump == self.altJumps[i]: # True for ACCs and NOPs/JMPs where value == 1.
    #             terminableGroups[i] = terminableGroups[i+curJump]
    #
    #         else: # Test switch... very brute force... possibly a sign of giving up
    #             self.logger.debug("{}.{}: Brute Switch i:{}, group:{}, risc:{}, curJump:{}, altJump:{}".format(
    #                 self.__class__.__name__, inspect.currentframe().f_code.co_name, i, terminableGroups[i],
    #                 self.riscInstructions[i], curJump, self.altJumps[i]))
    #             newIs = dict(self.riscInstructions)
    #             newIs[i] = (0, self.altJumps[i])
    #             if self.runRisc(newIs) == self.haltPos:
    #                 self.logger.debug("{}.{}: Brute Switch Worked! i:{}".format(
    #                     self.__class__.__name__, inspect.currentframe().f_code.co_name, i))
    #                 # print("{}.{}: Brute Switch Worked! i:{}".format(
    #                 #     self.__class__.__name__, inspect.currentframe().f_code.co_name, i))
    #                 return self.acc
    #
    #
    #         # elif curJump > 0 and curJump + i <= self.haltPos + 1:
    #         #     pass
    #
    #         self.logger.debug("{}.{}: i:{}, group:{}, risc:{}, curJump:{}, altJump:{}".format(
    #             self.__class__.__name__, inspect.currentframe().f_code.co_name, i, terminableGroups[i],
    #             self.riscInstructions[i], curJump, self.altJumps[i]))
    #         # print("i:{}, group:{}, risc:{}, curJump:{}, altJump:{}".format(
    #         #     i, terminableGroups[i], self.riscInstructions[i], curJump, self.altJumps[i]))
    #         # print(terminableGroups)
    #
    #         # exit()

    def readASM(self, fileName):
        self.logger.debug("{}.{}(\"{}\")".format(self.__class__.__name__,
                                                inspect.currentframe().f_code.co_name,
                                                fileName))
        i = 0
        with open(fileName) as inFile:
            for line in inFile:
                instruction = self.translate(line.strip())
                self.logger.debug("{}.{}: line {}:\"{}\": {}".format(self.__class__.__name__,
                                                         inspect.currentframe().f_code.co_name,
                                                         i, line.strip(), instruction))
                if instruction:
                    self.riscInstructions[i] = instruction
                    i += 1
        self.haltPos = i
        self.logger.debug("{}.{}: maxPos={}, haltPos={})".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name,
            max(self.riscInstructions.keys()), self.haltPos))

    def runRisc(self, instructionsCopy, start=0, bin=None, dests=None):
        """Return stop position: either infinite loop or end (=self.haltPos)
        3 running modes:    bin=None, dest=None: 8.1 default
                            bin={}, dest=None: findHalting for throughtrace.
                            bin=None, dest=[...]: find alt route to halting."""
        self.logger.debug("{}.{}(start={}, bin={}, dest={})".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, start, bin, dests))
        self.acc = 0
        pos = start
        unfixed = bool(dests)
        if dests:
            dests.append(self.haltPos)

        while(pos in instructionsCopy):
            if bin != None:
                bin[pos] = instructionsCopy[pos]

            inc, jump, alt = instructionsCopy.pop(pos)
            self.logger.debug("{}.{}: Pos: {}: risc: ({}, {}, {}), unfixed: {}:".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, pos, inc, jump, alt, unfixed))

            if unfixed and (jump != alt) and ((pos + jump) in dests): # alternate jump is available and leads to a halting path
                self.logger.info("{}.{}: CodeFix. Pos: {}: risc: ({}, {}, {}), unfixed: {}:".format(
                    self.__class__.__name__, inspect.currentframe().f_code.co_name, pos, inc, jump, alt, unfixed))
                unfixed = False
                jump = alt

            if bin:
                bin[pos] = (inc, jump)
            self.logger.debug("{}.{}: state={}: risc={}".format(self.__class__.__name__,
                                                                inspect.currentframe().f_code.co_name,
                                                                (self.acc, pos), (inc, jump)))
            self.acc += inc
            pos += jump

        self.logger.info("{}.{}: EndPos: {}: EndAcc: {}".format(
            self.__class__.__name__, inspect.currentframe().f_code.co_name, pos, self.acc))
        return pos

    def translate(self, line):
        """Turn ASM into RISC instructions: (acc, jump, alt) = accumulator increment, jump, alternative jump."""
        self.logger.debug("{}.{}({})".format(self.__class__.__name__,
                                             inspect.currentframe().f_code.co_name, line))
        retVal = None
        instruction, value = line.split()
        if instruction == "nop":
            retVal = (0, 1, int(value))
        elif instruction == "acc":
            retVal = (int(value), 1, 1)
        elif instruction == "jmp":
            retVal = (0, int(value), 1)
        else:
            self.logger.info("{}.{}: instruction \"{}\" not recognised ".format(
                self.__class__.__name__, inspect.currentframe().f_code.co_name, instruction))
        return retVal

