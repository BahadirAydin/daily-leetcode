"""
1665. Minimum Initial Energy to Finish Tasks
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
"""


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        # greedy
        # (minimum - actual) is the best choice everytime
        tasks.sort(key=lambda x: -(x[1] - x[0]))

        total = 0
        current_energy = 0

        for actual, minimum in tasks:

            if current_energy < minimum:
                need = minimum - current_energy
                total += need
                current_energy += need  # which equals minimum
            current_energy -= actual

        return total
