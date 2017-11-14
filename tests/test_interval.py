from test_base import TestBase
__pragma__('alias', 'S', '$')

# I really need to make func() take a long time so I can ensure interval instead of sleep
    
class TestInterval(TestBase):
    NEEDED_TIME = 1000

    def begin(self):
        self.counter = 0
        self.start_time = __new__(Date())
        def func():
            self.counter += 1
        self.div.timers().IntervalTimer({
            'millis': 400,
        }).do(func)
        
    def end(self):
        self.assertTrue(self.counter == 2)
        
S.fn.timers.TESTS.append(TestInterval)
    
    

class TestIntervalAfter(TestBase):
    NEEDED_TIME = 1000

    def begin(self):
        self.counter = 0
        self.start_time = __new__(Date())
        def func():
            self.counter += 1
        self.div.timers().IntervalAfterTimer({
            'millis': 400,
        }).do(func)
        
    def end(self):
        self.assertTrue(self.counter == 3)
        
S.fn.timers.TESTS.append(TestIntervalAfter)
    
    

class TestMillisShortcut(TestBase):
    NEEDED_TIME = 1000

    def begin(self):
        self.counter = 0
        self.start_time = __new__(Date())
        def func():
            self.counter += 1
        self.div.timers().IntervalTimer(400).do(func)
        
    def end(self):
        self.assertTrue(self.counter == 2)
        
S.fn.timers.TESTS.append(TestMillisShortcut)
    
    
    
    