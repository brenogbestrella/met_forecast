
# README #

## WELCOME ABOARD ##

This **README** is the entrypoint to your journey into the GOL's Ops Analytics team. Here, we're going to challenge you
in order to have a better understanding of your perceptions and tech skills.

First of all, **_pay attention to the rules_**. Those rules will guide you through the challenge and help to avoid
some traps:

- Read the documentation.
- There's no right way, but we have a direction to follow.
- Save your breath! Perform exactly what's necessary.
- Leave us a breadcrumb trail. Comment your code during the path.
- Feel free to carry some technology in your luggage.
- Don't cheat. We will know and your journey will end earlier.

## WHAT WE WANT ##

Barring a few exceptions, it doesn't matter if you've had a formal programming study. What matters is what you really know! 

We hope you will be able to build, fix, critique, and improve the app. But, as we said before, there is no right way here. Feel free to explore the different ways to solve the challenge. As a matter of fact, we don't count the possible versions.

**However**, we are challenging you to code a Python-Django app, so we will not accept another one, okay?


## A SHORT BRIEF ##

The purpose here is to share a small piece of what we are used to on a daily basis. Nothing better than using a real case, right?

Let's work! In this challenge, we intend to satisfy a client's needs by building a solution to obtain some meteorological data. They are not
common weather data. We need to provide a [METAR][1] message! Please, we don't want you to know about weather message! (yet) So abstract this knowledge and focus on solving the challenge by bringing in the data using the [REDEMET API][2].

Forget the front end, okay? Let's focus on the backend to create a simple [Django][3] project to feed clients with METAR, through just one endpoint in the API. Feel free to name your end-point whatever you like, but a customer will not like to request an end-point called "foo" or "bar". Obviously!

We purposely leave some bad/incomplete code, errors, easter eggs, and shortcuts. Of course, it's part of this challenge to solve then. But don't be afraid! The challenge doesn't have a correct formal answer. But you can't go so far away! 

You will have the time and freedom to consult official documentation and equivalents. Do not hesitate to use it well!

Below we are going to share a recipe for making THE cake. By following this recipe correctly and using the right ingredients, you can't go wrong!

## RECIPE ##

1. Clone the bitbucket [repo][4] to your local repository
2. Build your environment
3. Take a look around in the project and explore the legacy code
4. Run your first run.py
5. Fix some issues
6. Implement a log routine to write all the responses coming from REDEMET API requests
6. Build a Django project **_api_** into **_src/_** then an **_app_** inside **_src/api/_**
8. Test if your raw Django project is running correctly
8. Create the end-point in the app views
8. Configure the URL to reach the end-point 
9. Connect the pipe to response through the end-point
10. Run your Django project and perform a http request to return a METAR message

[1]: https://pt.wikipedia.org/wiki/Metar "Wikipedia"
[2]: https://www.redemet.aer.mil.br/?i=facilidades&p=api-redemet "REDEMET API Link"
[3]: https://www.djangoproject.com/ "Official Django Website"
[4]: https://bitbucket.org/danrantunes/met_forecast/src/master/ "Bitbucket @danrantunes"


