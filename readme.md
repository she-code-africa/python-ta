# Python Track Assessment

## Instructions

This repo contains the accessment exercise for the Python Track
Please perform the following instructions.

* Fork this repository.
* Clone the repository to your local computer.
* Add your solution to the specificied position.
* Commit your solution.
* Push your update to your repository.
* Submit your repository URL on the provided google form.

## Structure

The directory structure of this template

``` html
python-ta/
.
├── readme.md
├── src
│   ├── __init__.py
│   └── app.py
└── test.py

```

## Example

``` py
# src/app.py

def solution(n):
    # your code goes here


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    n = int(sys.argv[1])
    print(solution(n))

```

## Running your code

Write your solution in the way your pass the argument into the program via the commandLine/Terminal.

``` shell
# invoke the solution
$: python src/app.py <input>
```

## Testing

The [test](test.py) containers some basic test to make sure your solution are correct. Run the test to verify.
``` shell
$: python -m unittest test
```

## Need Help

contact: ***
