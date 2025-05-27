def get_num_words(content):
    lst = content.split()
    return len(lst)


def get_word_freq(content):
    dict = {}

    for i in content:
        if i.lower() not in dict:
            dict[i.lower()] = 1
        else:
            dict[i.lower()] += 1

    return dict

def sort_dict(dicts):
    return dict(sorted(dicts.items(), key=lambda item: item[1], reverse=True))

    