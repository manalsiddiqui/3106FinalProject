# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

value = 0
score = 0
values
def max_value(state):
    if state is terminal:
        return score(state)

    values = []
    for a in get_actions(state):
        v = min_value(state.get_child(a))
        values.append(v)

    value = max(values)
    action = argmax(values)

    return value, action

def min_value(state):
    if state is terminal:
        return score(state)

    values = []
    for a in get_actions(state):
        v = max_value(state.get_child(a))
        values.append(v)

    value = min(values)
    action = argmin(values)

    return value, action


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

