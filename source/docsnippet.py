import re

class DocSnippet:
    """
    This class represents a function in Python, and its related information:

    function_name   - the name of the function
    parameter_names - a list of parameters the function takes
    return_name     - the name of the return parameter
    """

    def create(self, function_name, parameter_names, return_name, function_comment):
        self.function_name = function_name
        self.parameter_names = parameter_names
        self.return_name = return_name
        self.function_comment = function_comment
        self.score = 0
        self.comment_length = len(str(function_comment))

    def match_in_snippet(self, term):
        # If the term is found in the snippet, return true, else return false

        return re.search("(.*)(\s)" + "\\b" + re.escape(term)
                         + "\\b" + "[,\" :-]*[*]*[,\" :-]*(.*)",
                         self.function_comment)

    def covers_function(self):
        # Parse the document snippet
        # Check if it contains the function name as an exact match

        return self.match_in_snippet(self.function_name)

    def covers_parameters(self):
        # Parse the document snippet
        # Check if it contains the parameter names

        for parameter in self.parameter_names:
            if not self.match_in_snippet(parameter):
                return False
        return True

    def covers_return(self):
        return self.match_in_snippet(self.return_name)

    def get_comment_length(self):
        return self.comment_length

    def get_score(self):
        """
        We define score for now to be weighted as:

        0 or 50 for whether the function_name is covered
        0 to 25 for whether the parameter_names are covered
        0 to 25 for whether the return_name is covered
        """
        score = 0
        if self.covers_function():
            score = score + 50
        if self.covers_parameters():
            score = score + 25
        if self.covers_return():
            score = score + 25

        return score
