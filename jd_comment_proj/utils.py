
def num2code(num):
    """转换京东页面的数字与code"""

    # 大于 1000 不处理
    if num >= 1000:
        return

    pre_code = "jdSearchResultBkCb"
    alphas = 'IZABCDEFGHI'
    code_dict = {digit: alp for alp, digit in zip(alphas, list(range(11)))}

    if num < 10:
        code = code_dict[num]
    elif num == 10:
        code = 'I'
    elif num < 100:
        right_digit = num % 10
        left_digit = int(num / 10) % 10

        right_char = code_dict[right_digit]

        if right_digit == 0:
            left_char = code_dict[left_digit]
        else:
            left_char = code_dict[left_digit + 1]

        code = left_char + right_char
    elif num == 100:
        code = 'II'
    else:
        # 根据 index 来取
        alphas = 'ZABCDEFGHI'
        idx_2_dict = {digit: alp for alp, digit in zip(alphas, list(range(0, 10)))}
        alphas = 'ZABCDEFGHI'
        idx_1_dict = {digit: alp for alp, digit in zip(alphas, list(range(11)))}
        alphas = 'IZABCDEFGHI'
        idx_0_dict = {digit: alp for alp, digit in zip(alphas, list(range(11)))}

        # 取位置
        code = ''
        for idx, ch in enumerate(reversed(str(num))):
            digit = int(ch)
            if idx == 0:
                char = idx_0_dict[digit]
            elif idx == 1:
                char = idx_1_dict[digit]
            else:
                char = idx_2_dict[digit]
            code = code + char
        code = code[::-1]

    return pre_code + code


def comment_num2code(num):
    """comment 页面参数的 callback_code"""
    pre_code = 'skuJDEval'
    alphas = 'ZABCDEFGHI'
    num_dict = {num: alp for alp, num in zip(alphas, list(range(10)))}
    # {0: 'Z', 1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I'}
    code = ''
    for ch in str(num):
        digit = int(ch)
        char = num_dict[digit]
        code = code + char

    return pre_code + code
