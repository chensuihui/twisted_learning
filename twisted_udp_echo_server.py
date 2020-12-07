# coding:UTF-8
import twisted
import twisted.internet.protocol
import twisted.internet.reactor

SERVER_PORT = 8080  # 设置监听端口


class EchoServer(twisted.internet.protocol.DatagramProtocol):  # 数据报协议
    def datagramReceived(self, datagram, addr):  # 接收数据处理
        print("【服务端】接收到消息，消息来源IP：%s、来源端口：%s" % addr)
        print("【服务端】接收到数据消息：%s" % datagram.decode("UTF-8"))
        echo_data = "【ECHO】%s" % datagram.decode("UTF-8")  # 设置回应信息
        self.transport.write(echo_data.encode("UTF-8"), addr)  # 将信息返回给指定客户端


def main():  # 主函数
    twisted.internet.reactor.listenUDP(SERVER_PORT, EchoServer())
    print("服务器启动完毕，等待客户端连接......")
    twisted.internet.reactor.run()  # 事件轮询


if __name__ == "__main__":  # 判断程序执行名称
    main()  # 调用主函数
