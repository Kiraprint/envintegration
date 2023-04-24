import unittest

from pes_digenv import TextEmotionApi


class TestApi(unittest.TestCase):
    def setUp(self) -> None:
        self.api = TextEmotionApi()

    def test_is_toxic(self):
        self.assertTrue(self.api.is_toxic('Ты дурак'))
        self.assertTrue(self.api.is_toxic('Ну и лошара'))
        self.assertTrue(self.api.is_toxic('От тебя воняет'))
        self.assertTrue(self.api.is_toxic('Вот ты собака ползаборная'))
        self.assertFalse(self.api.is_toxic('Люблю милых котиков'))
        self.assertFalse(self.api.is_toxic('Обратись к психотерапевту, это действительно может тебе помочь'))
        self.assertFalse(self.api.is_toxic('Работаем не покладая рук!'))

    def test_get_mat(self):
        self.assertFalse(self.api.get_mat('Ты дурак') == 0)
        self.assertTrue(self.api.get_mat('Ты мудила') == 1)
        self.assertTrue(self.api.get_mat('Хуйня из-под коня') == 1)
        self.assertFalse(self.api.get_mat('Ты такая милая') == 0)
        self.assertTrue(self.api.get_mat('хуегномы угрожают бомбардировкой') == 1)
        self.assertFalse(self.api.get_mat('Казахстан угрожает нам бомбардировкой') == 0)
        self.assertFalse(self.api.get_mat('Мудоёбище должно нас не заметить. Иначе мы попадём в просак') == 1)
        
    def test_emotion(self):
        self.assertTrue(self.api.emotion('Мне так плохо') == 'грусть')
        self.assertTrue(self.api.emotion('Завтра выходной!') == 'радость')
        self.assertTrue(self.api.emotion('Такая ясная погода!') == 'радость')
        self.assertTrue(self.api.emotion('Ты адекватный?!') == 'возмущение')
        self.assertTrue(self.api.emotion('Корабли лавировали-лавировали да не вылавировали') == 'безэмоциональное')
        self.assertTrue(self.api.emotion('Мне так хорошо!') =='радость')
        

if __name__ == "__main__":
    unittest.main()
