# 00_1.1_河内塔

"""
Lecture: /第_1_章_递归问题
Content: 00_1.1_河内塔
"""

from typing import List, Tuple, Dict

class TowerOfHanoi:
    def __init__(self, num_disks: int):
        """初始化河内塔问题。

        Args:
            num_disks (int): 圆盘数量。
        """
        self.num_disks = num_disks
        self.actions: List[str] = []
        self.status: Dict[str, List[int]] = {
            'A': list(range(num_disks, 0, -1)),
            'B': [],
            'C': []
        }

    def solve(self) -> None:
        """解决河内塔问题，并记录移动步骤和状态。"""
        self._move_disks(self.num_disks, 'A', 'C', 'B')

    def _move_disks(self, n: int, source: str, target: str, auxiliary: str) -> None:
        """递归地移动圆盘。

        Args:
            n (int): 移动的圆盘数量。
            source (str): 源柱子。
            target (str): 目标柱子。
            auxiliary (str): 辅助柱子。
        """
        if n == 1:
            self._move_single_disk(source, target)
        else:
            self._move_disks(n - 1, source, auxiliary, target)
            self._move_single_disk(source, target)
            self._move_disks(n - 1, auxiliary, target, source)

    def _move_single_disk(self, source: str, target: str) -> None:
        """移动一个圆盘，并记录动作和状态。

        Args:
            source (str): 源柱子。
            target (str): 目标柱子。
        """
        disk = self.status[source].pop()
        self.status[target].append(disk)
        self.actions.append(f"Move disk {disk} from {source} to {target}")
        print("## This is the {}th action".format(len(self.actions)))
        print(f"### Move disk {disk} from {source} to {target}")
        self._print_status()

    def _print_status(self) -> None:
        """打印当前状态。"""
        print("Status:")
        for peg in ['A', 'B', 'C']:
            print(f"{peg}: {self.status[peg]}")
        print("-" * 20)

    def get_actions(self) -> List[str]:
        """获取移动步骤列表。

        Returns:
            List[str]: 移动步骤列表。
        """
        return self.actions

    def get_status(self) -> Dict[str, List[int]]:
        """获取当前状态。

        Returns:
            Dict[str, List[int]]: 当前状态。
        """
        return self.status


def main() -> None:
    """主函数，用于执行河内塔问题的解决过程。"""
    num_disks = 4  # 可以根据需要修改圆盘数量
    hanoi = TowerOfHanoi(num_disks)
    hanoi.solve()

if __name__ == "__main__":
    main()
