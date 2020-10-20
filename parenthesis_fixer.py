"""
Given a string of parentheses such as “(()())((()” write a function that adds parentheses to the beginning and end to make all parentheses match. This function should return the corrected string.
Example input: “)(()(”
Output: “()(()())”
We added “(” to the beginning and “))” to the end
"""


class ParenthesisFixer:

    @classmethod
    def fix(cls, par_str: str):
        open_count = 0
        close_count = 0
        required_pref = 0

        for char in par_str:
            if char == '(':
                open_count += 1
            else:
                close_count += 1
            if close_count > open_count:
                required_pref += 1
                open_count += 1

        required_pref_list = ['('] * required_pref
        required_pref_str = ''.join(required_pref_list)

        required_post = open_count - close_count
        required_post_list = [')'] * required_post
        required_post_str = ''.join(required_post_list)

        return f'{required_pref_str}{par_str}{required_post_str}'


def main():
    input_1 = ")(()("
    expected_res_1 = "()(()())"
    real_res = ParenthesisFixer.fix(input_1)
    assert expected_res_1 == real_res, f'{real_res=}, {expected_res_1=}'

    input_2 = ")))"
    expected_res_2 = "((()))"
    real_res_2 = ParenthesisFixer.fix(input_2)
    assert expected_res_2 == real_res_2, f'{real_res_2=}, {expected_res_2=}'

    input_3 = "((("
    expected_res_3 = "((()))"
    real_res_3 = ParenthesisFixer.fix(input_3)
    assert expected_res_3 == real_res_3, f'{real_res_3=}, {expected_res_3=}'


if __name__ == '__main__':
    main()
