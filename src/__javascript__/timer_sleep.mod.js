	(function () {
		var BaseTimer = __init__ (__world__.timer_base).BaseTimer;
		var S = jQuery;
		var SleepTimer = __class__ ('SleepTimer', [BaseTimer], {
			get _startTimer () {return __get__ (this, function (self) {
				return window.setTimeout (self._notifyObservers, self.millis);
			});}
		});
		var SleepAfterTimer = __class__ ('SleepAfterTimer', [SleepTimer], {
			get start () {return __get__ (this, function (self) {
				if (self.run_index == 0) {
					return self._notifyObservers ();
				}
				return __super__ (SleepAfterTimer, 'start') (self);
			});}
		});
		__pragma__ ('<use>' +
			'timer_base' +
		'</use>')
		__pragma__ ('<all>')
			__all__.BaseTimer = BaseTimer;
			__all__.S = S;
			__all__.SleepAfterTimer = SleepAfterTimer;
			__all__.SleepTimer = SleepTimer;
		__pragma__ ('</all>')
	}) ();
