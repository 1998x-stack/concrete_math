structure = toc = {
    "前言": [],
    "第_1_章_递归问题": [
        "1.1_河内塔",
        "1.2_平面上的直线",
        "1.3_约瑟夫问题",
        "习题"
    ],
    "第_2_章_和式": [
        "2.1_记号",
        "2.2_和式和递归式",
        "2.3_和式的处理",
        "2.4_多重和式",
        "2.5_一般性的方法",
        "2.6_有限微积分和无限微积分",
        "2.7_无限和式",
        "习题"
    ],
    "第_3_章_整值函数": [
        "3.1_底和顶",
        "3.2_底和顶的应用",
        "3.3_底和顶的递归式",
        "3.4_mod_二元运算",
        "3.5_底和顶的和式",
        "习题"
    ],
    "第_4_章_数论": [
        "4.1_整除性",
        "4.2_素数",
        "4.3_素数的例子",
        "4.4_阶乘的因子",
        "4.5_互素",
        "4.6_mod_同余关系",
        "4.7_独立剩余",
        "4.8_进一步的应用",
        "4.9_φ函数和μ函数",
        "习题"
    ],
    "第_5_章_二项式系数": [
        "5.1_基本恒等式",
        "5.2_基本练习",
        "5.3_处理的技巧",
        "5.4_生成函数",
        "5.5_超几何函数",
        "5.6_超几何变换",
        "5.7_部分超几何和式",
        "5.8_机械求和法",
        "习题"
    ],
    "第_6_章_特殊的数": [
        "6.1_斯特林数",
        "6.2_欧拉数",
        "6.3_调和数",
        "6.4_调和求和法",
        "6.5_伯努利数",
        "6.6_斐波那契数",
        "6.7_连项式",
        "习题"
    ],
    "第_7_章_生成函数": [
        "7.1_多米诺理论与换零钱",
        "7.2_基本策略",
        "7.3_解递归式",
        "7.4_特殊的生成函数",
        "7.5_卷积",
        "7.6_指数生成函数",
        "7.7_狄利克雷生成函数",
        "习题"
    ],
    "第_8_章_离散概率": [
        "8.1_定义",
        "8.2_均值和方差",
        "8.3_概率生成函数",
        "8.4_抛掷硬币",
        "8.5_散列法",
        "习题"
    ],
    "第_9_章_渐近式": [
        "9.1_量的等级",
        "9.2_大O记号",
        "9.3_O运算规则",
        "9.4_两个渐近技巧",
        "9.5_欧拉求和公式",
        "9.6_最后的求和法",
        "习题"
    ],
}




import os
import json
from typing import Union, Dict, List, Any

def create_directories_and_files(
    base_path: str, 
    structure: Dict[str, Any], 
    readme_file, 
    parent_path: str = "", 
    level: int = 1
):
    """
    根据给定的目录结构创建目录和文件，并生成 README.md 文件。

    Args:
        base_path (str): 根目录路径。
        structure (Dict[str, Any]): 目录结构的嵌套字典。
        readme_file (File): 用于写入README内容的文件对象。
        parent_path (str): 父目录路径。
        level (int): 目录的层级，用于确定 README 标题级别。

    Returns:
        None
    """
    heading = "#" * level

    for key, value in structure.items():
        current_path = os.path.join(base_path, key.replace(" ", "_").replace("/", "_").replace("-", "_"))

        # 创建目录
        os.makedirs(current_path, exist_ok=True)

        # 在README中添加章节标题
        if parent_path:
            readme_file.write(f"{heading} {parent_path}/{key}\n\n")
        else:
            readme_file.write(f"{heading} {key}\n\n")

        # 递归调用创建子目录和文件
        if isinstance(value, dict) and value:
            create_directories_and_files(
                current_path, 
                value, 
                readme_file, 
                parent_path + "/" + key if parent_path else key, 
                level + 1
            )
        elif isinstance(value, list) and value:
            for idx, item in enumerate(value):
                if isinstance(item, dict) and item:
                    create_directories_and_files(
                        current_path, 
                        item, 
                        readme_file, 
                        parent_path + "/" + key if parent_path else key, 
                        level + 1
                    )
                else:
                    item = f"{idx:02d}_{item}"
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.py)\n")
                    
                    
                    file_name = item.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
                    file_path = os.path.join(current_path, file_name)
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f"# {item}\n\n")
                        file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {item}\n"""\n\n')

                    # 在README中添加文件链接
                    item_clean = item.replace(" ", "_").replace("/", "_").replace("-", "_")
                    parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
                    key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
                    readme_file.write(f"- [{item}](./{parent_clean}/{key_clean}/{item_clean}.md)\n")
        else:
            # 创建文件并写入初始内容
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".py"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")
            
            
            file_name = key.replace(" ", "_").replace("/", "_").replace("-", "_") + ".md"
            file_path = os.path.join(current_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {key}\n\n")
                file.write(f'"""\nLecture: {parent_path}/{key}\nContent: {key}\n"""\n\n')

            # 在README中添加文件链接
            parent_clean = parent_path.replace(" ", "_").replace("/", "_").replace("-", "_")
            key_clean = key.replace(" ", "_").replace("/", "_").replace("-", "_")
            readme_file.write(f"- [{key}](./{parent_clean}/{key_clean}/{file_name})\n")

        # 添加空行以分隔不同的章节
        readme_file.write("\n")

def main():
    root_dir = './'
    # 创建根目录
    os.makedirs(root_dir, exist_ok=True)

    # 创建 README.md 文件
    with open(os.path.join(root_dir, "README.md"), 'w', encoding='utf-8') as readme_file:
        readme_file.write("# 具体数学\n\n")
        readme_file.write("这是一个关于具体数学的目录结构。\n\n")
        create_directories_and_files(root_dir, structure, readme_file)

    print("目录和文件结构已生成，并创建 README.md 文件。")

if __name__ == "__main__":
    main()