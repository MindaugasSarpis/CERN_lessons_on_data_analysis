# 1: Motivation and Introduction to CERN Engineering Infrastructure

---

## Seminar

### Use KeyViz

- Explain that we are starting very slowly, but working toward the endgame

- Split them into tutors and students (well versed and just starting )

- Ask about different OS people are using

- Talk about windows / applications

- Talk about people typing on phones / ipads

- Talk about touchtyping https://typer.io/lobby

- Talk about one-time vs repeatable tasks

- Show Incompatibility, versions (SaveAs...)

- Show MS Word -> XML Catalogue

- Sketch a diagram of computing / research project

- Talk about Scriptable vs Non-Scriptable Applications (Slides)

- Show tesseract example on ChatGPT

- Introduce concepts of modularity and reusability

- Install [Python](https://www.python.org/)

- Explain about multiple python installations

- Explain about differences in OSs

- Go to python interpreter

  - Explain about CLI

  - Explain what prompt is

  - Show how to exit (quit(), exit(), Ctrl-D, Ctrl-Z)

  - Show how to get help (help(), help('keywords'))

  - [tutorial](https://docs.python.org/3/tutorial/introduction.html)

    ```python
    2 + 2

    50 - 5*6

    (50 - 5*6) / 4

    8 / 5  # division always returns a floating-point number
    ```

    - Types (**int, float**)

    ```python
    17 / 3  # classic division returns a float
    
    
    17 // 3  # floor division discards the fractional part
    
    17 % 3  # the % operator returns the remainder of the division
    
    5 * 3 + 2  # floored quotient * divisor + remainder
    ```

    - Powers

    ```python
    5 ** 2  # 5 squared
    2 ** 7  # 2 to the power of 7
    ```

    - Variable asignments

    ```python
    width = 20  # variable names can be a single letter or more descriptive names
    height = 30
    area = width * height
    ```

    Naming **Conventions** for **Variables**

    - **Single lowercase** letter

      - a

      - b

      - c

    - never use l (Lima)

    - **Single Uppercase** letter

      - A

      - B

      - C

    - never use O (Oscar) or I (India)

    - **lowercase**

      - velocity

      - temperature

      - total

    - **lower_case_with_underscores**

      - user_age

      - file_name

      - calculate_total

    - **UPPERCASE**

      - PI = 3.14159
  
      - MAX_SIZE = 100
  
      - DEFAULT_TIMEOUT = 30
  
      - DEBUG_MODE = True

    - **UPPER_CASE_WITH_UNDERSCORES**

      - DEFAULT_USER_ROLE = "guest"

      - CONNECTION_TIMEOUT_LIMIT = 60

      - MAX_BUFFER_SIZE = 1024

    - **CamelCase**

      - DataProcessor

      - HTTPRequestHandler

      - XMLParser

    - Acronyms are capitalized

    - **mixedCase**

      - fileReader

      - isEnabled

      - getValue

- Install VS Code [Tutorial](https://code.visualstudio.com/docs/setup/setup-overview)

- Talk about buttons and how not to use them

- Use textfiles files .txt

- Talk about intellisense

- Introduce extensions - show thesis, slides

