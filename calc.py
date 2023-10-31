def calculator(A: int, B: int, C: str) -> float:
    if C == "+":
        return float(A+B)
    elif C == "-":
        return float(A-B)    
    elif C == "*":
        return float(A*B)
    elif C == "/" and B != 0:
        return float(A/B)
    else:
        raise ZeroDivisionError("You can't divide from 0")