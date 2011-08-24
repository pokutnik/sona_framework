# Sona less

A [less][less]-based CSS Framework for developing layouts that allows you to mix and match any of the following CSS frameworks:

 * [sona_gs] - Sona grid system. Allows you to create grid based layouts 
 * [rhythm] - toolbox for perfect vertycally alligned texts and boxes
 * [utils] - widely used helper functions like clearfix
 * [reset] - collection of CSS resets: html5doctor, mayer, yui
 * in future some popular CSS frameworks
 


## Sona less framework Provides

0. Great power of [less][less]. So you write Less instead of Css use variables and mixins in your code 
1. Easy and flexible way to create grid based layout.
2. Great local layout development enviroment. (Autoreloading styles, local webserver)
3. Skeleton for creation responsible design


## Quick Start

1. Grab a copy of this repo `git clone http:\\` or [link to zip]
2. Include sona less framework in your html

    <!-- link jQuery -->
    <script src="js/libs/jquery-1.5.2.js"></script>
    <!-- link sona grid system js files -->
    <script src="js/sona/css.js"></script>
    <script src="js/libs/less-1.1.3.js"></script>
    <!-- link to enable auto styles refresh -->
    <script src="js/sona/less-watch.js"></script>
    <!-- include main dev.less file -->
    <script>
        css.load('dev.less', 'stylesheet/less', 'dev_css');
    </script>

3. Open your html in browser. 
4. Code layout in `dev.less` file. Changes will automaticly reloded so you will see them directly in browser without reloading page.
 


## More Information

## Author
Sona less framework is written by Pokutnik Alexandr and Jievgenii Likhovidov at [Sona studio][http://sona-studio.com].<br>

## License
Copyright (c) 2008-2009 Sona studio<br>
All Rights Reserved.<br>
Released under a ...  License.


[less]: http://lessjs.com/ "Less CSS"
