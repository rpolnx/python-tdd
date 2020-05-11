def returnAnagram(word):
    if len(word) == 1:
        return [word]

    all_letters_from_initial_word = list(word)
    result = set()

    for index, base_letter in enumerate(all_letters_from_initial_word):
        word_without_initial_letter = remove_letter_by_index_from_word(index, all_letters_from_initial_word)
        for walking_index_from_non_base_letter, walking_letter in enumerate(word_without_initial_letter):
            result.add(
                buildWord(word_without_initial_letter, base_letter, walking_letter, walking_index_from_non_base_letter))

    return result


def buildWord(word_without_initial_letter, base_letter, walking_letter, index2):
    return base_letter + walking_letter + convert_vector_to_string(
        remove_letter_by_index_from_word(index2, word_without_initial_letter))


def convert_vector_to_string(vector):
    return ''.join(vector)


def remove_letter_by_index_from_word(index, letters):
    return letters[0:index] + letters[index + 1:len(letters)]
