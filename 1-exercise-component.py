import os
from typing import NamedTuple
from kfp.components import create_component_from_func

@create_component_from_func
def print_and_return_number(number: int) -> int:
    print(number)
    return number

def print_and_return_number2(number: int) -> int:
    print(number)
    return number

def divide_and_return_number(
    number: int,
) -> NamedTuple("DivideOutputs", [("quotient", int), ("remainder", int)]):
    from collections import namedtuple

    quotient, remainder = divmod(number, 2)
    print("quotient is", quotient)
    print("remainder is", remainder)

    divide_outputs = namedtuple(
        "DivideOutputs",
        [
            "quotient",
            "remainder",
        ],
    )
    return divide_outputs(quotient, remainder)

if __name__ == "__main__":
    base_dir = './kf-yamls'
    path1 = os.path.join(base_dir, "1-print_and_return_number.yaml")
    path2 = os.path.join(base_dir, "1-print_and_return_number2.yaml")
    path3 = os.path.join(base_dir, "1-divide_and_return_number.yaml")
    
    print_and_return_number.component_spec.save(path1)
    print_and_return_number2 = create_component_from_func(func=print_and_return_number2, base_image='python:3.8.13')
    print_and_return_number2.component_spec.save(path2)
    divide_and_return_number = create_component_from_func(func=divide_and_return_number, base_image='python:3.8.13')
    divide_and_return_number.component_spec.save(path3)

    # How To Use in Kubeflow Pipeline
    # from kfp.components import load_component_from_file
    # print_and_return_number = load_component_from_file("print_and_return_number.yaml")