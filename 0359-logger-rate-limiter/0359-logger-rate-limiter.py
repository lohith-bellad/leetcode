class Logger:
    """
    def __init__(self):
        self.msg_table = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_table:
            self.msg_table[message] = timestamp
            return True
        else:
            last_time = self.msg_table[message]
            if timestamp - last_time >= 10:
                self.msg_table[message] = timestamp
                return True
            else:
                return False
    """
    def __init__(self):
        self.log_count_table = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        should_print = True

        if message in self.log_count_table:
            latest_print = self.log_count_table[message]
            if timestamp - latest_print < 10:
                should_print = False
            else:
                self.log_count_table[message] = timestamp
        else:
            self.log_count_table[message] = timestamp
        return should_print

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)