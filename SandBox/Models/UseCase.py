class UseCase:
    def __init__(self, title, description, expected_result, steps):
        self.title = title
        self.description = description
        self.expected_result = expected_result
        self.steps = steps

    def edit_characters(self):
        self.title = "This field previously had {} characters".format(len(self.title))
        self.description = "This field previously had {} characters".format(len(self.description))
        self.expected_result = "This field previously had {} characters".format(len(self.expected_result))
        new_steps = []
        for step in self.steps:
            new_steps.append("This field previously had {} characters".format(len(step)))
        self.steps = new_steps;
