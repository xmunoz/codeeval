#! /usr/bin/env python

'''
My python solution to the jugglefest yodle problem on code eval.
By Cristina Munoz

example use:
$ python juggle_fest.py input_file

More info here:
    https://www.codeeval.com/open_challenges/88/
'''

# ----------
# Imports
# ----------

import sys
import string
from operator import mul

# ----------
# Functions
# ----------

def parse_input(input_file):
    '''
    Takes in file name, opens file and reads input.
    Returns file input as 2 lists, with a bit of text processing.
    '''
    text = open(input_file, 'r')
    jugglers, circuits = [[],[]], []
    for line in text:
        line = line.rstrip()
        if line:
            elems = line.split(' ')
            hep = extract_hep(elems[2:5])
            if line[0] ==  'C':
                circuits.append(hep)
            elif line[0] == 'J':
                rankings = extract_rankings(elems[5])
                jugglers[0].append(hep)
                jugglers[1].append(rankings)
    text.close()
    return jugglers, circuits

def extract_hep(hep_list):
    '''
    A text processing function.
    Extract the numeric H, E and P values into a list, with index as juggler id
    '''
    result = []
    for hep in hep_list:
        vals = hep.split(':')
        #append only the score
        result.append(int(vals[1]))
    return result
        
def extract_rankings(rankings_str):
    '''
    A text processing function.
    Extract juggler circuit rankings, which index as juggler id
    '''
    result = []
    rankings = rankings_str.split(',')
    for ranking in rankings:
        #first letter is C, strip that and add rest of string, which will be an int
        result.append(int(ranking[1:]))
    return result

def compute_optimal_pairings(jugglers, circuits):
    '''
    Computes the most optimal assignment arrangement and returns resulting matrix
    '''
    num_jugglers = sum(True for i in jugglers[0])
    num_circuits = len(circuits)
    num_jugglers_per_circuit = num_jugglers/num_circuits
    
    dot_vals = compute_dot_product_matrix(jugglers, circuits)
    #assign all jugglers to first choice
    groupings = []
    for x in range(num_circuits):
        groupings.append([])

    #first, assign jugglers to circuits based on juggler prefs
    i = 0
    for juggler_ranking in jugglers[1]:
        groupings[juggler_ranking[0]].append(i)
        i += 1
    
    #now tweak assignments to reflect HEP vals
    i = 0
    k = 0
    final_groupings = []
    # alternative method.
    # pop of begining after each iteration, then only check for available lists
    # iterative process complete when k reaches num_circuits, meaning each circuit has the appropriate number of jugglers
    while k < num_circuits:
        n = i%num_circuits
        if len(groupings[n]) > num_jugglers_per_circuit:
            k = 0
            scores = {}
            #get HEPs for all jugglers in current circuit, and store in convenient dict
            for juggler in groupings[n]:
                scores[dot_vals[juggler][n]] = juggler
            # find min HEP in circuit
            dot_circuit = scores.keys()
            dot_circuit.sort()
            # slice off the smallest scores to trim circuit to right size
            min_scores = dot_circuit[0:(len(dot_circuit)-num_jugglers_per_circuit)]
            for score in min_scores:
                j_id = scores[score]
                # delete juggler ID from grouping
                groupings[n].remove(j_id)
                # figure out what choice (1st, 2nd, 3rd) the current circuit is for juggler
                choice = jugglers[1][j_id].index(n)
                # iterate through next choice and find circuit that will take juggler
                groupings[jugglers[1][j_id][choice + 1]].append(j_id)
        
        else:
            k+=1
        i += 1
    
    write_to_file(groupings, dot_vals, jugglers[1])

    return groupings

def write_to_file(groupings, dot_prod_matrix, juggler_prefs):
    '''
    Properly formats results and write them to file
    '''

    f = open('results.txt', 'w')
    for i in range(len(groupings)-1, -1, -1):
        group = groupings[i]
        g_str = 'C' + str(i) + ' '
        for group_member in group:
            g_str += 'J' + str(group_member) + ' '
            for pref in juggler_prefs[group_member]:
                g_str += 'C' + str(pref) + ':' + str(dot_prod_matrix[group_member][pref]) +  ' '
            g_str = g_str.rstrip() + ', '
        g_str = g_str.rstrip(', ')
        f.write(g_str + '\n')
    f.close()

def compute_dot_product_matrix(jugglers, circuits):
    dot_products = []
    for j in range(len(jugglers[0])):
        dot_products.append([])
    i = 0
    for juggler in jugglers[0]:
        for circuit in circuits:
            dot_prod = sum(map(mul, circuit, juggler))
            dot_products[i].append(dot_prod)
        i += 1
    return dot_products

# -------
# Main
# -------

def main():
    '''
    TODO- write results into a file instead of just stdout
    '''
    juggles, circuits = parse_input(sys.argv[1])
    compute_optimal_pairings(juggles, circuits)

if __name__ ==  '__main__':
    main()

