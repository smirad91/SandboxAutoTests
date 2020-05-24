class UseCase:
    """
    Stores all data from use case
    """
    def __init__(self, title, description, expected_result, steps):
        self.title = title
        self.description = description
        self.expected_result = expected_result
        self.steps = steps

    def edit_on_specific_way(self):
        """
        Edit all parameters by replacing it with string
        "This field previously had"+No of characters+"characters"
        """
        # log.info("Edit use case all fields in pattern: 'This field previously had x characters' ")
        self.title = "This field previously had {} characters - Delete me".format(len(self.title))
        self.description = "This field previously had {} characters".format(len(self.description))
        self.expected_result = "This field previously had {} characters".format(len(self.expected_result))
        # log.info("New fields: {},{},{}".format(self.title, self.description, self.expected_result))
        new_steps = []
        for step in self.steps:
            step_text = "This field previously had {} characters".format(len(step))
            new_steps.append(step_text)
            # log.info("New step: {}".format(step_text)
        self.steps = new_steps
        # log.screenshot("Fields are edited.")

    def which_step_deleted(self, edited_steps):
        """
        Returns step that is missing
        :param edited_steps: Steps as in current use case but with one less step
        :type: UseCase
        """
        # log.info("Find deleted step from {} and {}".format(self.steps, edited_steps))
        deleted_step = set(self.steps).difference(set(edited_steps))
        step = deleted_step.pop()
        # log.info("Deleted step is {}".format(step))
        return step


