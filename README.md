# Yu-Gi-Oh Card Generator
This will become an application that will let users create their own Yu-Gi-Oh cards and save them to the database.

## MVP
These are the following goals for the MVP:
- [ ] Users can register, log in, and delete their accounts
- [ ] Logged in users can create Yu-Gi-Oh cards (but they can't add images yet)
- [ ] They can save those cards to the database
- [ ] Tests for *almost* **everything**
- [ ] All cards are **non-effect** monster cards only.
    - After successfully being able to add monster cards to db, will start to look into adding spell/trap/monster effect cards. Will need to use polymorphism and add a Card parent class for all other card classes to use.
    - Said Card parent class will be used for endpoint to get **all** cards

## Getting to the MVP
In order to get there, we'll need to take one small step at a time.

---

## Post-MVP
These will be the next goals:
- [ ] Create a front-end with a nice UI to make creating cards easier
- [ ] Users will be able to add pictures and save those too to the database
- [ ] Users will be able to construct their own decks from the cards they generated

## Endgame
This card generator will be the basis for the eventual Yu-Gi-Oh game I'd like to create.
Users will be able to create any card they'd like and battle it out against an AI, or opponents.
This however, is something I have planned for in the *far future*.
So for now, the top priority is just to get to the MVP.