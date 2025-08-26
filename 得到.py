import re
import itertools


def generate_truth_table(_str1):
    # output为输出变量
    # 表达式输入
    expr = _str1

    # 检查非法字符
    if not re.match(r'^[\w\s∧∨¬()]+$', expr):
        print("错误：表达式中包含非法字符！")
        return

    # 替换逻辑符号为Python运算符
    expr = re.sub(r'¬', 'not ', expr)
    expr = re.sub(r'\s*∧\s*', ' and ', expr)
    expr = re.sub(r'\s*∨\s*', ' or ', expr)
    expr = re.sub(r'\s+', ' ', expr).strip()  # 合并多余空格

    try:
        # 提取变量（排除逻辑运算符）
        variables = re.findall(r'\b[a-zA-Z_]\w*\b', expr) # 正则表达式提取变量
        variables = [var for var in variables if var not in {'and', 'or', 'not'}]
        variables = sorted(list(set(variables)))

        if not variables:
            print("错误：未找到有效变量！")
            return

        # 生成真值组合
        truth_table = []
        for values in itertools.product([False, True], repeat=len(variables)):
            env = dict(zip(variables, values))

            # 计算表达式结果
            try:
                result = eval(expr, {}, env)
            except:
                output = "错误：无效的逻辑表达式！"
                return output


            truth_table.append((*values, result))

        # 打印真值表
        header = variables + ['结果']
        output = ("        \n真值表：\n" + "        | " +" | ".join(header) +
                  " |" +"\n"+ "        |" + "|".join(["---" for _ in header]) + "|"+"\n")

        for row in truth_table:
            bool_str = ["T" if val else "F" for val in row]
            output += "        | " + " | ".join(bool_str) + " |" + "\n"

    except Exception as e:
        output = f"发生错误：{str(e)}"
    return output

if __name__ == "__main__":
    stt =input("")
    print(generate_truth_table(stt))