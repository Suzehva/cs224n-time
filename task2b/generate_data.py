# TASK 2B:
# Dataset format: "The president of the United States is Barack Obama. Who was the
# president [year] years before Obama?". This dataset will assess the LM’s temporal
# reasoning (ability to reason about relative time).

# input format: list of (prompt, [solns])
PROMPTS = [
    ("The current president of the US is John F. Kennedy. The president 10 years ago was ", "Harry Truman"),
    ("The current president of the US is George Washington. The president 10 years ago was ", "None"),
    ("The current president of the US is Thomas Jefferson. The president 10 years ago was ", "John Adams"),
    ("The current president of the US is James Madison. The president 10 years ago was ", "Thomas Jefferson"),
    ("The current president of the US is James Monroe. The president 10 years ago was ", "James Madison"),
    ("The current president of the US is Andrew Jackson. The president 10 years ago was ", "James Monroe"),
    ("The current president of the US is Martin Van Buren. The president 10 years ago was ", "John Quincy Adams"),
    ("The current president of the US is John Tyler. The president 10 years ago was ", "Andrew Jackson"),
    ("The current president of the US is James K. Polk. The president 10 years ago was ", "Andrew Jackson"),
    ("The current president of the US is Franklin Pierce. The president 10 years ago was ", "John Tyler"),
    ("The current president of the US is James Buchanan. The president 10 years ago was ", "James K. Polk"),
    ("The current president of the US is Abraham Lincoln. The president 10 years ago was ", "Franklin Pierce"),
    ("The current president of the US is Ulysses S. Grant. The president 10 years ago was ", "James Buchanan"),
    ("The current president of the US is Rutherford B. Hayes. The president 10 years ago was ", "Abraham Lincoln"),
    ("The current president of the US is Benjamin Harrison. The president 10 years ago was ", "James Buchanan"),
    ("The current president of the US is William McKinley. The president 10 years ago was ", "Ulysses S. Grant"),
    ("The current president of the US is Theodore Roosevelt. The president 10 years ago was ", "Rutherford B. Hayes"),
    ("The current president of the US is Woodrow Wilson. The president 10 years ago was ", "Grover Cleveland"),
    ("The current president of the US is Calvin Coolidge. The president 10 years ago was ", "William McKinley"),
    ("The current president of the US is Franklin D. Roosevelt. The president 10 years ago was ", "Woodrow Wilson"),
    ("The current president of the US is Harry S. Truman. The president 10 years ago was ", "Calvin Coolidge"),
    ("The current president of the US is Dwight D. Eisenhower. The president 10 years ago was ", "Franklin D. Roosevelt"),
    ("The current president of the US is Lyndon B. Johnson. The president 10 years ago was ", "Harry S. Truman"),
    ("The current president of the US is Richard Nixon. The president 10 years ago was ", "Dwight D. Eisenhower"),
    ("The current president of the US is Jimmy Carter. The president 10 years ago was ", "Lyndon B. Johnson"),
    ("The current president of the US is Ronald Reagan. The president 10 years ago was ", "John F. Kennedy"),
]

def generate_task2b(prompts):
    with open('task2b/task2b-with-solns.data', 'w', newline='',) as file:
        for text, value in prompts:
            file.write(text + " | " + value + "\n")
    with open('task2b/task2b.data', 'w', newline='',) as file:
        for text, value in prompts:
            file.write(text + "\n")  ## just the prompts
 
if __name__ == "__main__":
    generate_task2b(prompts=PROMPTS)
