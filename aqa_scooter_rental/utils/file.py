def path_from_project(relative_path: str):
    import aqa_scooter_rental.utils
    from pathlib import Path

    return (
        Path(aqa_scooter_rental.utils.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
