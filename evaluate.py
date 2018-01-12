from model.data_utils import CoNLLDataset
from model.ner_model import NERModel
from model.config import Config
import codecs

def align_data(data):
    """Given dict with lists, creates aligned strings

    Adapted from Assignment 3 of CS224N

    Args:
        data: (dict) data["x"] = ["I", "love", "you"]
              (dict) data["y"] = ["O", "O", "O"]

    Returns:
        data_aligned: (dict) data_align["x"] = "I love you"
                           data_align["y"] = "O O    O  "

    """
    spacings = [max([len(seq[i]) for seq in data.values()])
                for i in range(len(data[list(data.keys())[0]]))]
    data_aligned = dict()

    # for each entry, create aligned string
    for key, seq in data.items():
        str_aligned = ""
        for token, spacing in zip(seq, spacings):
            str_aligned += token + " " * (spacing - len(token) + 1)

        data_aligned[key] = str_aligned

    return data_aligned



def interactive_shell(model):
    """Creates interactive shell to play with model

    Args:
        model: instance of NERModel

    """
    wordsList = codecs.open("data/input.txt",encoding="UTF-8")
    sentence = wordsList.readline()
    words_raw = sentence.strip().split(" ")
    preds = model.predict(words_raw)
    with codecs.open("data/result.txt", "w",encoding="UTF-8") as f:
        for i, word in enumerate(words_raw):
            f.write(word + " : " + preds[i] + "\r\n")


def main():
    # create instance of config
    config = Config()

    # build model
    model = NERModel(config)
    model.build()
    model.restore_session(config.dir_model)
    interactive_shell(model)


if __name__ == "__main__":
    main()
