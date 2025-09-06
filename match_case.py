
def evaluate(exp: Expression, env: Environment) -> Any:
    match exp:
        case ['quote', x]:
            return x
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        case ['lambda', [*parms], *body] if body:
            return Procedure(parms, body, env)
        case ['define', Symbol() as name, value_exp]:
            env[name] = evaluate(value_exp, env)
        case ['define', [Symbol() as name, *parms], *body] if body:
            env[name] = Procedure(parms, body, env)
        case _:
            raise SyntaxError(lispstr(exp))
        
