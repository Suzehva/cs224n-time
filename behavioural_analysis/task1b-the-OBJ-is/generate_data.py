# TASK 1B:
# LM input: "Who is the president of the United States?", "When is the next Olympics?",
# etc. The answer to these questions will help us place the LMs in a specific time.

TEMPLATES = ["The current president of the US is ", # Donald Trump, as of 2025
            "The next Olympics will take place at ", # Milan & Cortina d'Ampezzo, Italy, as of 2025
             "The newest COVID variant is ", # XEC, as of 2025
             "The latest iPhone model is ", # iPhone 16, as of 2025
             "The most recent FIFA World Cup winner is ", # Argentina, in 2022
             "The previous Nobel Prize in Physics went to ", # John J. Hopfield and Geoffrey Hinton in 2024
             "The previous president of the US is ", # Joe Biden, as of 2025
             "The previous Olympics took place at ", # Paris France, in 2024
             "The most recent Best Picture winner at the Oscars is ", # Oppenheimer, as of 2024
             "The current Prime Minister of the UK is ", # Keir Starmer, as of 2024
             "The current CEO of Twitter is ", # Elon Musk, as of 2025
             "The latest version of macOS is ", # macOS 15 Sequoia, as of 2024
            ]

# TODO: generate more prompts by sweeping over...
# "previous"/"current"/"next"  
# change how we phrase the query

def generate_task1b(templates):
    with open('task1b/task1b.data', 'w', newline='',) as file:
        for template in templates:
            file.write(template + "\n")
    
if __name__ == "__main__":
    generate_task1b(templates=TEMPLATES)
