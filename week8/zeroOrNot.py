print(
    any(
        list(
            map(
                lambda x: int(input()) == 0, 
                range(
                    int(
                        input()
                    )
                )
            )
        )
    )
)
