# import nltk
# nltk.download('averaged_perceptron_tagger')


from nltk import word_tokenize, pos_tag
import pdftotext

with open("/users/rishavraj/desktop/lease.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
    # for page in pdf:
    #     print(page)
    combined_page = []
    for i in range(len(pdf)):
        combined_page = combined_page + pdf[i].split()
    combined_page = ' '.join(combined_page)
    verb_list = []
    noun_list = []
    for word in pos_tag(word_tokenize(combined_page)):
        if word[1] in {'NN', 'NNP', 'NNS'} and word not in noun_list:
            noun_list.append(word)
        elif word[1] in {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'} and word not in verb_list:#, 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}:
            verb_list.append(word)
    for word in noun_list:
        print(word)
    print('No. of verbs = ', len(verb_list))
    print('No. of nouns = ', len(noun_list))





# with open('/users/rishavraj/desktop/term.txt', 'r', errors='replace') as f:
#     read_file = f.read()
#     for line in read_file.splitlines():


# for line in read_file.splitlines():
#     print(line)
#     print('\nbreak\n')
# print(read_file)

# for line in read_file.splitlines():
#     print(pos_tag(word_tokenize(line)))
#     print('break')