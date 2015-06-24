# RoutePlaningHere

This project is the result from the 2015 Hackathon/Mapathon at HERE in Berlin.
It's also a simple example of how the api can be used.

The goal was a tool solving a optimizing problem to create the best route using a starting point (last point defined in cordinates.txt), waypoints (all other points defined in cordinates.txt) and a maximum time (currently 8 hrs).
Input: List of coordinates
Output: Sortet list of coordinates defining the calculated route, time needed for that route (and currently some debug information like a request of the whole route at once) or an error (probably because of not viable coordinates).


The tool currently is pretty simple, using a greedy algorithm to find the fastest point to get to. It is currently indeed not very intelligent and needs a lot of time for all the requests to the api.
There is much room for improvement like

- a better README.md (oh boy rly?)
- better input handling, also for the maximum time
- a better algorithm or providing different algorithms
- using a secure https connection to the api
- better internal variable handling (e.g. saving "app_id" and "app_code" in variables instead of writing those in each URL seperately)
- aaaand I guess much much more....

## Contribution and License

If you have interest in doing stuff (like adding improvements), feel free to contribute or fork and play with the code.
This is just a simple example - so completely open source and for use for everything and everyone (but please don't do bad stuff - that's bad).

PS.: You may need to get an app_id and an app_code via registration at https://developer.here.com/ .
