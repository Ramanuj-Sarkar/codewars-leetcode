def hamming(final):
    assert final >= 1, 'Final cannot be less than 1.'
    hamming_list = [1]
    new_min = 1
    xth_number = 1
    
    hamming_multiples = (2, 3, 5)   # multiples of hamming
    mult_index = [0, 0, 0]          # which number the multiple will multiply
    
    # these are the next candidates to be the minimum value
    next_candidates = [multiple * hamming_list[index] for multiple, index in zip(hamming_multiples, mult_index)]
    
    while True:
        if xth_number == final:
            return new_min
        
        new_min = min(next_candidates)
        hamming_list.append(new_min)
        xth_number += 1
        
        # this for-loop makes the min larger
        for (num, (value, x, index)) in enumerate(zip(next_candidates, hamming_multiples, mult_index)):
            if value == new_min:
                index += 1
                mult_index[num] = index  # now the next thing will be multiplied by this number
                next_candidates[num] = x * hamming_list[index]     # multiplies the index-th thing by this number
        
        # the following code stops hamming_list
        # from being unnecessarily long
        mini = min(mult_index)
        if mini >= 1000:
            del hamming_list[:mini]
            mult_index = [i - mini for i in mult_index]
