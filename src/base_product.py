from abc import ABC, abstractmethod


class BaseProduct(ABC):
	""" Базовый классметод создание нового объекта класса """

	@classmethod
	@abstractmethod
	def new_product(cls, *args, **kwargs):
		pass

