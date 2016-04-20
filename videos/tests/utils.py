from django.test import TestCase
from videos.utils import random_url_populate, youtube_video_exists


class UtilsTestCase(TestCase):

    CORRECT_VIDEOS = [
        'https://www.youtube.com/watch?v=jdiAraeA_8k&t=638s',
        'https://www.youtube.com/watch?v=-iSxls2f0Qo',
        'http://www.youtube.com/watch?v=-iSxls2f0Qo',
        'www.youtube.com/watch?v=-iSxls2f0Qo',
        'www.youtube.com/watch?v=-iSxls2f0Qo'
    ]

    INCORRECT_VIDEOS = [
        'https://www.youtube.com/watch?v=dsguhdiufgh_',
        'https://www.google.com/',
        'sdjfnksjafnbubiubsadf'
    ]

    def test_random_url_populate(self):
        random_str = random_url_populate()
        self.assertTrue(random_str.__len__() == 7)
        self.assertTrue(random_str.isalnum())

    def test_youtube_video_exists(self):
        for v in self.CORRECT_VIDEOS:
            self.assertTrue(youtube_video_exists(v))
        for v in self.INCORRECT_VIDEOS:
            self.assertFalse(youtube_video_exists(v))




