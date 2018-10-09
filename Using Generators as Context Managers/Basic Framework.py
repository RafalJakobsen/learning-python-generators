# Context Manager

@contextmanager
def simple_cm(n):
    try:
        #setup code
        yield
    finally:
        # wrap up code