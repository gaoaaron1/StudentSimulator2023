# !usr/bin/env python3

# For reference, here is a text-based version of the game (still a WIP).


from __future__ import annotations

import textwrap
from collections import Counter
from dataclasses import asdict, astuple, dataclass
from operator import add, sub
from typing import Iterator, Literal, NamedTuple

from typing_extensions import Self

# Constants.

DECISIONS_PER_TERM = 5
TERMS = {
    1: "fall",
    2: "winter",
    3: "summer/spring",
}
HELP_TEXT = textwrap.dedent(
    """
    To select an option, type the number beside it.
    As an example, if presented with the following
    menu:

    \t0: Do <X>.
    \t1: Do <Y>.

    Your input would be "0" if you wanted to do <X>.\n
    """
)


# Comparisons between students work the same as regular sequence
# comparisons in Python, so ordering works without issues.


@dataclass(order=True)
class Stats:
    academic: int = 0
    wellness: int = 0
    social: int = 0
    coins: int = 0

    def __iter__(self) -> Iterator:
        yield from astuple(self)

    def __add__(self, other: Self) -> Self:
        return type(self)(*map(add, self, other))

    def __sub__(self, other: Self) -> Self:
        return type(self)(*map(sub, self, other))

    def __str__(self) -> str:
        return "({})".format(", ".join(f"{v:+} {k}" for k, v in asdict(self).items()))


class Job(NamedTuple):
    requirements: Stats

    def is_qualified(self, student: Student) -> bool:
        return student.graduated and student.stats >= self.requirements


class Action(NamedTuple):
    name: str
    stats: Stats


TermString = Literal["fall", "winder", "summer/spring"]
DecisionString = Literal[
    "clubbing", "take course", "working out", "therapy", "volunteering", "interning"
]

ACTIONS = [
    Action(name="clubbing", stats=Stats(social=1)),
    Action(name="take course", stats=Stats(academic=1, coins=-1000)),
    Action(name="work out", stats=Stats(wellness=1)),
    Action(name="therapy", stats=Stats(wellness=1)),
    Action(name="volunteering", stats=Stats(social=1)),
    Action(name="interning", stats=Stats(social=1, coins=1000)),
    Action(name="spritual acitivities", stats=Stats(wellness=1)),
]

ACTION_MAP = dict(enumerate(ACTIONS))


@dataclass
class Student:
    year: int
    term: TermString
    stats: Stats = Stats(coins=10_000)
    courses_taken: int = 0
    graduated: bool = False

    @property
    def balance(self) -> int:
        return self.stats.coins

    @balance.setter
    def balance(self, value: int) -> None:
        self.stats.coins += value

    def display_actions(self, term: str, year: int) -> None:
        """Displays the actions a student can take when given a term and a year."""
        print(
            f"\nYou are currently in the {term} term, and a year {year} student.",
            "\nCurrent stats: " + str(self.stats),
            "\nSelect an action: ",
            "-" * 64,
            sep="\n",
        )
        for i, (action, stats) in enumerate(ACTIONS):
            print(f"{i}. {f'{action}: ':20s}", str(stats))


def play() -> None:
    student = Student(year=1, term="fall")
    for year in range(1, 5):  # Represents years 1 and 4 inclusive.
        for term in TERMS.values():
            counts = Counter()  # type: ignore
            for _ in range(DECISIONS_PER_TERM):
                print(f"Current Balance: ${student.balance}")
                student.display_actions(term, year)
                print("-" * 64)
                while True:
                    try:
                        choice = int(input())
                    except ValueError:
                        print("Invalid option, please try again.")
                    else:
                        if choice >= len(ACTIONS):
                            print("Invalid option, please try again.")
                            continue
                        action = ACTION_MAP[choice]
                        if action.name == "interning" and counts["interning"] == 2:
                            print("Cannot intern more than twice in a term.")
                            continue
                        student.stats += action.stats
                        counts += Counter({action.name: 1})
                        break
                if student.balance < 0:
                    print("Balance went below $0. Game over.")
                    exit()
                if student.courses_taken == 40:
                    student.graduated = True
        student.year = year


def main() -> None:
    print("Welcome to Student Simulator.")
    while True:
        print("Please select an action: ", "\t0: Play", "\t1: Help", sep="\n")
        choice = input("choice: ")
        print()
        match choice.casefold():  # Ignore case.
            case "0" | "play" | "p":
                play()
                break
            case "1" | "help" | "h":
                print(HELP_TEXT, "going back to main menu.", sep="\n")
                continue
            case _:
                print("Invalid input. Please try again.\n")


if __name__ == "__main__":
    main()
