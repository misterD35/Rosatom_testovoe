# version 1: собственный алгоритм

def version_comparison(version_a: str, version_b: str) -> int:
    splited_version_a, splited_version_b = version_a.split('.'), version_b.split('.')
    for num in range(len(min(splited_version_a, splited_version_b))):
        if splited_version_a[num] == splited_version_b[num]:
            continue
        elif splited_version_a[num] < splited_version_b[num]:
            return -1
        else:
            return 1
    return 0 if len(splited_version_a) == len(splited_version_b) \
        else 1 if max(splited_version_a, splited_version_b) == splited_version_a \
        else -1


# version 2:собственный алгоритм

def version_comparison_v1(version_a: str, version_b: str) -> int:
    version_a = version_a.strip(".")
    version_b = version_b.strip(".")
    splited_version_a, splited_version_b = version_a.split('.'), version_b.split('.')
    min_length = len(splited_version_a) if len(splited_version_a) <= len(splited_version_b) else len(splited_version_b)
    for left_num, right_num in zip(splited_version_a[:min_length], splited_version_b[:min_length]):
        if left_num == right_num:
            continue
        elif left_num < right_num:
            return -1
        else:
            return 1
    return 0 if len(splited_version_a) == len(splited_version_b) \
        else -1 if len(splited_version_a) < len(splited_version_b) \
        else 1


# version 3: решение со сторонней утилитой

from packaging import version


def compare_versions(version_a: str, version_b: str) -> int:
    if version.parse(version_a) < version.parse(version_b):
        return -1
    elif version.parse(version_a) == version.parse(version_b):
        return 0
    else:
        return 1


if __name__ == "__main__":
    print('version 1')
    print(version_comparison('1.10', '1.1'))

    print('\n', 'version 2')
    print(version_comparison_v1('1.10.5', '1.10.5.'))

    print('\n', 'version 3')
    print(compare_versions("2.3.1.1", "2.3.10"))
