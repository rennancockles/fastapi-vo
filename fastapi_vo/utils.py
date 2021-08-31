from typing import Type, Sequence, Union
from pydantic import BaseModel


def Omit(model: Type[BaseModel],
         fields: Union[str, Sequence[str]],
         *,
         classname: str = None) -> Type[BaseModel]:
    def _format_fields(fields):
        if isinstance(fields, str):
            return set((fields,))
        else:
            return set(fields)

    fields = _format_fields(fields)

    classname = classname or model.__name__
    bases = model.__bases__

    model_fields = model.__fields__.copy()
    for field_name in filter(lambda f: f in model_fields, fields):
        model_fields.pop(field_name)

    dict_ = {
        '__fields__': model_fields,
    }

    return type(classname, bases, dict_)


def Pick(model: Type[BaseModel],
         fields: Union[str, Sequence[str]],
         *,
         classname: str = None) -> Type[BaseModel]:
    def _format_fields(fields):
        if isinstance(fields, str):
            return set((fields,))
        else:
            return set(fields)

    fields = _format_fields(fields)

    classname = classname or model.__name__
    bases = model.__bases__

    model_fields = {}
    for field_name in filter(lambda f: f in model.__fields__, fields):
        model_fields[field_name] = model.__fields__[field_name]

    dict_ = {
        '__fields__': model_fields,
    }

    return type(classname, bases, dict_)
