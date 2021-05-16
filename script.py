def decorator_counter(func):
    
    def wrapper(*args):
      wrapper.c +=1
      return func(*args)
    wrapper.c = 0
    return wrapper


@decorator_counter
def original_func(*arg):
  print(*arg)
    
original_func()
original_func()


# def counter(fu):
    
#     def inner(*a,**kw):
#         inner.count+=1
#         return fu(*a,**kw)
#     inner.count = 0
#     return inner

original_func("avc", "bbb")

print(original_func.c)