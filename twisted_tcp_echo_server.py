# coding:UTF-8
import twisted
import twisted.internet.protocol
import twisted.internet.reactor

SERVER_PORT = 8080  # 设置监听端口


class Server(twisted.internet.protocol.Protocol):  # 服务端一定要设置一个继承父类
    def connectionMade(self):  # 客户端连接的时候触发
        print("客户端地址：%s" % self.transport.getPeer().host)

    def dataReceived(self, data):  # 接收客户端数据
        print("【服务器】接收到数据：%s" % data.decode("UTF-8"))  # 输出接收到的数据
        self.transport.write(("【ECHO】%s" % data.decode("UTF-8")).encode("UTF-8"))  # 回应


class DefaultServerFactory(twisted.internet.protocol.Factory):  # 定义处理工厂类
    protocol = Server  # 注册回调操作


def main():  # 主函数
    twisted.internet.reactor.listenTCP(SERVER_PORT, DefaultServerFactory())  # 服务监听
    print("服务器启动完毕，等待客户端连接......")
    twisted.internet.reactor.run()  # 事件轮询


if __name__ == "__main__":  # 判断程序执行名称
    main()  # 调用主函数
