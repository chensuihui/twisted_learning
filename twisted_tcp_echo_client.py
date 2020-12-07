# coding:UTF-8
import twisted
import twisted.internet.protocol
import twisted.internet.reactor

SERVER_HOST = "localhost"  # 服务主机
SERVER_PORT = 8080  # 连接端口号


class Client(twisted.internet.protocol.Protocol):
    def connectionMade(self):  # 客户端连接的时候触发
        print("服务器连接成功，可以进行数据交互，如果要结束通讯，则直接回车。")
        self.send()  # 建立连接后进行数据的发送

    def dataReceived(self, data):  # 接收服务端数据
        print(data.decode("UTF-8"))  # 输出接收到的数据
        self.send()  # 继续发送

    def send(self):  # 数据发送，自定义的方法
        input_data = input("请输入要发送的数据：")
        if input_data:
            self.transport.write(input_data.encode("UTF-8"))  # 回应
        else:  # 没有输入内容表示操作结束
            self.transport.loseConnection()  # 关闭连接


class DefaultClientFactory(twisted.internet.protocol.ClientFactory):  # 客户端工厂
    protocol = Client  # 定义回调
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: \
        twisted.internet.reactor.stop()


def main():  # 主函数
    twisted.internet.reactor.connectTCP(SERVER_HOST, SERVER_PORT, DefaultClientFactory())  # 服务监听
    twisted.internet.reactor.run()  # 程序运行


if __name__ == "__main__":  # 判断程序执行名称
    main()  # 调用主函数
