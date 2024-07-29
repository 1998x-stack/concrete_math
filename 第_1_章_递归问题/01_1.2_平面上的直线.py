import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from typing import List, Tuple

class PlaneLines:
    def __init__(self, num_lines: int):
        """初始化平面直线问题。

        Args:
            num_lines (int): 直线数量。
        """
        self.num_lines = num_lines
        self.lines: List[Tuple[float, float]] = []  # 存储直线的斜率和截距
        self.fig, self.ax = plt.subplots()
        self.x = np.linspace(-10, 10, 400)

    def add_line(self, slope: float, intercept: float) -> None:
        """添加一条直线。

        Args:
            slope (float): 直线的斜率。
            intercept (float): 直线的截距。
        """
        self.lines.append((slope, intercept))

    def _draw_current_lines(self) -> None:
        """绘制当前所有的直线。"""
        self.ax.clear()
        # 生成一组颜色，确保区域的颜色不同
        color_map = plt.cm.get_cmap('rainbow', self.num_lines + 1)
        for idx, (slope, intercept) in enumerate(self.lines):
            y = slope * self.x + intercept
            self.ax.plot(self.x, y, label=f'Line {idx + 1}', color=color_map(idx))
        
        # 着色区域
        self._color_regions()
        self.ax.legend()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        
        # 更新标题
        num_areas = self._calculate_areas()
        self.ax.set_title(f"Lines: {len(self.lines)}, Areas: {num_areas}")


    def _calculate_areas(self) -> int:
        """计算当前直线划分出的区域数。

        Returns:
            int: 区域数。
        """
        return 1 + sum(range(1, len(self.lines) + 1))
    
    def _color_regions(self) -> None:
        """根据当前直线为区域着色。"""
        X, Y = np.meshgrid(np.linspace(-10, 10, 400), np.linspace(-10, 10, 400))
        Z = np.zeros(X.shape)
        color_map = plt.cm.get_cmap('rainbow', self.num_lines + 1)

        for idx, (slope, intercept) in enumerate(self.lines):
            Z += (Y > slope * X + intercept).astype(int) * (idx + 1)
        
        self.ax.imshow(Z, extent=(-10, 10, -10, 10), origin='lower', cmap=color_map, alpha=0.3)

    def generate_lines(self) -> None:
        """生成随机的直线并绘制动画。"""
        slopes = np.random.uniform(-5, 5, self.num_lines)
        intercepts = np.random.uniform(-10, 10, self.num_lines)
        
        for slope, intercept in zip(slopes, intercepts):
            self.add_line(slope, intercept)
            self._draw_current_lines()
            # plt.pause(2)  # 暂停2秒以显示动画效果

    def show(self) -> None:
        """显示图形。"""
        plt.show()

def main() -> None:
    """主函数，用于执行平面直线问题的解决过程。"""
    num_lines = 5  # 可以根据需要修改直线数量
    plane_lines = PlaneLines(num_lines)
    plane_lines.generate_lines()
    plane_lines.show()

if __name__ == "__main__":
    main()
