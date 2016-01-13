def BalanceParenthesis(s):
    Open = '{[('
    Close = '}])'
    new = []
    for i in range(0, len(s)):
        if s[i] in Open:
            new.append(s[i])
        else:
            if new == []:
                return False
            else:
                z = new.pop()
                if z != Open[(Close.index(s[i]))]:
                    return False
    if new == []:
        return True
    else:
        return False

print(BalanceParenthesis('{{}}[(){}]'))
            
