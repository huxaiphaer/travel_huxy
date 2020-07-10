import ast


def filter_args_and_json_custom_creator(val):
    output = []
    for i in val:
        f = str(i).replace("\'", "\"")
        formatted = ast.literal_eval(f)
        output.append(formatted)
    return output
