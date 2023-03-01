class Poll:
    """
    A class representing a poll with a question and multiple options.

    Attributes:
        question (str): The question asked in the poll.
        options (list): A list of strings representing the options for the poll.
        votes (dict): A dictionary representing the votes for each option.

    Methods:
        vote(vote): Adds a vote to the specified option.
        add_option(option): Adds a new option to the poll.
        remove_option(option): Removes an existing option from the poll.
        get_votes(): Returns a list of tuples representing the options and their vote counts.
        get_winner(): Returns the option with the highest vote count.
    """

    def __init__(self, question: str, options: list[str]) -> None:
        self.question = question
        self.options = options
        self.votes = dict(zip(options, [0 for i in range(len(options))]))

    def vote(self, vote: str):
        """Adds a vote to the specified option."""
        self.votes[vote] += 1

    def add_option(self, option: str):
        """Adds a new option to the poll."""
        if option not in self.options:
            self.options.append(option)
            self.votes.update({option: 0})

    def remove_option(self, option: str):
        """Removes an existing option from the poll."""
        if option in self.options:
            self.options.remove(option)
            self.votes.pop(option)

    def get_votes(self) -> list[tuple[str, int]]:
        """
            Return a list of tuples containing the options and their vote counts,
            sorted in decreasing order by the vote count.
        """
        return sorted([(key, value) for key, value in self.votes.items()], key=lambda element: element[1], reverse=True)

    def get_winner(self) -> str:
        """Return the option with the highest vote count."""
        return max(self.votes, key=lambda k: self.votes[k])
