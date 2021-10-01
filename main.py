import climb_hill
import random
import math
import time


def climb_hill_structure(initial_state, gen_neighbors, get_most, test_goal, limit_step):
    step = 0
    solutions = []
    current = initial_state
    while step < limit_step:
        if test_goal(current):
            return [solutions, True, step]
        step += 1
        neighbors, cost = gen_neighbors(current)
        index = get_most(cost, current)
        if index == -1:
            return [[], False]
        current = neighbors[index]
        solutions.append(current)

    return [[], False]


def p_accept(p):
    n = random.random()
    if n <= p:
        return True
    else:
        return False


def simulated_annealing_structure(init_state, gen_neighbors, test_goal, get_score, init_t, t_low, down_ratio):
    step = 0
    solutions = []
    current = init_state
    t = init_t
    while t >= t_low:
        if test_goal(current):
            return [solutions, True, step]
        step += 1
        neighbors, cost = gen_neighbors(current)
        score_cur = get_score(current)
        while True:
            index = random.randint(0, len(neighbors)-1)  # 随机选择一个后继
            now_neighbor = neighbors[index]
            score_nei = get_score(now_neighbor)
            if score_nei < score_cur:
                solutions.append(now_neighbor)
                current = now_neighbor
                break
            else:
                if p_accept(math.exp(score_cur - score_nei) / t):
                    solutions.append(now_neighbor)
                    current = now_neighbor
                    break
                else:
                    continue

        t = t * down_ratio

    return None


def climb_hill_random_8_queue_once(limit_times):
    restart_times = 0
    while restart_times < limit_times:
        init_state = climb_hill.gen_init_states_8_queue()
        res = climb_hill_structure(init_state, climb_hill.gen_neighbors_8_queue, climb_hill.get_most_8_queue, \
                                   climb_hill.test_goal_8_queue, 50)
        if res[1]:
            return [restart_times, res[2]]
        restart_times += 1
    return None


def climb_hill_8_queue():
    yes = 0
    steps = 0
    for i in range(1000):
        init_state = climb_hill.gen_init_states_8_queue()

        res = climb_hill_structure(init_state, climb_hill.gen_neighbors_8_queue, climb_hill.get_most_8_queue, \
                                   climb_hill.test_goal_8_queue, 15)
        if res[1]:
            yes+=1
            steps += res[2]

    print('8皇后爬山法')
    print('------------------------------')
    print("{:8}{:8}{:8}{:8}".format('成功个数', '失败个数', '成功率', '平均步数'))
    print("{:8d}{:12d}{:9.2f}%{:12.2f}".format(yes, 1000-yes, yes/10, steps/yes))

def climb_hill_8_puzzle():
    yes = 0
    steps = 0
    for i in range(1000):
        init_state = climb_hill.gen_init_states_8_puzzle()
        res = climb_hill_structure(init_state, climb_hill.gen_neighbors_8_puzzle, climb_hill.get_most_8_puzzle, \
                                   climb_hill.test_goal_8_puzzle, 30)
        if res[1]:
            yes+=1
            steps += res[2]
    print('8-puzzle首选爬山法')
    print('------------------------------')
    print("{:8}{:8}{:8}{:8}".format('成功个数', '失败个数', '成功率', '平均步数'))
    print("{:8d}{:12d}{:9.2f}%{:12.2f}".format(yes, 1000-yes, yes/10, steps/yes))


def climb_hill_random_8_queue():
    print('8皇后随机重启法')
    print('------------------------------')
    print("{:12}{:12}{:12}{:12}{:12}{:12}{:12}".format('重启次数上限', '成功个数', '失败个数', '成功率', '平均步数', '平均重启次数', '总共耗时'))
    for i in [5, 10, 20, 35, 50]:
        steps = 0
        restart_times = 0
        success = 0
        time_start = time.time()
        for j in range(1000):
            now = climb_hill_random_8_queue_once(i)
            if now:
                steps += now[1]
                restart_times += now[0]
                success += 1
        time_end = time.time()


        print("{:12}{:14}{:16}{:15.1%}{:16.2}{:16.2}{:16.2f}s".format(i, success, 1000-success, success/1000, \
                                                                        steps/success, restart_times / success, time_end-time_start))


def simulated_annealing_structure_8_queue():
    print('8皇后模拟退火')
    print('------------------------------')
    print("{:12}{:12}{:12}{:12}{:12}{:12}{:12}{:12}".format('初始温度', '最低温度', '温度衰退率', '成功个数', '失败个数', \
                                                       '成功率', '平均步数',  '总共耗时'))
    for i in [0.8, 0.9, 0.99]:
        yes = 0
        steps = 0
        time_start = time.time()
        for j in range(1000):
            init_state = climb_hill.gen_init_states_8_queue()

            res = simulated_annealing_structure(init_state, climb_hill.gen_neighbors_8_queue, \
                                                climb_hill.test_goal_8_queue,  \
                                                climb_hill.get_score_8_queue, 100, 1, i)
            if res:
                yes += 1
                steps += res[2]
        time_end = time.time()
        print("{:<16}{:<14}{:12.2f}{:14}{:14}{:15.1%}{:16.2}{:16.2f}s".format(1, 100, i, yes, 1000-yes, yes/1000, \
                                                                              steps/yes, time_end-time_start))


def simulated_annealing_structure_8_puzzle():
    print('8-puzzle模拟退火')
    print('------------------------------')
    print("{:12}{:12}{:12}{:12}{:12}{:12}{:12}{:12}".format('初始温度', '最低温度', '温度衰退率', '成功个数', '失败个数', \
                                                            '成功率', '平均步数',  '总共耗时'))
    for i in [0.8, 0.9, 0.99]:
        yes = 0
        steps = 0
        time_start = time.time()
        for j in range(1000):
            init_state = climb_hill.gen_init_states_8_puzzle()

            res = simulated_annealing_structure(init_state, climb_hill.gen_neighbors_8_puzzle, \
                                                climb_hill.test_goal_8_puzzle, \
                                                climb_hill.get_score_8_puzzle, 100, 1, i)
            if res:
                yes += 1
                steps += res[2]
        time_end = time.time()
        print("{:<16}{:<14}{:12.2f}{:14}{:14}{:15.1%}{:16.2f}{:16.2f}s".format(1, 100, i, yes, 1000-yes, yes/1000, \
                                                                              steps/yes, time_end-time_start))



if __name__ == '__main__':
    # time_start = time.time()
    # climb_hill_8_queue()
    # climb_hill_8_puzzle()
    # climb_hill_random_8_queue()
    simulated_annealing_structure_8_queue()
    simulated_annealing_structure_8_puzzle()
    # time_end = time.time()
    # print('总共耗时', time_end - time_start, 's')
