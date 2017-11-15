def calc_hypo(a, b):
    
    if (type(a) not in (int, float)) or (type(b) not in (int, float)):
        print 'Bad argument'
        return False

    if (not a > 0) or (not b > 0):
        print 'Bad argument'
        return False
        
    hypo = (a**2 + b**2)**0.5
    return hypo

print calc_hypo(3, 4)
print calc_hypo(3.0, 4.0)
print calc_hypo(93.24, 8)
print calc_hypo(3, 'b')
print calc_hypo('a', 4)
print calc_hypo(-5, 4)
print calc_hypo(0, 2)
