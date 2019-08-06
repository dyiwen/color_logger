#! encoding:utf-8

import logging
from colorlog import ColoredFormatter
from logging.handlers import RotatingFileHandler


class Log(object):
	"""docstring for Log"""
	def __init__(self, file_path, logger_name=__name__, mode = 'a'):
		self.mode = mode
		self.file_path = file_path
		self.logger = logging.getLogger(logger_name)
		self.logger.setLevel('DEBUG')
		# self.formatter = logging.Formatter('%(asctime)s 进程:%(process)d [line:%(lineno)d] %(levelname)s %(message)s')
		# self.colorlog.basicConfig(format = '%(asctime)s 进程:%(process)d [line:%(lineno)d] %(levelname)s %(message)s',
		# 	datefmt='%a, %d %b %Y %H:%M:%S',)
		self.formatter = ColoredFormatter('%(log_color)s%(asctime)s 进程:%(process)d [line:%(lineno)d] %(levelname)s %(message)s',
			datefmt = None,
			reset = True,
			log_colors = {
				'DEBUG':'cyan',
				'INFO':'green',
				'WARNING':'yellow',
				'ERROR':'red',
				'CRITICAL':'red,bg_white'
			},
			secondary_log_colors={},
			)


	def file_info_handle(self):
		file_rt_info_handler = RotatingFileHandler(filename=self.file_path, 
			mode='a', 
			maxBytes=30 * 1024 * 1024, 
			backupCount=1)
		# 设置日志文件记录等级
		file_rt_info_handler.setLevel(level=logging.INFO)
		file_rt_info_handler.setFormatter(self.formatter)
		return file_rt_info_handler

	def file_error_handle(self):
		file_rt_error_handler = RotatingFileHandler(filename=self.file_path + '.error', 
			mode='a',
			maxBytes=30 * 1024 * 1024,
			backupCount=1)
		# 设置日志文件记录等级
		file_rt_error_handler.setLevel(level=logging.ERROR)
		file_rt_error_handler.setFormatter(self.formatter)
		return file_rt_error_handler


	def stream_handler(self):
		chlr = logging.StreamHandler()
		chlr.setLevel('INFO')
		chlr.setFormatter(self.formatter)
		return chlr

	def main(self):
		self.logger.addHandler(self.file_info_handle())
		self.logger.addHandler(self.file_error_handle())
		self.logger.addHandler(self.stream_handler())
		return self.logger


def out(s):
        log_.info(s)

def err(s):
        log_.error(s)

def warn(s):
        log_.warning(s)

def debug(s):
        log_.debug(s)

log_ = Log('log/new.log').main()



if __name__ == '__main__':
	log_ = Log('log/watch.log')
	log_ = log_.main()
	# log_.error('Hello,this is error message!!!!')
	log_.info('1111111111111111')
	# log_.log(3,'111111111111111')
