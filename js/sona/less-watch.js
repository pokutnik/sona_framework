;(function(window, undefined){
    console.log("start watch hook");
    var cache = window.localStorage ||  null;
    cache.clear();    
    var watchTimer = setInterval(function (){
        less.refresh(true);
    }, 5000);
})(window);
