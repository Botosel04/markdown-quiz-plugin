MkDocs Interactive Quiz Plugin

The MkDocs Quiz Plugin transforms static documentation into engaging, interactive learning experiences through diverse question formats.

It addresses key challenges in modern documentation: it transforms passive reading into active learning, provides immediate verification, and enables interactive content creation without technical expertise.

✨ Features

Author in Markdown: Write quizzes using a simple, intuitive text syntax. No HTML required.

Diverse Question Types: Supports Single/Multiple Choice, Dropdowns, Drag-and-Drop Ordering, Matching, and Picture questions.

Instant Verification: Immediate feedback for users as they learn.

Advanced Configurations: Support for timers, passing scores, layouts (list/book), and randomized shuffling.

Explanations & References: Link answers directly to specific documentation sections to reinforce learning.

Modular: Reuse and import quizzes across different files using the @include directive.

📦 Installation

Before you begin, ensure you have Python 3.8+ and MkDocs 1.0+ installed.

Install the mkdocs-quiz-plugin package from TestPyPI using pip:

pip install -i [https://test.pypi.org/simple/](https://test.pypi.org/simple/) mkdocs-quiz-plugin


Add the plugin to your mkdocs.yml file to enable it for your project:

plugins:
  - search
  - quiz


🚀 Quick Start

To create a quiz, wrap your questions inside @START and @END tags. Use [x] to mark the correct answer.

@START
@title: Math Basics Quiz
@time_limit: 60

What is 2 + 2?
[ ] 3
[x] 4
[ ] 5

---

What is 3 × 3?
[ ] 6
[ ] 8
[x] 9
@END


📚 Full Documentation

This README is just a quick start guide. The plugin supports advanced features like:

Matching: {Leonardo da Vinci | Mona Lisa}

Ordering: (1.) Step one, (2.) Step two

Dropdowns: {{Correct|Wrong1|Wrong2}}

Detailed Explanations & Anchors: @explanation: Read more [here](#anchor)

For the complete keyword reference, advanced usage, and FAQ, please see our Full Documentation. (Note: Update this link to point to wherever your documentation is hosted/stored).

🤝 Contributions

We welcome contributions from the community!

Fork the repository.

Clone your fork and set up a virtual environment.

Install dependencies: pip install -e .

Create a new branch, make your changes, and submit a Pull Request.

📄 License

MIT
