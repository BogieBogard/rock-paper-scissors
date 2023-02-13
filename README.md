# Rock, Paper, Scissors

A simple Rock, Paper, Scissors game, completed as part of a job application process for a software engineering position.

## View the App

To view this app, you can:

1. Clone this repository and visit the `index.html` file in your web browser.

Or,

2. Visit the live version of the site at: [https://mbogard.com/rps](https://mbogard.com/rps)

## Approach

1. I started the project by importing Bootstrap to set up basic HTML and CSS structure, which allowed me to quickly focus on the logic of the RPS game.

2. I used jQuery to build the core logic of the game. For large enterprise applications, I believe React is a better solution for the front-end. However, for small projects like this with a time limit, I prefer jQuery because it allows me to build functionality slightly faster.

3. I completed the core logic of the game in about two hours. The game includes the following features:
  - Two players can enter their names.
  - A user can play against the computer.
  - After each round, the winner is shown and the scores are incremented.

4. After completing these features, instead of working on the rest of the features described in the assignment, I decided to pivot to demonstrate my tech stack flexibility. I built a new page for the same game that uses Python code for some of its logic instead of JavaScript. In this new version, when a user chooses rock, paper, or scissors, the script makes a call to a Python service in my Google Cloud Platform account, which provides a response that is then consumed by the later jQuery code. There is a link to the Python page at the bottom of the `index.html` page.

5. If I had more time then I would have liked to add the rest of the features listed in the assignment. Specifically, I would like to support two player mode--currently the game only support one player versus the computer. Additionally I would like to add a "save game" feature.

### Thank you for your time and consideration!