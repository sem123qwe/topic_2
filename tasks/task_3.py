custem_sep: str = '\n'
print('Python is an', '\tinterpreted,', '\thigh-level,',
      '\tgeneral-purpose', 'programming language.', sep=custem_sep)

# -----
var: str = ('Python is an\n\tinterpreted,\n\thigh-level,'
            '\n\tgeneral-purpose\nprogramming language.')
print(var)

# -----

var_2: str = """Python is an
    interpreted,
    high-level,
    general-purpose
programming language.
"""

print(var_2)
