import re

from utils.generate_random_data import create_random_number, create_random_letters, \
    create_random_mobile_phone, create_random_datetime


def function_dollar(field, variable_list):
    """
    替换${变量名}的方法
    :param field: 第一个参数是yaml文件里面定义的字段
    :param variable_list: 第二个参数是变量列表
    :return:
    """

    if "${" in field:
        for key, value in variable_list:
            field = field.replace("${" + key + "}", value)
            # replace(old, new)把字符串中的旧字符串替换成正则表达式提取的值
    else:
        pass

    return field
    # 返回替换后的字段


def function_rn(field):
    """
    替换RN随机数字的方法
    :param field: 参数为yaml文件里面定义的字段
    :return:
    """

    if "{__RN" in field:
        digit_list = re.findall("{__RN(.+?)}", field)
        # 获取位数列表
        for i in digit_list:
            random_number = create_random_number(int(i))
            # 调用生成随机数字的方法
            field = field.replace("{__RN" + i + "}", random_number)
    else:
        pass

    return field
    # 返回替换后的字段


def function_rl(field):
    """
    替换RL随机字母的方法
    :param field: 参数为yaml文件里面定义的字段
    :return:
    """

    if "{__RL" in field:
        digit_list = re.findall("{__RL(.+?)}", field)
        # 获取位数列表
        for i in digit_list:
            random_letters = create_random_letters(int(i))
            # 调用生成随机数字的方法
            field = field.replace("{__RL" + i + "}", random_letters)
    else:
        pass

    return field
    # 返回替换后的字段


def function_mp(field):
    """
    替换MP随机手机号码的方法
    :param field: 参数为yaml文件里面定义的字段
    :return:
    """

    if "{__MP" in field:
        random_mobile_phone = create_random_mobile_phone()
        # 调用生成随机手机号码的方法
        field = field.replace("{__MP}", random_mobile_phone)
    else:
        pass

    return field
    # 返回替换后的字段


def function_rd(field):
    """
    替换RD随机日期时间的方法
    :param field: 参数为yaml文件里面定义的字段
    :return:
    """

    if "{__RD" in field:
        digit_list = re.findall("{__RD(.+?)}", field)
        # 获取年份列表
        for i in digit_list:
            i_split = i.split(",")
            random_datetime = create_random_datetime(i_split[0], i_split[1])
            # 调用生成随机日期时间的方法
            field = field.replace("{__RD" + i + "}", random_datetime)
    else:
        pass
    # 返回替换后的字段
    return field
