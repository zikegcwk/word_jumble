def combination(s):
    '''
    calcualte the combination of a string
    '''
    N = pow(2, len(s))

    combs = []

    for idx in xrange(N):

        #construct the combination code for idx
        idx_bi = bin(idx)[2:][::-1]

        #combination for this particular idx
        comb = [
            s[chn_idx] for chn_idx, chn in enumerate(idx_bi) if chn == '1'
        ]

        # no empty ones
        if comb:
            combs.append(
                ('').join(comb)
            )

    return combs


def permutation(s):
    '''
    Calculate the permutation of a string
    Note that optimization by considering repeation is still of O(n!).
    '''

    # recursing exit condition.
    if len(s) == 1:
        return s
    
    rtn = []
    
    sub_s = s[1::]

    # recursion
    for sub_p in permutation(sub_s):
        for insert_idx in range(len(s)):
            
            new_p = sub_p[0:insert_idx] + s[0] + sub_p[insert_idx::]

            #take out the repeated ones for next step.
            if new_p not in rtn:
                rtn.append(
                    new_p        
                ) 

    return rtn


def parse_dictionary():
    '''
    Parse the dictionary to a dict with key being the sorted letters and  value being a 
    list of words that can have the key.

    Performance can be improved if using a trie.
    '''

    f = open('dictionary/agid-4/infl.txt', 'r')

    parsed_dict = {}

    for ln in f:
        wd = ln.split(' ')[0].lower()
        k = ('').join(sorted(wd))

        if k in parsed_dict:
            if wd not in parsed_dict[k]:
                parsed_dict[k].append(wd)
        else:
            parsed_dict.update(
                {
                    k: [wd]
                }
            )

    return parsed_dict


def is_a_word(word, parsed_dict):
    '''
    given a dictionary, check if word is in the dictionary.
    '''
    
    wd = word.lower()

    k = ('').join(sorted(wd))

    if k not in parsed_dict:
        return False

    if wd not in parsed_dict[k]:
        return False

    return word


def jumble_game(s, d):

    comb_wds = combination(s)

    ans = []

    for comb_wd in comb_wds:
        for comb_p_wd in permutation(comb_wd):
            if is_a_word(comb_p_wd, d):
                if comb_p_wd not in ans:
                    ans.append(
                        comb_p_wd
                    )

    return sorted(ans)


if __name__ == '__main__':
    
    input_s = raw_input('Welcome to Word Jumble Game! \n Please type some letters: ')

    try:
        import re
        s = "".join(re.findall("[a-zA-Z]+", input_s)).lower()
    except ImportError:
        if not input_s.isalpha():
            print 'Sorry, letters only! Please re-run the program.'
        
    s = input_s.lower()

    d = parse_dictionary()

    words = jumble_game(s, d)

    if words:
        print "Here are the words can be formed: "

    for wd in words:
        print wd




