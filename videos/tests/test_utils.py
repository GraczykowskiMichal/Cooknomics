from django.test import TestCase
from videos.utils import youtube_video_exists


class UtilsTestCase(TestCase):

    CORRECT_VIDEOS = [
        'jdiAraeA_8k&t=638s',
        '-iSxls2f0Qo',
        '-iSxls2f0Qo',
    ]

    INCORRECT_VIDEOS = [
        'https://www.youtube.com/watch?v=dsguhdiufgh_',
        'https://www.google.com/',
        'sdjfnksjafnbubiubsadf'
    ]

    def test_youtube_video_exists(self):
        for v in self.CORRECT_VIDEOS:
            self.assertTrue(youtube_video_exists(v))
        for v in self.INCORRECT_VIDEOS:
            self.assertFalse(youtube_video_exists(v))



