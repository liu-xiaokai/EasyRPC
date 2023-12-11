from EasyRPC.client import rpcclient


def get_client(host):
    client = rpcclient.RPCClient()
    client.connect(host, 5000)  # 连接 Server
    return client


def test(host):
    client = get_client(host)
    res = client.test("测试项", kw1="1")
    return res


def test1(host):
    client = get_client(host)
    res = client.test1("测试项2", kw1="1")
    return res


if __name__ == '__main__':

    res = test('127.0.0.1')     # 调用 Server 端的函数
    res1 = test1('127.0.0.1')     # 调用 Server 端的函数
    print("远程调用的返回值 res = {}".format(res))
    print("远程调用的返回值 res1 = {}".format(res1))