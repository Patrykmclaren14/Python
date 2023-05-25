from random import randint


def learning(tab1, tab2):
    amount_good_answer = 0
    wrong_answer = []
    x = 0
    z = len(tab1)
    while x < z:
        y = randint(0, len(tab1)-1)
        x += 1
        print(tab1[y])
        a = input('Enter correct word:')
        if a == tab2[y].lower():
            amount_good_answer += 1
            print('correct')
            tab1.remove(tab1[y])
            tab2.remove(tab2[y])
        else:
            print('incorrectly')
            wrong_answer.append(tab1[y]+' = ' + tab2[y])
            tab1.remove(tab1[y])
            tab2.remove(tab2[y])
    print(str((amount_good_answer/z)*100) + '%')
    print('--------------------------')
    for answer in wrong_answer:
        print(answer)


tab2 = ['death penalty', 'evidence', 'jail', 'give a verdict', 'in the dock', 'keep in custody', 'life sentence', 'testify', 'unemployed', 'freedom of speech', 'live below the breadline', 'redistribution of wealth', 'sheltered accommodation', 'financial markets', 'come out of recession', 'inflation', 'interest rates', 'long-term investment', 'outlook', 'plummet', 'prosperity',
        'shares', 'the stock market', 'crash', 'currency', 'downturn', 'drop in value', 'exchange rate', 'at an alarming rate', 'be under the impression', 'browse through books', 'burning issue', 'come up with an idea', 'deterrent', 'have no clue', 'in the long term', 'instil values in', 'pursue a career', 'stick to (traditions)', 'tap into someone\'s need', 'would-be pop star']


tab1 = ['kara śmierci', 'dowody', 'więzienie', 'wydać wyrok', 'na ławie oskarżonych', 'przetrzymywanie w areszcie śledczym', 'dożywotnie więzienie', 'zeznawać', 'bez pracy', 'wolność słowa', 'żyć poniżej granicy ubóstwa', 'redystrybucja bogactwa', 'mieszkania chronione dla osób starszych', 'rynki finansowe', 'wyjść z recesji', 'inflacja', 'stopy procentowe', 'inwestycja długoterminowa', 'perspektywy, widoki', 'gwałtownie spadać',
        'dobrobyt', 'akcje', 'giełda papierów wartościowych', 'krach', 'waluta', 'spadek, tendencja zniżkowa', 'tracić na wartości', 'kurs wymiany', 'w zastraszającym tempie', 'odnieść wrażenie', 'przeglądać książki', 'palący problem', 'wpaść na pomysł', 'środek odstraszający', 'nie mieć pojęcia', 'na dłuższą metę', 'wpajać wartości (komuś)', 'rozpocząć karierę', 'przestrzegać (tradycji)', 'wykorzystać czyjąś potrzebę', 'aspirująca gwiazda popu']


learning(tab1, tab2)
