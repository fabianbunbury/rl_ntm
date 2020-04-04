# This module contains theturing machine. it describes the tape and contains the functions that move the read and write heads and insert and retrieve the data. 
# it describes a class that the ntm controller reads and writes to.

import numpy as np

class TuringMachine():
    def __init__(self,tape_length = 10):
        self.tape_length = tape_length
        self.tape = [0]* tape_length
        self.writehead_position = int(list_length/2) # FABIAN: The position of the write head. It initialises to the center of the tape.
        self.readhead_position =  int(list_length/2)

    def move_readhead(self, direction_to_move = 0): # [[][][][][][][][][]] # FABIAN: If the direction to move is +1 move the head right, if it's -1 move the head left.
        legal_direction_to_move_values = [-1,1,0]
        assert direction_to_move in legal_direction_to_move_values, "I'm teribly sorry but the direction_to_move variable must be either -1 for left or 1 for right"
        
        read_head_positions_before_check = self.readhead_position + direction_to_move

        if read_head_position_before_check >= 0 and read_head_position_before_check <  self.tape_length: #FABIAN: check if the read head is off the tape
            self.readhead_position = read_head_position_before_check

    def read_from_tape():
        return self.tape[self.readhead_position]

    def write_to_tape(input):
        self.tape[self.writehead_position] = input

    def clear_tape():
        self.tape = [0]*self.tape_length # FABIAN: im not sure if this is the corect way to do it.

    
        


    
        