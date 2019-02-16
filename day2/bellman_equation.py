def V(state, gamma=0.99):
    V = R(state) + gamma * max_V_on_next_state(state)
    return V

def R(state):
    if state == "happy_end":
        return 1
    elif state == "bad_end":
        return -1
    else:
        return 0

def max_V_on_next_state(state):
    # If game end, expected value is 0.
    if state in ["happy_end", "bad_end"]:
        return 0

    actions = ["up", "down"]
    values = []
    for action in actions:
        transition_probs = transit_func(state, action)
        value = 0
        for next_state in transition_probs:
            prob = transition_probs[next_state]
            value += prob * V(next_state)
        values.append(value)
    return max(values)

def transit_func(s, a):
    """
    Make next state by adding action str to state.
    ex: (s = 'state', a = 'up') => 'state_up'
        (s = 'state_up', a = 'down') => 'state_up_down'
    """
    actions = s.split("_")[1:]
    LIMIT_GAME_COUNT = 5
    HAPPY_END_BORDER = 4
    MOVE_PROB = 0.9

    def next_state(state, action):
        return "_".join([state, action])

    if len(actions) == LIMIT_GAME_COUNT:
        up_count = sum([1 if a == "up" else 0 for a in actions])
        state = "happy_end" if up_count >= HAPPY_END_BORDER else "bad_end"
        prob = 1.0
        return {state: prob}
    else:
        opposite = "up" if a == "down" else "down"
        return {
            next_state(s, a): MOVE_PROB,
            next_state(s, opposite): 1 - MOVE_PROB
        }

if __name__ == "__main__":
    print(V("state"))
    print(V("state_up_up"))
    print(V("state_down_down"))
