import numbers


def ensure(name,validate,doc=None):
    def decorator(Class):
        privateName="__"+name
        def getter(self):
            return getattr(self,privateName)
        def setter(self,value):
            validate(name,value)
            setattr(self,privateName,value)
        setattr(Class,name,property(getter,setter,doc=doc))
        return Class
    return decorator


def is_in_range(minimum=None,maximum=None):
    assert minimum is not None or maximum is not None
    def is_in_range(name,value):
        if not isinstance(value,numbers.Number):
            raise ValueError("{} must be a number".format(name))
        if minimum is not None and value<minimum:
            raise ValueError("{} {} is too small".format(name,value))
        if maximum is not None and value>maximum:
            raise ValueError("{} {} is too big".format(name,value))
    return is_in_range

def is_not_empty_str(name,value):
    if not isinstance(value,str):
        raise ValueError("{} must be of type str".format(name))
    if not bool(value):
        raise ValueError("{} may not be empty".format(name))


