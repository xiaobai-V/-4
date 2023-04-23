import PCF8591 as ADC
import time


class HysteresisComparator:
    def __init__(self, low_threshold, high_threshold):
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold
        self.state = False

    def compare(self, voltage):
        if voltage > self.high_threshold:
            self.state = True
        elif voltage < self.low_threshold:
            self.state = False
        return self.state


def loop():
    while True:
        for i in range(3):
            temp = ADC.read(i)  # 读取AIN0的数值
            print(f"AIN{i}:{temp}")
            # ADC.write(temp)  # 控制AOUT输出
            time.sleep(1)


# 异常处理函数
def destroy():
    ADC.write(0)  # AOUT输出为0


# 程序入口
if __name__ == "__main__":
    try:
        ADC.setup(0x48)  # PCF8591模块地址设置
        loop()           # 调用无限循环
    except KeyboardInterrupt:
        destroy()  # 释放AOUT端口
