gridnav
=======

Algorithms for generating collision and navigation data using Dota 2 navgrids.

![](http://i.imgur.com/37k200l.png)

Floodfill
========

The algorithm first performs a floodfill from a specified point to get the "pathable" track area. For dotadash this is used to calculate the pathable "track" where players can move.

The algorithm then marks all of the edges of this area as edges.

Edge Angle Calculation
=========

The algorithm, for each of the edge points, calculates the angle towards the pathable area. This is used to calculate the collision later and is used as a smooth normal for the jagged wall.

This data is exported to a format friendly with the Lua engine in Dota 2.
