import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]


cx_Freeze.setup(
    name = "Flappy Bird by LAXMAN",
    options = {"build_exe": {"packages":["pygame"], "include_files":["bird.png"]}},
    executables = executables
    )
