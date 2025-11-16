import re
from mkdocs.plugins import BasePlugin

# 1. Define our regular expressions (Regex)

# This pattern is for US #23 (creating questions)
# It looks for lines starting with "::question::" and captures (.*?) everything after it
QUESTION_REGEX = re.compile(
    r'^::question::(.*?)$',  # $ ensures it matches only to the end of the line
    flags=re.MULTILINE | re.DOTALL  # MULTILINE makes ^ match start of lines, DOTALL makes . match newlines
)

# This pattern is for US #24 & #26 (creating answers and defining correct ones)
# It looks for lines starting with [ ] or [x]
ANSWER_REGEX = re.compile(
    r'^\s*\[( |x)\]\s*(.*)',  # \s* allows indentation at the start of the line
                            # \[( |x)\] finds the brackets and captures (Group 1) the " " or "x" inside
                            # \s* allows spaces between brackets and text
                            # (.*) captures (Group 2) the answer text
    flags=re.MULTILINE       # MULTILINE makes ^ match start of each line
)

# 2. Write our plugin class

class QuizPlugin(BasePlugin):

    # on_page_markdown is the core "hook" for MkDocs plugins
    # MkDocs sends all markdown text to this function before converting it
    def on_page_markdown(self, markdown, **kwargs):
        
        # Step 1: Process Questions
        # We use a simple .sub() (substitution)
        # to replace "::question::My question"
        # with "<div class="quiz-question">My question</div>"
        # The r'\1' here refers to the captured (Group 1) from QUESTION_REGEX
        markdown = QUESTION_REGEX.sub(
            r'<div class="quiz-question">\1</div>', 
            markdown
        )
        
        # Step 2: Process Answers
        # This substitution is more complex because we need to check [ ] vs [x]
        # So, instead of passing a "replacement string", we pass a "replacement function"
        markdown = ANSWER_REGEX.sub(
            self._answer_replacer,  # Tells .sub(), "for every match you find, send it to the _answer_replacer function"
            markdown
        )

        return markdown


    # This is a "helper function" to handle the complex replacement from Step 2
    # Python's re.sub() automatically passes the "match object" to it
    def _answer_replacer(self, match):
        
        # "match.group(1)" gets the 1st captured group from ANSWER_REGEX
        # which is either ' ' or 'x'
        marker = match.group(1)
        
        # "match.group(2)" gets the 2nd captured group
        # which is the "answer text"
        text = match.group(2)
        
        # Now, we check if the marker was 'x'
        if marker == 'x':
            is_correct = "true"
        else:
            is_correct = "false"
            
        # Based on the check above, return a brand new HTML string
        # This is the final product for US #24 & #26:
        # A clickable button with a data-correct attribute
        return f'<button class="quiz-answer" data-correct="{is_correct}">{text}</button>'