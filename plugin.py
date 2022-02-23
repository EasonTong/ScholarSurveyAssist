def summar_except_title(title):
    title = title.lower()
    except_letter = [
        'code',
        'medic',
        'patient',
        'video',
        'opinion',
        'review',
        'statistic',
        'discharge',
        'scientific',
        'legal',
        'tweet',
        'blog',
        'multi-document',
        'citation',
        'arabic',
        'malayalam',
        'czech',
        'remote',
        'sensor',
        'stream',
        'persian',
        'bengali',
        'timeline',
        'bug',
        'report',
        'telugu',
        'policy',
        'dialogue',
        'health',
        'online',
        'forum',
        'meeting',
        'screen',
        'conversation',
        'answer',
        'clinic',
        'patent',
        'hospital',
        'interactive',
        'german',
        'disaster',
        'gene',
        'executive',
        'bangla',
        'urdu',
        'meteorologic',
        'scholar',
        'event',
        'motion',
        'device',
        'chinese',
        'sign',
        'vietnamese',
        'argument',
        'cross-lingual',
        'multilingual',
        'claim',
        'russian',
        'history',
        'korea',
        'product',
        'collaborative',
        'education',
        'speech',
        'sport',
        'slovak',
        'danish',
        'turkish',
        'disease',
        'movie',
        'kazakh',
        'figure',
        'hindi',
        'temporal',
        'music',
        'person',
        'spanish',
        'song',
        'spatio',
        'scatterplot',
        'albanian',
        'linguistic',
        'nurse',
        'spoken',
        'interpret',
        'konkani',
        'action',
        'photo',
        'album',
        'smell',
        'reddit',
        'academic',
        'publications',
        'lyric',
        'audio',
        'japanese',
        'cancer',
        'object',
        'trace',
        'flow',
        'portuguese',
        'private',
        'twitter',
        'ontology',
        'work',
        'indonesian',
        'spectrum',
        'kyutech',
        'tamil',
        'punjabi',
    ]
    except_word = ['data', 'rdf', 'lay']
    except_multi_words = []

    if any(map(lambda x: x in title, except_letter)):
        return True
    if any(map(lambda multi_words: not all(lambda x: x not in title, multi_words), except_multi_words,)):
        return True
    title = title.split(' ')
    
    if any(map(lambda x: x in title, except_word)):
        return True


def pre_train_except_title(title):
    title = title.lower()
    if 'pre-train' not in title:
        return True


def fine_tun_except_title(title):
    title = title.lower()
    if 'fine-tun' not in title:
        return True


def multi_modal_except_title(title):
    title = title.lower()
    if 'multi-modal' not in title:
        return True

def cross_modal_except_title(title):
    title = title.lower()
    if 'cross-modal' not in title:
        return True
