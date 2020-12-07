# coding:UTF-8
import twisted
import twisted.internet.defer
import twisted.internet.protocol
import twisted.internet.reactor
import twisted.internet.threads
import time

SERVER_HOST = "localhost"  # 服务主机
SERVER_PORT = 8080  # 连接端口号


class DeferClient(twisted.internet.protocol.Protocol):
    def connectionMade(self):
        print("服务器连接成功，可以进行数据交互，如果要结束通讯，则直接回车。")
        self.send()  # 建立连接后进行数据的发送

    def dataReceived(self, data):  # 接收服务端数据
        content = data.decode("UTF-8")
        twisted.internet.threads.deferToThread(self.handle_request, content).addCallback(self.handle_success)

    def handle_request(self, content):  # 数据处理过程
        print("【客户端】对服务器端的接收（%s）进行处理，此处会产生1秒延迟" % content)  # 处理完毕后的信息输出
        time.sleep(1)
        return content

    def handle_success(self, result):  # 操作处理完毕
        print("处理完成，进行参数接收：%s" % result)  # 处理完毕后的信息输出
        self.send()

    def send(self):  # 数据发送，自定义的方法
        input_data = input("请输入要发送的数据：")
        if input_data:
            self.transport.write(input_data.encode("UTF-8"))  # 回应
        else:  # 没有输入内容表示操作结束
            self.transport.loseConnection()  # 关闭连接


class DefaultClientFactory(twisted.internet.protocol.ClientFactory):  # 客户端工厂
    protocol = DeferClient
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: \
        twisted.internet.reactor.stop()


def main():  # 主函数
    twisted.internet.reactor.connectTCP(SERVER_HOST, SERVER_PORT, DefaultClientFactory())  # 服务监听
    twisted.internet.reactor.run()  # 程序运行


if __name__ == "__main__":  # 判断程序执行名称
    main()  # 调用主函数
