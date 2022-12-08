"""
def max_value_alphabeta(state, alpha, beta):
    if state is terminal:
        return score(state)

    values = []
    for a in get_actions(state):
        v = min_value_alphabeta(state.get_child(a), alpha, beta)
        values.append(v)

    if v >= beta:
        return v
    alpha = max(alpha, v)

    value = max(values)
    action = argmax(values)

    return value, action



def min_value_alphabeta(state, alpha, beta):
    if state is terminal:
        return score(state)

    values = []
    for a in get_actions(state):
        v = max_value_alphabeta(state.get_child(a), alpha, beta)
        values.append(v)

    if v <= beta:
        return v
    alpha = min(alpha, v)

    value = min(values)
    action = argmin(values)

    return value, action

"""