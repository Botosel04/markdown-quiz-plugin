import re
from mkdocs.plugins import BasePlugin

class QuizPlugin(BasePlugin):
    
    pattern = re.compile(r"'''question\s+(.*?)'''", flags=re.DOTALL)
    answer_pattern = re.compile(r'^\s*\[\s*\]\s*(.+)$', re.MULTILINE)

    def on_page_content(self, html, **kwargs):
        
        def make_quiz(match):
            content = match.group(1)
            lines = [line.strip() for line in content.split('\n') if line.strip()]
            
            question = lines[0] if lines else ""
            answers = [line[3:].strip() for line in lines[1:] if line.startswith('[ ]')]
            
            buttons = ''.join(f'<button class="quiz-btn">{ans}</button>' for ans in answers)
            
            return f'''
            <div>
                <p>{question}</p>
                <div>
                    {buttons}
                </div>
            </div>
            '''

        return self.pattern.sub(make_quiz, html)