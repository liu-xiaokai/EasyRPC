from EasyRPC.server import rpcserver
import inspect


def get_functions():
    functions = []
    module = inspect.getmodule(inspect.currentframe())
    members = inspect.getmembers(module)
    for name, obj in members:
        if inspect.isfunction(obj):
            if name != 'get_functions':
                functions.append(obj)
    return functions


def test(*args, **kwargs):
    print("服务器端注册的 test 被调用了")
    print("test: args = {}, kwargs = {}".format(args, kwargs))
    return 'the test function has been called'


def test1(*args, **kwargs):
    aa = 11
    return aa


if __name__ == '__main__':
    s = rpcserver.RPCServer()
    for func in get_functions():
        s.register_function(func)       # 注册函数
    s.loop('127.0.0.1', 5000)       # 要监听的 IP 和端口



