#! /bin/python3
if __name__ == '__main__':
    import sys
    import os

    assert len(sys.argv) == 3
    n_problem, title = sys.argv[1:]
    filename = f"p{n_problem.zfill(3)}_{'_'.join(title.lower().split(' '))}.py"
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(f'"""\n\n"""\n')
