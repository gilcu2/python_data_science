def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    n_houses = len(states)
    old_states = states
    new_states = [0] * n_houses
    for i in range(days):
        for j in range(n_houses):
            left_value = 0
            if j > 0:
                left_value = old_states[j-1]
            right_value = 0
            if j < n_houses - 1:
                right_value = old_states[j+1]
            if left_value == right_value:
                new_states[j] = 0
            else:
                new_states[j] = 1
        old_states = new_states
        new_states = [0] * n_houses

    return old_states

if __name__ == '__main__':
    print(cellCompete([1,0,0,0,0,1,0,0],1))