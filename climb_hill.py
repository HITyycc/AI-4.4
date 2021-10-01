import random
# 八皇后
def gen_init_states_8_queue():
    state = []
    for i in range(8):
        state.append(random.randint(0,7))
    return state

def gen_neighbors_8_queue(current):
    neighbors = []
    cost = []
    for i in range(len(current)):
        for j in range(8):
            if current[i] == j:
                continue
            else:
                new_neighbor = current[:]
                new_neighbor[i] = j
                neighbors.append(new_neighbor)
                cost.append(get_score_8_queue(new_neighbor))
    list = []
    for i in range(len(cost)):
        list.append([neighbors[i], cost[i]])
    random.shuffle(list)
    states_shuffle = []
    cost_shuffle = []
    for _ in list:
        states_shuffle.append(_[0])
        cost_shuffle.append(_[1])
    return states_shuffle, cost_shuffle


def get_score_8_queue(state):
    score = 0
    for i in range(len(state)):
        # 竖边
        for j in range(i+1, len(state)):
            if state[i] == state[j]:
                score += 1
        # 斜边
        for j in range(1, 8-i):
            if state[i+j] == state[i] - j or state[i+j] == state[i] + j:
                score += 1
    return score

def get_most_8_queue(cost, current):
    cost_min = min(cost)
    if get_score_8_queue(current) <= cost_min:
        return -1
    else:
        return cost.index(cost_min)

def test_goal_8_queue(state):
    return get_score_8_queue(state) == 0

# 8数码

def get_position(index):
    return index // 3, index % 3


def legal_position(row, col):
    return row >= -1 and row < 3 and col >= -1 and col < 3

def position2indx(row, col):
    return row * 3 + col

def gen_init_states_8_puzzle():
    state = list(range(9))
    random.shuffle(state)
    return state

def get_score_8_puzzle(state):
    score = 0
    for i in range(9):
        if i != state[i]:
            row_cur, col_cur = get_position(state[i])
            row_tar, col_tar = get_position(i)
            score += abs(row_cur - row_tar) + abs(col_cur - col_tar)
    return score

def test_goal_8_puzzle(state):
    return get_score_8_puzzle(state) == 0

def get_most_8_puzzle(cost, current):
    cost_min = min(cost)
    if(get_score_8_puzzle(current) < cost_min):
        return -1
    else:
        return cost.index(cost_min)

def gen_neighbors_8_puzzle(current):
    neighbors = []
    cost = []
    empty_index = current.index(0)
    empty_row, empty_col = get_position(empty_index)
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for [i, j] in directions:
        now_row, now_col = empty_row + i, empty_col + j
        if legal_position(now_row, now_col):
            new_node = current[:]
            new_node[empty_index] = current[position2indx(now_row, now_col)]
            new_node[position2indx(now_row, now_col)] = 0
            neighbors.append(new_node)
            cost.append(get_score_8_puzzle(new_node))
        else:
            continue
    return neighbors, cost




