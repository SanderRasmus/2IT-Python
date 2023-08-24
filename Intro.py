def hei():
    navn = str(input('Hva heter du? '))
    print('Hei ' + navn)


def kuprat():
    melding = str(input('Hva skal kua si? '))
    boblelengde = len(melding) + 2

    print(' ' + '_' * boblelengde)
    print('<' + melding + '>')
    print(' ' + '-' * boblelengde)
    print('     \   ^__^')
    print('      \  (oo)\_______')
    print('         (__)\       )')
    print('             ||----W |')
    print('             ||     ||')

kuprat()