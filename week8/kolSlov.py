import functools
print(
    len(
        set(
            functools.reduce(
                lambda x, y: x + y, 
                list(
                    map(
                        lambda x: x.split(), 
                        open('input.txt').readlines()
                    )
                )
            )
        )
    )
)
