def check_then(f):
    def wrapper(result):
        if result[0] == "ok":
            return f(result[1])
        else:
            return result

    return wrapper


def convert_to_int(value: str):
    try:
        result = int(value)
    except:
        return ("error", "convert error")
    return ("ok", result)


def gen_range_checker(minimun: int, maximun: int):
    def check_range(value):
        if minimun > value:
            return ("error", f"value({value}) out of range")
        if maximun < value:
            return ("error", f"value({value}) out of range")
        return ("ok", value)

    return check_range


if __name__ == "__main__":
    field = ""
    check_range = gen_range_checker(18, 150)
    cnvt_to_int = check_then(convert_to_int)
    chk_range = check_then(check_range)

    int_value = cnvt_to_int(("ok", field))
    result = chk_range(int_value)

    print(result)

    field = "17"
    int_value = cnvt_to_int(("ok", field))
    result = chk_range(int_value)

    print(result)

    field = "151"
    int_value = cnvt_to_int(("ok", field))
    result = chk_range(int_value)

    print(result)

    field = "18"
    int_value = cnvt_to_int(("ok", field))
    result = chk_range(int_value)

    print(result)

    field = "150"
    int_value = cnvt_to_int(("ok", field))
    result = chk_range(int_value)

    print(result)
