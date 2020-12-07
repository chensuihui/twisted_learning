# coding:UTF-8
import twisted
import twisted.internet.defer
import twisted.internet.reactor
import time


class DeferHandle:  # 设置一个回调处理类
    def __init__(self):
        self.defer = twisted.internet.defer.Deferred()  # 获取Defer对象

    def get_defer(self):  # 让外部获得实例
        return self.defer

    def work(self):  # 模拟网络下载
        print("模拟网络下载延迟操作，等待3秒的时间...")
        time.sleep(3)  # 延迟3秒执行
        self.defer.callback("finish")  # 执行回调

    def handle_success(self, result):
        print("处理完成，进行参数接收：%s" % result)  # 处理完毕后的信息输出

    def handle_error(self, exp):  # 错误回调
        print("程序出错：%s" % exp)


def main():
    defer_client = DeferHandle()
    twisted.internet.reactor.callWhenRunning(defer_client.work)  # 执行耗时操作
    defer_client.get_defer().addCallback(defer_client.handle_success)  # 执行完毕后回调
    defer_client.get_defer().addCallback(defer_client.handle_error)  # 错误输出的回调
    twisted.internet.reactor.callLater(5, stop)  # 5秒后停止Reactor调用
    twisted.internet.reactor.run()  # 启用事件轮询


def stop():
    twisted.internet.reactor.stop()
    print("服务调用结束")


if __name__ == '__main__':
    main()
