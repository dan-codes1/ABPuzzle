import sys
import heapq
import random


class AB:
    def __init__(self, n: int):
        self.n = n
        self.large_disks = []
        self.small_disks = []
        self.goal_state = []
        self.configure()

    def configure(self):
        def configure_disks(n: int) -> ([int], [int]):
            large_disks = []
            small_disks = []

            for _ in range(n ** 2):
                large_disks.append(random.randint(1, 4))
            large_disks.append(random.randint(1, 4))  # n^2 + 1

            for i in range(1, n + 1):
                small_disks.extend([i] * n)
            small_disks.append(0)  # The uncovered small disk

            random.shuffle(small_disks)
            random.shuffle(large_disks)
            return (small_disks, large_disks)

        def configure_goal_state(n: int) -> [int]:
            goal_state = []
            for i in range(1, n + 1):
                goal_state.extend([i] * n)
            goal_state.append(0)
            return goal_state

        self.small_disks, self.large_disks = configure_disks(n=self.n)
        self.goal_state = configure_goal_state(n=self.n)

    def heuristic(self, state: [int]) -> int:
        sum = 0
        for i in range(0, n - 1):
            if state[i] != self.goal_state[i]:
                sum += 1
        return sum

    def get_possible_moves(self, state: [int]) -> [[int]]:
        zero_idx = state.index(0)
        move = self.large_disks[zero_idx]
        neighbors = []

        def swap_and_create(new_index: int):
            new_state = state[:]
            # swap the disks
            new_state[zero_idx], new_state[new_index] = new_state[new_index], new_state[zero_idx]
            neighbors.append(new_state)

        state_size = len(state)
        swap_and_create((zero_idx - move) % state_size)
        swap_and_create((zero_idx + move) % state_size)
        swap_and_create((zero_idx - 1) % state_size)
        swap_and_create((zero_idx + 1) % state_size)
        return neighbors

    def get_path(self, parent_map: dict[(int), [int]], state: [int]) -> [[int]]:
        path = []
        curr = state
        while curr is not None:
            path.append(curr)
            curr = parent_map[tuple(curr)]
        path.reverse()
        return path

    def solve(self) -> [[int]]:
        initial_state = self.small_disks
        if initial_state == self.goal_state:  # trivial case.
            return [initial_state]

        priority_queue: [(int, [int])] = []  # min-heap for best first search
        heapq.heappush(priority_queue, (self.heuristic(initial_state), initial_state))
        visited: set[tuple[int]] = set()  # using tuples instead of arrays because they are hashable for sets
        visited.add(tuple(initial_state))

        # to help get the solution path. Key is the state, value is the parent of the state.
        path_map: dict[(int), [int]] = {tuple(initial_state): None}

        while priority_queue:
            _, curr_state = heapq.heappop(priority_queue)
            possible_moves = self.get_possible_moves(curr_state)
            for move in possible_moves:
                move_tuple = tuple(move)
                if move_tuple not in visited:
                    visited.add(move_tuple)
                    path_map[move_tuple] = curr_state
                    if move == self.goal_state:  # solved!
                        return self.get_path(path_map, move)
                    hamming_distance = self.heuristic(move)
                    heapq.heappush(priority_queue, (hamming_distance, move))

        return None  # no solution


if __name__ == "__main__":
    n = int(sys.argv[1])
    puzzle = AB(n)
    solution = puzzle.solve()
    print("Large disks:", puzzle.large_disks)
    print("Small disks:", puzzle.small_disks)
    print()
    if solution:
        print("Solution is")
        for state in solution:
            print(state)
    else:
        print("No solution")
